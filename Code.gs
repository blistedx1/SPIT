/**
 * =====================================================================
 * PANCHSHILA INTERNATIONAL SCHOOL - CENTRALIZED EXECUTIVE SYSTEM
 * GOOGLE APPS SCRIPT HIGH-PERFORMANCE BACKEND (Code.gs)
 * =====================================================================
 * Features:
 *  - High-speed CacheService (L1 in-memory) + PropertiesService (L2 cloud)
 *  - Automatic Real-time Spreadsheet Synchronization ('Staff_Registry' sheet)
 *  - LockService concurrency protection against simultaneous write collisions
 *  - Reliable Indian Standard Time (IST) timezone handling on Google Cloud
 *  - Both Web App UI (doGet) and REST JSON API (doGet/doPost) support
 * =====================================================================
 */

/**
 * 1. WEB APP ENTRY POINT
 */
function doGet(e) {
  // Support REST API endpoint queries (e.g. ?action=getRegistry or ?action=liveStatus)
  if (e && e.parameter && e.parameter.action) {
    return handleApiGet(e);
  }

  var template;
  try {
    template = HtmlService.createTemplateFromFile('Index');
  } catch (err1) {
    try {
      template = HtmlService.createTemplateFromFile('index');
    } catch (err2) {
      return HtmlService.createHtmlOutput(
        '<div style="font-family:sans-serif; padding:40px; text-align:center;">' +
        '<h2 style="color:#dc2626;">Configuration Notice</h2>' +
        '<p>Please ensure your HTML file in Apps Script is named <strong>Index.html</strong> or <strong>index.html</strong>.</p>' +
        '</div>'
      );
    }
  }

  return template
    .evaluate()
    .setTitle('Panchshila International School Executive Dashboard')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * 2. POST WEBHOOK / REST API HANDLER
 */
function doPost(e) {
  try {
    var postData = "";
    if (e && e.postData && e.postData.contents) {
      postData = e.postData.contents;
    }
    
    var payload = {};
    if (postData) {
      try {
        payload = JSON.parse(postData);
      } catch (ex) {
        payload = e.parameter || {};
      }
    } else {
      payload = e.parameter || {};
    }

    var action = payload.action || (e && e.parameter ? e.parameter.action : "");

    if (action === "saveRegistry" && payload.registry) {
      var res = saveTeachersPinRegistry(payload.registry);
      return createJsonResponse({ status: "SUCCESS", result: res });
    }

    if (action === "processForm" && payload.formData) {
      var formRes = processForm(payload.formData);
      return createJsonResponse({ status: "SUCCESS", result: formRes });
    }

    return createJsonResponse({ status: "SUCCESS", message: "API Active" });
  } catch (err) {
    return createJsonResponse({ status: "ERROR", message: err.toString() });
  }
}

/**
 * Helper to include partial HTML files (Best Practice for Apps Script)
 */
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

/**
 * Helper: Resolve active or standalone spreadsheet safely
 */
function getTargetSpreadsheet() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    if (ss) return ss;
  } catch (e) {}

  try {
    var sheetId = PropertiesService.getScriptProperties().getProperty('SPREADSHEET_ID');
    if (sheetId) return SpreadsheetApp.openById(sheetId);
  } catch (e) {}

  return null;
}

/**
 * Helper: Indian Standard Time (IST) safe timezone resolver
 */
function getSystemTimeZone() {
  try {
    return Session.getScriptTimeZone() || "GMT+5:30";
  } catch (e) {
    return "GMT+5:30";
  }
}

/**
 * =====================================================================
 * STAFF REGISTRY ENGINE
 * =====================================================================
 */

