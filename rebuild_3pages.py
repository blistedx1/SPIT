import re

html_path = r"c:\test\badminton.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect where header begins and ends
header_and_body_pattern = re.compile(r'(<header class="site-header">.*?</header>\s*<div class="container">)(.*?)(<!-- Official Tournament Draw Announcement Modal -->)', re.DOTALL)

new_body = """    <!-- Story Progress Bar (3 Pages / Screens - Instagram / TikTok Story Aesthetic) -->
    <div class="story-progress-container" id="storyProgressNav">
      <div class="story-progress-bars">
        <div class="story-bar-segment active" id="storySegment1" onclick="goToStoryPage(1)" title="Page 1: Intro & Hero"></div>
        <div class="story-bar-segment" id="storySegment2" onclick="goToStoryPage(2)" title="Page 2: Live Timers"></div>
        <div class="story-bar-segment" id="storySegment3" onclick="goToStoryPage(3)" title="Page 3: Squad & Brackets"></div>
      </div>
      <div class="story-nav-labels">
        <div class="story-nav-label-item active" id="storyLabel1" onclick="goToStoryPage(1)">
          <span class="status-dot"></span>
          <span>01. Intro & Hero</span>
        </div>
        <div class="story-nav-label-item" id="storyLabel2" onclick="goToStoryPage(2)">
          <i data-lucide="clock" style="width: 14px; height: 14px;"></i>
          <span>02. Live Timers</span>
        </div>
        <div class="story-nav-label-item" id="storyLabel3" onclick="goToStoryPage(3)">
          <i data-lucide="trophy" style="width: 14px; height: 14px;"></i>
          <span>03. Squad & Brackets</span>
        </div>
      </div>
    </div>

    <!-- Multi-Screen Pages Wrapper -->
    <div class="app-screens-wrapper">

      <!-- =======================================================================
           PAGE 1: INTRO & HERO PAGE
           ======================================================================= -->
      <section class="app-screen-page active-page" id="screenPage1">
        <main class="hero-section" id="overview">
          <div class="hero-glass-stage">
            
            <!-- Tournament Badge Eyebrow -->
            <div class="hero-eyebrow-pill">
              <span class="status-dot"></span>
              <span>Suryodaya Park Men's Doubles Championship 2026</span>
            </div>

            <!-- 1. TOURNAMENT SIGN / NAME (Luxury Editorial Serif + Coral Dot) -->
            <div class="hero-sign-container">
              <h1 class="hero-grand-sign">
                <span class="hero-sign-title">Suryodaya</span>
                <span class="hero-sign-flourish">Badminton<span class="coral-dot"></span></span>
              </h1>
              <div class="hero-editorial-sub">
                <span>F O R &nbsp; R E S I D E N T S &nbsp; • &nbsp; M E N ' S &nbsp; D O U B L E S &nbsp; • &nbsp; 2 0 2 6</span>
              </div>
            </div>

            <!-- 2. MOTTO (Glassmorphic Quote Showcase) -->
            <div class="hero-motto-glasscard">
              <div class="motto-quote-mark">“</div>
              <p class="hero-motto-text">
                Weekday ki thakan bhulao, puraane yaaron ke saath court par utro.<br>
                <span class="motto-highlight">Sirf ek game nahi, poora weekend blast hai!</span>
              </p>
              <div class="motto-meta-badge">
                <span class="status-dot"></span>
                <span>10 Confirmed Duos Locked • Weekend Blast Edition</span>
              </div>
            </div>

            <!-- 3. ENTER NEXT PAGE BUTTON -->
            <div class="hero-enter-container" style="display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; align-items: center;">
              <button class="btn-enter-website" onclick="goToStoryPage(2)" style="background: none; border: none; cursor: pointer;">
                <span class="btn-enter-label">PAGE 2: VIEW TIMERS</span>
                <div class="btn-enter-arrow">
                  <i data-lucide="arrow-right" style="width: 24px; height: 24px;"></i>
                </div>
              </button>
            </div>

          </div>
        </main>
      </section>

      <!-- =======================================================================
           PAGE 2: DEDICATED LIVE TIMERS & DRAW ANNOUNCEMENT PAGE
           ======================================================================= -->
      <section class="app-screen-page" id="screenPage2">
        <div class="timer-page-stage">
          
          <div class="section-eyebrow" style="margin-bottom: 30px;">
            <div class="badge-pill">
              <span class="status-dot"></span>
              <span>Official Tournament Clocks</span>
            </div>
            <h2 class="section-title">Live Match Fixtures & Kickoff Timers</h2>
            <p class="section-desc">
              Synchronized real-time countdown for today's lottery chit draw and the grand opening weekend tournament kickoff.
            </p>
          </div>

          <!-- Master Timer Card 1: 9:00 PM IST DRAW NOTICE (LOTTERY CHIT SYSTEM) -->
          <div class="timer-master-card gold-border" id="drawSectionCard">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 18px;">
              <div class="draw-banner-badge" style="margin-bottom: 0;">
                <span class="status-dot"></span>
                <span>CRITICAL NOTICE • TODAY AT 9:00 PM IST</span>
              </div>
              <div style="font-family: var(--font-mono); font-size: 12px; color: var(--accent-gold); font-weight: 700;">
                OPEN LOTTERY CHIT SYSTEM
              </div>
            </div>

            <h3 class="draw-banner-heading" style="text-align: left; margin-bottom: 12px;">
              Official Match Fixtures & Seeding Draw
            </h3>

            <!-- English Notice -->
            <p style="font-size: 16px; color: #f1f5f9; line-height: 1.6; margin-bottom: 14px; font-weight: 500;">
              The official match fixtures and pool allocations for all 10 registered doubles pairs will be drawn live via an open lottery chit system <strong>today at 9:00 PM IST</strong>. All resident players are warmly requested to be present.
            </p>

            <!-- Hindi Notice -->
            <div style="font-size: 15px; font-weight: 600; color: var(--accent-mint); line-height: 1.6; border-top: 1px dashed rgba(52, 211, 153, 0.35); padding-top: 14px; margin-bottom: 24px;">
              टूर्नामेंट का आधिकारिक मैच ड्रॉ (लॉटरी चिट पद्धति द्वारा) आज सायं 9:00 बजे निकाला जाएगा। सभी सम्मानित प्रतिभागियों एवं खिलाड़ियों की उपस्थिति सादर प्रार्थनीय है।
            </div>

            <!-- Giant 9:00 PM Clock -->
            <div class="giant-clock-display gold-accent">
              <div class="draw-box-title" style="color: var(--accent-gold);">
                <i data-lucide="clock" style="width: 18px; height: 18px;"></i>
                <span>COUNTDOWN TO 9:00 PM IST DRAW TODAY</span>
              </div>
              <div class="giant-clock-digits">
                <div class="giant-clock-unit">
                  <div class="giant-clock-val gold" id="drawBannerHours">00</div>
                  <div class="giant-clock-label">Hours</div>
                </div>
                <div class="giant-clock-colon" style="color: var(--accent-gold);">:</div>
                <div class="giant-clock-unit">
                  <div class="giant-clock-val gold" id="drawBannerMins">00</div>
                  <div class="giant-clock-label">Mins</div>
                </div>
                <div class="giant-clock-colon" style="color: var(--accent-gold);">:</div>
                <div class="giant-clock-unit">
                  <div class="giant-clock-val gold" id="drawBannerSecs">00</div>
                  <div class="giant-clock-label">Secs</div>
                </div>
              </div>
              <div style="font-size: 12px; color: #94a3b8; font-family: var(--font-mono);">
                Location: Suryodaya Park Clubhouse & Pavilion Arena
              </div>
            </div>
          </div>

          <!-- Master Timer Card 2: TOURNAMENT OPENING KICKOFF -->
          <div class="timer-master-card">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 18px;">
              <div class="badge-pill">
                <span class="status-dot"></span>
                <span>Grand Kickoff</span>
              </div>
              <div style="font-family: var(--font-mono); font-size: 12px; color: var(--accent-mint); font-weight: 700;">
                24 OCTOBER 2026 • 6:30 PM
              </div>
            </div>

            <div class="timer-hero-grid">
              <div>
                <h3 style="font-family: var(--font-serif); font-size: 28px; font-weight: 800; color: #ffffff; margin-bottom: 12px;">
                  Championship Opening Rallies
                </h3>
                <p style="color: #94a3b8; font-size: 14.5px; line-height: 1.6; margin-bottom: 20px;">
                  32 resident players, 10 confirmed pairs, high-tempo 21-point feather shuttle clashes under professional stadium floodlights.
                </p>
                <div style="display: flex; flex-direction: column; gap: 10px;">
                  <div style="display: flex; align-items: center; gap: 10px; font-size: 13.5px; color: #cbd5e1;">
                    <i data-lucide="map-pin" style="color: var(--accent-mint); width: 16px; height: 16px;"></i>
                    <span>Suryodaya Park Indoor Pavilion, Court 1 & 2</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 10px; font-size: 13.5px; color: #cbd5e1;">
                    <i data-lucide="calendar" style="color: var(--accent-mint); width: 16px; height: 16px;"></i>
                    <span>Friday to Sunday Evening Sessions (6:30 PM - 10:30 PM)</span>
                  </div>
                </div>
              </div>

              <!-- Giant Kickoff Clock -->
              <div class="giant-clock-display">
                <div class="draw-box-title">
                  <i data-lucide="zap" style="width: 16px; height: 16px;"></i>
                  <span>TOURNAMENT COMMENCEMENT TIMER</span>
                </div>
                <div class="giant-clock-digits">
                  <div class="giant-clock-unit">
                    <div class="giant-clock-val" id="daysVal">21</div>
                    <div class="giant-clock-label">Days</div>
                  </div>
                  <div class="giant-clock-colon">:</div>
                  <div class="giant-clock-unit">
                    <div class="giant-clock-val" id="hoursVal">09</div>
                    <div class="giant-clock-label">Hours</div>
                  </div>
                  <div class="giant-clock-colon">:</div>
                  <div class="giant-clock-unit">
                    <div class="giant-clock-val" id="minVal">42</div>
                    <div class="giant-clock-label">Mins</div>
                  </div>
                  <div class="giant-clock-colon">:</div>
                  <div class="giant-clock-unit">
                    <div class="giant-clock-val" id="secVal">15</div>
                    <div class="giant-clock-label">Secs</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Page 2 Navigation Action Buttons -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 32px; border-top: 1px solid rgba(52, 211, 153, 0.2); padding-top: 24px; flex-wrap: wrap; gap: 14px;">
              <button class="action-btn-sm" onclick="goToStoryPage(1)" style="padding: 10px 20px; font-size: 13.5px;">
                <i data-lucide="arrow-left" style="width: 16px; height: 16px;"></i>
                <span>← Back to Intro</span>
              </button>
              <button class="action-btn-sm primary" onclick="goToStoryPage(3)" style="padding: 12px 24px; font-size: 14px; border-radius: 999px;">
                <span>Page 3: View 10 Duos & Brackets</span>
                <i data-lucide="arrow-right" style="width: 16px; height: 16px; margin-left: 6px;"></i>
              </button>
            </div>
          </div>

        </div>
      </section>

      <!-- =======================================================================
           PAGE 3: TOURNAMENT ARENA, 10 TEAMS, LEAGUE POOLS & BRACKETS
           ======================================================================= -->
      <section class="app-screen-page" id="screenPage3">
        
        <!-- Men's Doubles Structure Section -->
        <div class="division-section" id="doubles-league" style="padding-top: 10px; border-top: none;">
          <div class="section-eyebrow">
            <div class="badge-pill">
              <span class="status-dot"></span>
              <span>10 Confirmed Duos Locked</span>
            </div>
            <h2 class="section-title">Men's Doubles Championship Arena</h2>
            <p class="section-desc">
              Strictly Men's Doubles. 10 curated resident pairs competing in high-tempo group stages followed by direct knockouts for the Suryodaya Doubles Trophy.
            </p>
          </div>

          <div class="division-grid">
            <!-- Card 1 -->
            <div class="doubles-feature-card">
              <div class="category-icon">
                <i data-lucide="users"></i>
              </div>
              <h3>10 Confirmed Duos</h3>
              <p>Registration locked with 10 verified resident pairs (20 players) to ensure prime evening court availability and proper rest intervals.</p>
              <div class="card-footer-meta">
                <span>PAIR SLOTS</span>
                <span class="slots">10 / 10 LOCKED</span>
              </div>
            </div>

            <!-- Card 2 -->
            <div class="doubles-feature-card">
              <div class="category-icon">
                <i data-lucide="git-branch"></i>
              </div>
              <h3>Group Stages to Knockouts</h3>
              <p>2 Groups of 5 pairs (Pool A & Pool B). Top 2 pairs from each pool advance directly to the Semifinals and Grand Championship Final.</p>
              <div class="card-footer-meta">
                <span>FORMAT</span>
                <span class="slots">ROUND ROBIN + KO</span>
              </div>
            </div>

            <!-- Card 3 -->
            <div class="doubles-feature-card">
              <div class="category-icon">
                <i data-lucide="zap"></i>
              </div>
              <h3>Doubles Court Geometry</h3>
              <p>Full wide sidelines active for rallies. Strict BWF doubles service bounds (short service line to back doubles service boundary line).</p>
              <div class="card-footer-meta">
                <span>COURT SPECS</span>
                <span class="slots">WIDE SIDELINES</span>
              </div>
            </div>

            <!-- Card 4 -->
            <div class="doubles-feature-card">
              <div class="category-icon">
                <i data-lucide="trophy"></i>
              </div>
              <h3>Championship Honors</h3>
              <p>Pair trophies, custom gold engraved doubles medallions, and the eternal Suryodaya Park Doubles Champion plaque display in the clubhouse.</p>
              <div class="card-footer-meta">
                <span>AWARDS</span>
                <span class="slots">DUO TROPHIES</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Official Squad, Dynamic Brackets & League Section -->
        <div class="squad-section" id="squad-brackets" style="padding-top: 30px; border-top: none;">
          <!-- Main Tournament Container -->
          <div class="tournament-panel">
            <!-- Top Toolbar & Controls -->
            <div class="bracket-toolbar">
              <div class="bracket-toolbar-left">
                <!-- View Tabs -->
                <div class="bracket-tabs">
                  <button class="bracket-tab-btn active" id="tabBtnKnockout" onclick="switchBracketTab('knockout')">
                    <i data-lucide="git-branch" style="width: 15px; height: 15px;"></i>
                    <span>Knockout Tree</span>
                  </button>
                  <button class="bracket-tab-btn" id="tabBtnLeague" onclick="switchBracketTab('league')">
                    <i data-lucide="layout-grid" style="width: 15px; height: 15px;"></i>
                    <span>League Pools</span>
                  </button>
                  <button class="bracket-tab-btn" id="tabBtnRoster" onclick="switchBracketTab('roster')">
                    <i data-lucide="users" style="width: 15px; height: 15px;"></i>
                    <span>Manage Teams (<span id="tabTeamsCount">10</span>)</span>
                  </button>
                </div>
              </div>

              <div class="bracket-toolbar-right">
                <button class="action-btn-sm" onclick="shuffleTournamentSeeds()" title="Randomize Seeds & Bracket Draw">
                  <i data-lucide="shuffle" style="width: 14px; height: 14px;"></i>
                  <span>Shuffle Draw</span>
                </button>
                <button class="action-btn-sm" onclick="autoSimulateBracket()" title="Auto Simulate Match Outcomes">
                  <i data-lucide="play-circle" style="width: 14px; height: 14px;"></i>
                  <span>Auto Simulate</span>
                </button>
                <button class="action-btn-sm" onclick="resetTournamentBracket()" title="Reset Bracket Progression">
                  <i data-lucide="rotate-ccw" style="width: 14px; height: 14px;"></i>
                  <span>Reset</span>
                </button>
              </div>
            </div>

            <!-- TAB 1: KNOCKOUT BRACKET TREE -->
            <div id="bracketViewKnockout">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; flex-wrap: wrap; gap: 10px;">
                <div style="font-size: 13px; color: var(--text-dim); display: flex; align-items: center; gap: 8px;">
                  <i data-lucide="mouse-pointer-click" style="width: 14px; height: 14px; color: var(--accent-mint);"></i>
                  <span>Click on any team in a matchup to advance them as the winner to the next round!</span>
                </div>
                <div id="bracketMetaNotice" style="font-size: 12px; font-weight: 700; color: var(--accent-mint); background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(52, 211, 153, 0.3); padding: 4px 12px; border-radius: 8px; font-family: var(--font-mono);">
                  10 Teams • 16-Draw Bracket (6 Byes)
                </div>
              </div>

              <!-- Dynamic Round Filter View (Scroll & Round Navigation) -->
              <div class="round-filter-bar" id="roundFilterBar"></div>

              <!-- Horizontal Scroll Navigation Hint & Controls -->
              <div class="bracket-scroll-nav-bar">
                <div class="mobile-scroll-hint">
                  <i data-lucide="chevrons-left-right" style="width: 14px; height: 14px;"></i>
                  <span>Swipe horizontally to view all rounds ↔</span>
                </div>
                <div class="bracket-scroll-btns">
                  <button class="bracket-nav-btn" onclick="scrollBracket(-240)" title="Scroll Left">
                    <i data-lucide="chevron-left" style="width: 14px; height: 14px;"></i>
                    <span>Left</span>
                  </button>
                  <button class="bracket-nav-btn" onclick="scrollBracket(240)" title="Scroll Right">
                    <span>Right</span>
                    <i data-lucide="chevron-right" style="width: 14px; height: 14px;"></i>
                  </button>
                </div>
              </div>

              <div class="bracket-tree-wrapper">
                <div class="bracket-tree-flow" id="bracketTreeContainer">
                  <!-- Dynamically populated rounds and matches -->
                </div>
              </div>
            </div>

            <!-- TAB 2: LEAGUE POOLS STAGE -->
            <div id="bracketViewLeague" style="display: none;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px;">
                <div>
                  <h3 style="font-size: 18px; font-weight: 800; color: #ffffff;">Round-Robin League Stage</h3>
                  <p style="font-size: 13px; color: var(--text-muted);">Teams compete within pools. Top 2 pairs from each pool advance to the Knockout Brackets.</p>
                </div>
                <button class="action-btn-sm primary" onclick="seedKnockoutFromLeague()">
                  <i data-lucide="arrow-right-circle" style="width: 15px; height: 15px;"></i>
                  <span>Push Top Qualifiers to Knockout Bracket</span>
                </button>
              </div>
              <div class="league-grid" id="leaguePoolsContainer">
                <!-- Dynamically populated pools and standings -->
              </div>
            </div>

            <!-- TAB 3: MANAGE TEAMS ROSTER -->
            <div id="bracketViewRoster" style="display: none;">
              <!-- Inline Add Team Form -->
              <div class="inline-add-team-bar">
                <div style="font-weight: 800; font-size: 13px; color: #ffffff; margin-right: 8px; display: flex; align-items: center; gap: 6px;">
                  <i data-lucide="plus-circle" style="width: 16px; height: 16px; color: var(--accent-mint);"></i>
                  <span>Add Duo:</span>
                </div>
                <input type="text" id="quickP1" class="inline-input" placeholder="Player 1 Name (e.g. Rahul)">
                <input type="text" id="quickP2" class="inline-input" placeholder="Player 2 Name (e.g. Aman)">
                <button class="action-btn-sm primary" onclick="handleQuickAddTeam()" style="padding: 10px 18px;">
                  <span>+ Add Duo</span>
                </button>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                <div style="font-weight: 800; font-size: 16px; color: #ffffff; font-family: var(--font-serif); letter-spacing: 0.02em;">Confirmed Registered Duos (<span id="rosterCountLabel" style="color: var(--accent-mint);">10</span>)</div>
                <button class="action-btn-sm" onclick="clearAllTeams()" style="color: #f87171; border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.1);">
                  <i data-lucide="trash-2" style="width: 13px; height: 13px;"></i>
                  <span>Clear All</span>
                </button>
              </div>

              <div class="roster-grid" id="rosterListContainer">
                <!-- Dynamically populated team cards -->
              </div>
            </div>
          </div>
        </div>

        <!-- Tournament Details & Rules Grid -->
        <div class="division-section" id="doubles-rules" style="padding-top: 30px; border-top: none;">
          <div class="timer-master-card" style="border-radius: 32px; padding: clamp(32px, 5vw, 54px);">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px; align-items: center;">
              <div>
                <div class="badge-pill" style="margin-bottom: 20px;">
                  <span class="status-dot"></span>
                  <span>Men's Doubles Regulations</span>
                </div>
                <h3 style="font-family: var(--font-serif); font-size: clamp(26px, 3vw, 36px); font-weight: 800; color: #ffffff; margin-bottom: 16px; line-height: 1.2;">
                  Official Championship <br>
                  <span style="color: var(--accent-mint); font-style: italic;">Guidelines & Rules</span>
                </h3>
                <p style="color: #94a3b8; font-size: 15px; line-height: 1.65; margin-bottom: 24px;">
                  Every team comprises verified resident duos. Matches will be 3 sets of 21 points with feather shuttles, digital line telemetry, and referee monitoring.
                </p>
                <div style="display: flex; gap: 14px; flex-wrap: wrap;">
                  <div class="badge-pill">
                    <i data-lucide="check-circle-2" style="width: 14px; height: 14px; color: var(--accent-mint);"></i>
                    <span>Yonex Aerosensa 50 Feather Shuttles</span>
                  </div>
                  <div class="badge-pill">
                    <i data-lucide="check-circle-2" style="width: 14px; height: 14px; color: var(--accent-mint);"></i>
                    <span>Mandatory Non-Marking Gum Sole Shoes</span>
                  </div>
                </div>
              </div>

              <div style="display: flex; flex-direction: column; gap: 16px;">
                <div style="padding: 18px 22px; background: rgba(4, 30, 20, 0.8); border-radius: 16px; border: 1px solid rgba(52, 211, 153, 0.25); display: flex; gap: 16px; align-items: center;">
                  <i data-lucide="map-pin" style="color: var(--accent-mint); width: 24px; height: 24px; flex-shrink: 0;"></i>
                  <div>
                    <div style="font-weight: 700; font-size: 14.5px; color: #ffffff;">Venue Location</div>
                    <div style="font-size: 13px; color: #94a3b8;">Suryodaya Park Community Hall, Court 1 & 2</div>
                  </div>
                </div>

                <div style="padding: 18px 22px; background: rgba(4, 30, 20, 0.8); border-radius: 16px; border: 1px solid rgba(52, 211, 153, 0.25); display: flex; gap: 16px; align-items: center;">
                  <i data-lucide="clock" style="color: var(--accent-mint); width: 24px; height: 24px; flex-shrink: 0;"></i>
                  <div>
                    <div style="font-weight: 700; font-size: 14.5px; color: #ffffff;">Match Timings</div>
                    <div style="font-size: 13px; color: #94a3b8;">Evening Sessions: 6:30 PM to 10:30 PM IST (Friday - Sunday)</div>
                  </div>
                </div>

                <div style="padding: 18px 22px; background: rgba(4, 30, 20, 0.8); border-radius: 16px; border: 1px solid rgba(52, 211, 153, 0.25); display: flex; gap: 16px; align-items: center;">
                  <i data-lucide="users" style="color: var(--accent-mint); width: 24px; height: 24px; flex-shrink: 0;"></i>
                  <div>
                    <div style="font-weight: 700; font-size: 14.5px; color: #ffffff;">Team Eligibility</div>
                    <div style="font-size: 13px; color: #94a3b8;">Both partners must be resident contenders of Suryodaya Park</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Actions on Page 3 -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 30px 0; flex-wrap: wrap; gap: 14px;">
          <button class="action-btn-sm" onclick="goToStoryPage(2)" style="padding: 10px 20px; font-size: 13.5px;">
            <i data-lucide="arrow-left" style="width: 16px; height: 16px;"></i>
            <span>← Back to Live Timers</span>
          </button>
          <button class="action-btn-sm primary" onclick="goToStoryPage(1)" style="padding: 10px 22px; font-size: 13.5px; border-radius: 999px;">
            <i data-lucide="rotate-ccw" style="width: 15px; height: 15px;"></i>
            <span>Back to Intro / Hero ↺</span>
          </button>
        </div>

      </section>

    </div>

    <!-- Floating Bottom Story Dock (Page Controller) -->
    <div class="story-bottom-dock">
      <button class="dock-btn" onclick="prevStoryPage()" title="Previous Screen (Left Arrow)">
        <i data-lucide="chevron-left" style="width: 16px; height: 16px;"></i>
        <span>Prev</span>
      </button>
      <span class="dock-indicator-text" id="dockPageIndicator">PAGE 1 / 3</span>
      <button class="dock-btn primary" onclick="nextStoryPage()" title="Next Screen (Right Arrow)">
        <span>Next</span>
        <i data-lucide="chevron-right" style="width: 16px; height: 16px;"></i>
      </button>
    </div>

    <!-- Footer -->
    <footer style="padding: 40px 0 100px; border-top: 1px solid rgba(52, 211, 153, 0.2); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
      <div style="font-size: 13px; color: #94a3b8; font-family: var(--font-mono);">
        &copy; 2026 Suryodaya Park Residents Sports Committee. Luxury Men's Doubles Edition.
      </div>
      <div style="display: flex; gap: 20px; font-size: 13px; color: #cbd5e1;">
        <a href="javascript:void(0)" onclick="goToStoryPage(1)" style="color: inherit; text-decoration: none;">01. Intro</a>
        <a href="javascript:void(0)" onclick="goToStoryPage(2)" style="color: inherit; text-decoration: none;">02. Timers</a>
        <a href="javascript:void(0)" onclick="goToStoryPage(3)" style="color: inherit; text-decoration: none;">03. Arena</a>
      </div>
    </footer>
  </div>
"""