var DEFAULT_SCHOOL_REGISTRY = {
  "Abhishek Tiwari": "4815",
  "Abhishek Yadav": "5142",
  "Anjali": "8214",
  "Anjali Shukla": "9044",
  "Ankita Gupta": "7291",
  "Anoop Kumar": "1468",
  "Aparna Ashok": "3333",
  "Astha Dixit": "5832",
  "Gagan Deep Singh Chauhan": "8104",
  "Gaurav Gupta": "2893",
  "Hari Om Singh": "9760",
  "Harsh Gupta": "6359",
  "Hemlata Singh": "9598",
  "Kavita Verma": "4172",
  "Lalit Verma": "8520",
  "Lubna Naqvi": "4431",
  "Monu": "3619",
  "Namita Singh": "3031",
  "Neeraj Singh": "5194",
  "Pratima Srivastav": "6281",
  "Priyanka Trivedi": "9352",
  "Raj Mohan Trivedi": "4916",
  "Riya Vimal": "8472",
  "Saurabh Tripathi": "4163",
  "Shalini Chauhan": "7825",
  "Shalu Saluja": "1958",
  "Shruti Shukla": "8840",
  "Shweta Malik": "2741",
  "Taranjeet Kaur": "6147",
  "Vandana": "6352",
  "Vikas": "7461"
};

function getTeachersPinRegistry() {
  // 1. Try In-Memory CacheService (Instant)
  try {
    var cached = CacheService.getScriptCache().get('CACHE_TEACHER_PINS');
    if (cached) {
      var parsedCache = JSON.parse(cached);
      if (parsedCache && typeof parsedCache === 'object' && Object.keys(parsedCache).length > 0) {
        return parsedCache;
      }
    }
  } catch (e) {}

  // 2. Try PropertiesService (Project Cloud Store)
  try {
    var stored = PropertiesService.getScriptProperties().getProperty('TEACHER_PINS');
    if (stored) {
      var parsed = JSON.parse(stored);
      if (parsed && typeof parsed === 'object' && Object.keys(parsed).length > 0) {
        try {
          CacheService.getScriptCache().put('CACHE_TEACHER_PINS', stored, 21600); // Cache for 6 hours
        } catch(cErr) {}
        return parsed;
      }
    }
  } catch (e) {}

  // 3. Try Google Spreadsheet Tab 'Staff_Registry'
  try {
    var ss = getTargetSpreadsheet();
    if (ss) {
      var staffSheet = ss.getSheetByName('Staff_Registry');
      if (staffSheet && staffSheet.getLastRow() > 1) {
        var values = staffSheet.getRange(2, 1, staffSheet.getLastRow() - 1, 2).getValues();
        var sheetRegistry = {};
        for (var i = 0; i < values.length; i++) {
          var name = String(values[i][0]).trim();
          var pin = String(values[i][1]).trim();
          if (name) sheetRegistry[name] = pin;
        }
        if (Object.keys(sheetRegistry).length > 0) {
          var jsonStr = JSON.stringify(sheetRegistry);
          try { PropertiesService.getScriptProperties().setProperty('TEACHER_PINS', jsonStr); } catch(err) {}
          try { CacheService.getScriptCache().put('CACHE_TEACHER_PINS', jsonStr, 21600); } catch(err) {}
          return sheetRegistry;
        }
      }
    }
  } catch (e) {}

  // 4. Default Seed Fallback
  var defJson = JSON.stringify(DEFAULT_SCHOOL_REGISTRY);
  try { PropertiesService.getScriptProperties().setProperty('TEACHER_PINS', defJson); } catch(e) {}
  try { CacheService.getScriptCache().put('CACHE_TEACHER_PINS', defJson, 21600); } catch(e) {}

  return DEFAULT_SCHOOL_REGISTRY;
}

/**
 * SAVE / SYNCHRONIZE COMPLETE REGISTRY
 * Concurrency protected with LockService
 */
function saveTeachersPinRegistry(registryObj) {
  if (!registryObj || typeof registryObj !== 'object') {
    return "ERROR: Invalid registry payload";
  }

  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(10000); // 10s wait lock for thread safety
  } catch (e) {
    Logger.log("Lock acquisition failed: " + e.message);
  }

  try {
    var jsonStr = JSON.stringify(registryObj);

    // 1. Update PropertiesService
    PropertiesService.getScriptProperties().setProperty('TEACHER_PINS', jsonStr);

    // 2. Refresh CacheService
    try {
      CacheService.getScriptCache().remove('CACHE_TEACHER_PINS');
      CacheService.getScriptCache().put('CACHE_TEACHER_PINS', jsonStr, 21600);
    } catch (e) {}

    // 3. Batch Update 'Staff_Registry' Sheet in Spreadsheet
    var ss = getTargetSpreadsheet();
    if (ss) {
      var sheet = ss.getSheetByName('Staff_Registry');
      if (!sheet) {
        sheet = ss.insertSheet('Staff_Registry');
      }
      sheet.clearContents();

      sheet.appendRow(["Staff Member Name", "Security PIN", "Status", "Last Synchronized"]);
      sheet.getRange(1, 1, 1, 4)
        .setFontWeight("bold")
        .setBackground("#059669")
        .setFontColor("#ffffff");

      var names = Object.keys(registryObj).sort();
      var nowStr = Utilities.formatDate(new Date(), getSystemTimeZone(), "dd-MMM-yyyy hh:mm a");
      var rows = [];
      names.forEach(function(n) {
        rows.push([n, String(registryObj[n]), "Active", nowStr]);
      });

      if (rows.length > 0) {
        sheet.getRange(2, 1, rows.length, 4).setValues(rows);
      }
    }

    return "SUCCESS";
  } catch (err) {
    Logger.log("saveTeachersPinRegistry error: " + err.message);
    return "ERROR: " + err.message;
  } finally {
    try { lock.releaseLock(); } catch(e) {}
  }
}

/**
 * DIRECT SINGLE MEMBER ADD / UPDATE
 */
function addOrUpdateStaffMember(name, pin) {
  if (!name || !pin) return "ERROR: Name and PIN required";
  var reg = getTeachersPinRegistry();
  reg[name.trim()] = String(pin).trim();
  return saveTeachersPinRegistry(reg);
}

/**
 * DIRECT SINGLE MEMBER DELETE
 */
function deleteStaffMember(name) {
  if (!name) return "ERROR: Name required";
  var reg = getTeachersPinRegistry();
  var trimmed = name.trim();
  if (reg[trimmed]) {
    delete reg[trimmed];
    return saveTeachersPinRegistry(reg);
  }
  return "NOT_FOUND";
}

function checkIfPinRequired(userName) {
  var pins = getTeachersPinRegistry();
  return Boolean(pins[userName] && pins[userName] !== "");
}

function verifyDownloadPin(userName, pin) {
  var pins = getTeachersPinRegistry();
  if (!pins[userName]) return false;
  return (String(pins[userName]).trim() === String(pin).trim());
}

/**
 * =====================================================================
 * LIVE TELEMETRY & ATTENDANCE STATUS
 * =====================================================================
 */