# Let's replace the whole main container body
match = header_and_body_pattern.search(content)
if match:
    new_content = content[:match.start(2)] + "\n" + new_body + "\n  " + content[match.start(3):]
    
    # Also add JS handler for 3 story pages
    js_story_code = """
    // =========================================================================
    // 3-PAGE STORY NAVIGATION ENGINE
    // =========================================================================
    let currentStoryPage = 1;
    const totalStoryPages = 3;

    function goToStoryPage(pageNum) {
      if (pageNum < 1) pageNum = 1;
      if (pageNum > totalStoryPages) pageNum = totalStoryPages;
      currentStoryPage = pageNum;

      for (let i = 1; i <= totalStoryPages; i++) {
        const pageEl = document.getElementById('screenPage' + i);
        const segEl = document.getElementById('storySegment' + i);
        const lblEl = document.getElementById('storyLabel' + i);

        if (pageEl) {
          if (i === pageNum) {
            pageEl.classList.add('active-page');
            pageEl.style.display = 'block';
          } else {
            pageEl.classList.remove('active-page');
            pageEl.style.display = 'none';
          }
        }

        if (segEl) {
          if (i === pageNum) {
            segEl.classList.add('active');
          } else {
            segEl.classList.remove('active');
          }
        }

        if (lblEl) {
          if (i === pageNum) {
            lblEl.classList.add('active');
          } else {
            lblEl.classList.remove('active');
          }
        }
      }

      // Update bottom dock indicator
      const dockIndicator = document.getElementById('dockPageIndicator');
      if (dockIndicator) {
        dockIndicator.innerText = `PAGE ${pageNum} / ${totalStoryPages}`;
      }

      // Scroll smoothly to top of active screen
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Refresh icons
      if (window.lucide) lucide.createIcons();
    }

    function nextStoryPage() {
      if (currentStoryPage < totalStoryPages) {
        goToStoryPage(currentStoryPage + 1);
      } else {
        goToStoryPage(1); // loop back
      }
    }

    function prevStoryPage() {
      if (currentStoryPage > 1) {
        goToStoryPage(currentStoryPage - 1);
      } else {
        goToStoryPage(totalStoryPages);
      }
    }

    // Keyboard Arrow navigation (Left/Right arrow keys & 1, 2, 3)
    window.addEventListener('keydown', function(e) {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowRight') {
        nextStoryPage();
      } else if (e.key === 'ArrowLeft') {
        prevStoryPage();
      } else if (e.key === '1') {
        goToStoryPage(1);
      } else if (e.key === '2') {
        goToStoryPage(2);
      } else if (e.key === '3') {
        goToStoryPage(3);
      }
    });

    // Mobile Swipe Gesture Handling
    let touchStartX = 0;
    let touchEndX = 0;

    window.addEventListener('touchstart', function(e) {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    window.addEventListener('touchend', function(e) {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipeGesture();
    }, { passive: true });

    function handleSwipeGesture() {
      const diff = touchEndX - touchStartX;
      if (Math.abs(diff) > 60) {
        if (diff < 0) {
          // Swiped Left -> Go Next
          nextStoryPage();
        } else {
          // Swiped Right -> Go Prev
          prevStoryPage();
        }
      }
    }
    """

    if "goToStoryPage" not in new_content:
        new_content = new_content.replace("</script>\n</body>", js_story_code + "\n</script>\n</body>")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Rebuilt badminton.html with 3-page story system!")
else:
    print("Could not locate header and body pattern in badminton.html")