function getLiveAttendanceStatus() {
  var ss = getTargetSpreadsheet();
  var tz = getSystemTimeZone();
  var today = new Date();
  var dateStr = Utilities.formatDate(today, tz, "dd-MMM-yyyy");
  
  // Safe Hour Check respecting IST Timezone
  var hourStr = Utilities.formatDate(today, tz, "HH");
  var currentHour = parseInt(hourStr, 10);
  var isLocked = (currentHour < 12 || currentHour >= 20);

  var registry = getTeachersPinRegistry();
  var allTeachers = Object.keys(registry).sort();
  var statusMap = {};

  allTeachers.forEach(function(t) {
    statusMap[t] = { status: "Pending ⏳", time: "—" };
  });

  if (ss) {
    var sheet = ss.getSheetByName(dateStr);
    if (sheet && sheet.getLastRow() > 1) {
      var data = sheet.getDataRange().getValues();
      for (var i = 1; i < data.length; i++) {
        var teacherName = data[i][1];
        if (statusMap[teacherName]) {
          var timeVal = data[i][0];
          var timeStr = "—";
          try {
            if (timeVal instanceof Date) {
              timeStr = Utilities.formatDate(timeVal, tz, "hh:mm a");
            } else if (timeVal) {
              var parsedDate = new Date(timeVal);
              timeStr = isNaN(parsedDate.getTime()) ? String(timeVal) : Utilities.formatDate(parsedDate, tz, "hh:mm a");
            }
          } catch(e) {}

          statusMap[teacherName] = {
            status: "Submitted ✔️",
            time: timeStr
          };
        }
      }
    }
  }

  var recordList = allTeachers.map(function(t) {
    return {
      name: t,
      status: statusMap[t].status,
      time: statusMap[t].time
    };
  });

  return {
    records: recordList,
    isLocked: isLocked,
    serverTime: Utilities.formatDate(today, tz, "hh:mm:ss a"),
    currentHour: currentHour
  };
}

/**
 * =====================================================================
 * FORM SUBMISSION PROCESSING ENGINE
 * =====================================================================
 */
function processForm(formObject) {
  if (!formObject) return "ERROR: No form data received";

  var tz = getSystemTimeZone();
  var today = new Date();

  // 1. Timezone-Accurate Window Lock Enforcement
  var hourStr = Utilities.formatDate(today, tz, "HH");
  var currentHour = parseInt(hourStr, 10);
  if (currentHour < 12 || currentHour >= 20) {
    return "REJECTED: Submission Window Closed! (Active strictly 12:00 PM – 08:00 PM IST)";
  }

  // Normalize form properties
  var username = (formObject.username || "").trim();
  var userPin = (formObject.userPin || "").trim();
  var reportDate = (formObject.reportDate || "").trim();

  if (!username) return "REJECTED: Employee Name is required!";

  // 2. PIN Verification
  var pins = getTeachersPinRegistry();
  if (pins[username] && userPin !== String(pins[username]).trim()) {
    return "REJECTED: Verification PIN Mismatch! Access Denied.";
  }

  // Concurrency Lock for Sheet Write
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(12000);
  } catch (e) {
    return "ERROR: Server busy, please retry in 5 seconds.";
  }

  try {
    var ss = getTargetSpreadsheet();
    if (!ss) return "ERROR: Google Spreadsheet connection missing.";

    var sheetName = Utilities.formatDate(today, tz, "dd-MMM-yyyy");
    var sheet = ss.getSheetByName(sheetName) || ss.insertSheet(sheetName);

    // Header initialization
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Timestamp", "Name", "Date",
        "FB L", "FB C", "FB S",
        "IG L", "IG C", "IG S",
        "YT L", "YT C", "YT S"
      ]);
      sheet.getRange(1, 1, 1, 12)
        .setFontWeight("bold")
        .setBackground("#059669")
        .setFontColor("#ffffff");
    }

    // 3. Duplicate Prevention
    var data = sheet.getDataRange().getValues();
    for (var i = 1; i < data.length; i++) {
      if (String(data[i][1]).trim() === username) {
        return "DUPLICATE: Your submission data for today has already been logged into the registry!";
      }
    }

    // 4. Batch Record Write
    var timeStampFormatted = Utilities.formatDate(today, tz, "dd-MMM-yyyy hh:mm:ss a");
    sheet.appendRow([
      timeStampFormatted,
      username,
      reportDate || Utilities.formatDate(today, tz, "yyyy-MM-dd"),
      formObject.fbLikes || "NO",
      formObject.fbComments || "NO",
      formObject.fbShares || "NO",
      formObject.igLikes || "NO",
      formObject.igComments || "NO",
      formObject.igShares || "NO",
      formObject.ytLikes || "NO",
      formObject.ytComments || "NO",
      formObject.ytShares || "NO"
    ]);

    return "SUCCESS";
  } catch (err) {
    Logger.log("processForm error: " + err.message);
    return "ERROR: " + err.message;
  } finally {
    try { lock.releaseLock(); } catch(e) {}
  }
}

/**
 * =====================================================================
 * HISTORICAL DASHBOARD & AUDIT COMPLIANCE
 * =====================================================================
 */
function fetchHistoricalDashboardData(targetDateStr) {
  var ss = getTargetSpreadsheet();
  var tz = getSystemTimeZone();
  var registry = getTeachersPinRegistry();
  var allTeachers = Object.keys(registry).sort();
  var dataMap = {};

  allTeachers.forEach(function(teacher) {
    dataMap[teacher] = {
      submitted: false,
      time: "—",
      fb: { l: "—", c: "—", s: "—" },
      ig: { l: "—", c: "—", s: "—" },
      yt: { l: "—", c: "—", s: "—" }
    };
  });

  if (ss && targetDateStr) {
    var parsedDate = new Date(targetDateStr);
    var sheetName = Utilities.formatDate(parsedDate, tz, "dd-MMM-yyyy");
    var sheet = ss.getSheetByName(sheetName);

    if (sheet && sheet.getLastRow() > 1) {
      var data = sheet.getDataRange().getValues();
      for (var i = 1; i < data.length; i++) {
        var name = String(data[i][1]).trim();
        if (dataMap[name]) {
          var timeVal = data[i][0];
          var timeStr = "—";
          try {
            if (timeVal instanceof Date) {
              timeStr = Utilities.formatDate(timeVal, tz, "hh:mm a");
            } else if (timeVal) {
              var pD = new Date(timeVal);
              timeStr = isNaN(pD.getTime()) ? String(timeVal) : Utilities.formatDate(pD, tz, "hh:mm a");
            }
          } catch(e) {}

          dataMap[name] = {
            submitted: true,
            time: timeStr,
            fb: { l: String(data[i][3]), c: String(data[i][4]), s: String(data[i][5]) },
            ig: { l: String(data[i][6]), c: String(data[i][7]), s: String(data[i][8]) },
            yt: { l: String(data[i][9]), c: String(data[i][10]), s: String(data[i][11]) }
          };
        }
      }
    }
  }

  return allTeachers.map(function(teacher) {
    return {
      name: teacher,
      submitted: dataMap[teacher].submitted,
      time: dataMap[teacher].time,
      fb: dataMap[teacher].fb,
      ig: dataMap[teacher].ig,
      yt: dataMap[teacher].yt
    };
  });
}

function fetchReportBySingleDate(targetDateStr) {
  var extractedData = [
    ["Target Date", "Submission Time", "Employee Name", "Status", "FB Like", "FB Comment", "FB Share", "IG Like", "IG Comment", "IG Share", "YT Like", "YT Comment", "YT Share"]
  ];

  var dashboardData = fetchHistoricalDashboardData(targetDateStr);
  dashboardData.forEach(function(row) {
    var statusText = row.submitted ? "Submitted" : "Not Submitted";
    var rowData = [
      targetDateStr, row.time, row.name, statusText,
      row.fb.l, row.fb.c, row.fb.s,
      row.ig.l, row.ig.c, row.ig.s,
      row.yt.l, row.yt.c, row.yt.s
    ];
    extractedData.push(rowData);
  });
  return extractedData;
}

/**
 * JSON Response Formatter for API endpoints
 */
function createJsonResponse(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}

function handleApiGet(e) {
  var action = e.parameter.action;
  if (action === "getRegistry") {
    return createJsonResponse(getTeachersPinRegistry());
  }
  if (action === "liveStatus") {
    return createJsonResponse(getLiveAttendanceStatus());
  }
  if (action === "historical" && e.parameter.date) {
    return createJsonResponse(fetchHistoricalDashboardData(e.parameter.date));
  }
  return createJsonResponse({ error: "Unknown action" });
}
