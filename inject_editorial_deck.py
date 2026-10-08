import re

html_path = r"c:\test\badminton.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Google Fonts in <head> to include Syne, Unbounded, Plus Jakarta Sans, Space Grotesk
font_link_old = r'<link href="https://fonts.googleapis.com/css2\?[^"]+" rel="stylesheet">'
font_link_new = '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700;1,800&family=Space+Grotesk:wght@400;500;600;700&family=Syne:wght@600;700;800;900&family=Unbounded:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">'

html = re.sub(font_link_old, font_link_new, html, count=1)

# 2. Add New Editorial Aura Typography CSS Rules to :root and style block
editorial_css = """
    /* =========================================================================
       EDITORIAL NEON-LIME AURA & GEOMETRIC TYPOGRAPHY SYSTEM (FIGMA DECK STYLE)
       ========================================================================= */
    :root {
      --font-syne: 'Syne', -apple-system, sans-serif;
      --font-unbounded: 'Unbounded', sans-serif;
      --font-editorial: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-tech-mono: 'Space Grotesk', monospace;
      --neon-lime: #a3e635;
      --neon-lime-glow: rgba(163, 230, 53, 0.85);
      --neon-lime-diffuse: rgba(163, 230, 53, 0.45);
      --neon-emerald: #10b981;
      --obsidian-dark: #050c08;
      --obsidian-card: #08140d;
    }

    /* Deck Container */
    .figma-deck-container {
      max-width: 980px;
      margin: 0 auto 40px;
      display: flex;
      flex-direction: column;
      gap: 32px;
      position: relative;
      z-index: 10;
    }

    /* Master Slide Card */
    .deck-slide-card {
      position: relative;
      width: 100%;
      min-height: 480px;
      border-radius: 36px;
      background-color: var(--obsidian-dark);
      border: 1.5px solid rgba(163, 230, 53, 0.28);
      overflow: hidden;
      padding: clamp(32px, 5vw, 48px);
      box-shadow: 0 35px 80px -15px rgba(0, 0, 0, 0.9), 0 0 60px rgba(163, 230, 53, 0.16);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .deck-slide-card:hover {
      border-color: rgba(163, 230, 53, 0.6);
      box-shadow: 0 40px 90px -10px rgba(0, 0, 0, 0.95), 0 0 80px rgba(163, 230, 53, 0.28);
    }

    /* Dynamic Radiant Ambient Backlights */
    .deck-slide-card.slide-1-bg {
      background: radial-gradient(circle at 48% 45%, rgba(163, 230, 53, 0.42) 0%, rgba(34, 197, 94, 0.2) 32%, rgba(5, 12, 8, 0.98) 72%);
    }

    .deck-slide-card.slide-2-bg {
      background: radial-gradient(circle at 75% 50%, rgba(163, 230, 53, 0.48) 0%, rgba(16, 185, 129, 0.2) 35%, rgba(5, 12, 8, 0.98) 75%);
    }

    /* 4-Corner Micro-Metadata Tags */
    .deck-corner-meta {
      position: absolute;
      font-family: var(--font-tech-mono);
      font-size: 13px;
      font-weight: 600;
      color: rgba(255, 255, 255, 0.65);
      letter-spacing: 0.02em;
      z-index: 15;
      user-select: none;
      transition: color 0.2s ease;
    }

    .deck-corner-meta:hover {
      color: var(--neon-lime);
    }

    .deck-corner-tl { top: 28px; left: 34px; }
    .deck-corner-tr { top: 28px; right: 34px; }
    .deck-corner-bl { bottom: 28px; left: 34px; }
    .deck-corner-br { bottom: 28px; right: 34px; }

    /* Slide 1: Giant Backlit Dark Silhouette Numerals (128) */
    .giant-silhouette-backdrop {
      position: absolute;
      right: -20px;
      top: 50%;
      transform: translateY(-50%);
      width: 680px;
      height: 440px;
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      z-index: 2;
    }

    .giant-silhouette-num {
      font-family: var(--font-syne);
      font-size: clamp(140px, 22vw, 240px);
      font-weight: 900;
      line-height: 0.8;
      letter-spacing: -0.06em;
      color: #060e09;
      -webkit-text-stroke: 2px #a3e635;
      filter: drop-shadow(0 0 28px rgba(163, 230, 53, 0.85)) drop-shadow(0 0 75px rgba(132, 204, 22, 0.5));
      user-select: none;
    }

    /* Slide 2: High Contrast White Numerals + Lightning Geometric Shard */
    .giant-white-stat-num {
      font-family: var(--font-syne);
      font-size: clamp(90px, 14vw, 150px);
      font-weight: 900;
      line-height: 0.88;
      letter-spacing: -0.04em;
      color: #ffffff;
      text-shadow: 0 4px 30px rgba(0, 0, 0, 0.8);
      user-select: none;
      margin-bottom: 12px;
    }

    /* Floating Frosted Glass Chips */
    .deck-floating-chip {
      position: absolute;
      background: rgba(10, 24, 16, 0.65);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.24);
      border-radius: 9999px;
      padding: 8px 20px;
      font-family: var(--font-tech-mono);
      font-size: 13px;
      font-weight: 600;
      color: #ffffff;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.55), 0 0 20px rgba(163, 230, 53, 0.15);
      z-index: 12;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.3s ease;
      cursor: default;
    }

    .deck-floating-chip:hover {
      border-color: var(--neon-lime);
      transform: translateY(-2px) scale(1.03);
      box-shadow: 0 16px 35px rgba(0, 0, 0, 0.7), 0 0 28px rgba(163, 230, 53, 0.35);
    }

    .deck-floating-chip.chip-pos-1 {
      top: 18%;
      left: 38%;
    }

    .deck-floating-chip.chip-pos-2 {
      bottom: 38%;
      right: 18%;
    }

    /* Editorial Headline Typography */
    .deck-editorial-headline {
      font-family: var(--font-editorial);
      font-size: clamp(22px, 3.2vw, 34px);
      font-weight: 600;
      line-height: 1.24;
      color: #ffffff;
      letter-spacing: -0.025em;
      max-width: 420px;
      position: relative;
      z-index: 10;
      margin: auto 0;
    }

    .deck-editorial-headline .highlight-lime {
      color: var(--neon-lime);
      font-weight: 700;
    }

    /* Slide 2 Geometric Radiant Lightning Cutout */
    .deck-lightning-shard {
      position: absolute;
      right: 5%;
      top: 50%;
      transform: translateY(-50%);
      width: clamp(260px, 36vw, 420px);
      height: clamp(260px, 36vw, 420px);
      background: #060e09;
      clip-path: polygon(30% 0%, 100% 0%, 65% 52%, 95% 52%, 25% 100%, 45% 48%, 15% 48%);
      border: 2px solid rgba(163, 230, 53, 0.9);
      filter: drop-shadow(0 0 35px rgba(163, 230, 53, 0.9)) drop-shadow(0 0 80px rgba(101, 163, 13, 0.5));
      z-index: 3;
      pointer-events: none;
      animation: shardPulse 4s ease-in-out infinite alternate;
    }

    @keyframes shardPulse {
      0% { transform: translateY(-50%) rotate(0deg) scale(1); }
      100% { transform: translateY(-50%) rotate(2deg) scale(1.04); }
    }

    /* Bottom Profile / Signature Glass Badge */
    .deck-signature-card {
      max-width: 580px;
      margin: 0 auto;
      background: rgba(6, 18, 12, 0.85);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      border: 1.5px solid rgba(255, 255, 255, 0.2);
      border-radius: 28px;
      padding: 16px 26px;
      display: flex;
      align-items: center;
      gap: 20px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 35px rgba(163, 230, 53, 0.15);
      position: relative;
      z-index: 10;
      transition: all 0.3s ease;
    }

    .deck-signature-card:hover {
      border-color: rgba(163, 230, 53, 0.55);
      transform: translateY(-3px);
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.9), 0 0 50px rgba(163, 230, 53, 0.25);
    }

    .deck-avatar-img {
      width: 60px;
      height: 60px;
      border-radius: 18px;
      object-fit: cover;
      border: 2px solid rgba(163, 230, 53, 0.6);
      box-shadow: 0 0 20px rgba(163, 230, 53, 0.3);
      flex-shrink: 0;
    }

    .deck-signature-content {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    .deck-signature-name {
      font-family: var(--font-tech-mono);
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #ffffff;
    }

    .deck-signature-tags {
      font-size: 12.5px;
      color: #94a3b8;
      font-weight: 500;
      line-height: 1.4;
    }

    .deck-signature-handle {
      font-family: var(--font-tech-mono);
      font-size: 12px;
      color: var(--neon-lime);
      font-weight: 700;
      letter-spacing: 0.02em;
    }

    /* Interactive Deck Mode Switcher Tabs */
    .deck-mode-tabs {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }

    .deck-tab-pill {
      background: rgba(5, 16, 10, 0.85);
      border: 1px solid rgba(163, 230, 53, 0.3);
      color: #cbd5e1;
      padding: 8px 20px;
      border-radius: 9999px;
      font-family: var(--font-tech-mono);
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .deck-tab-pill:hover {
      color: #ffffff;
      border-color: var(--neon-lime);
      background: rgba(163, 230, 53, 0.15);
    }

    .deck-tab-pill.active {
      background: var(--neon-lime);
      color: #030a06;
      border-color: var(--neon-lime);
      box-shadow: 0 0 25px rgba(163, 230, 53, 0.55);
      font-weight: 800;
    }

    @media (max-width: 768px) {
      .deck-slide-card {
        min-height: 420px;
        padding: 64px 22px 54px;
      }
      .giant-silhouette-backdrop {
        right: -60px;
        width: 100%;
        opacity: 0.45;
      }
      .giant-silhouette-num {
        font-size: 140px;
      }
      .deck-floating-chip.chip-pos-1 {
        top: 14%;
        left: 20%;
      }
      .deck-floating-chip.chip-pos-2 {
        bottom: 24%;
        right: 8%;
      }
      .deck-lightning-shard {
        opacity: 0.35;
        right: -20px;
      }
      .deck-corner-tl { top: 18px; left: 20px; }
      .deck-corner-tr { top: 18px; right: 20px; }
      .deck-corner-bl { bottom: 18px; left: 20px; }
      .deck-corner-br { bottom: 18px; right: 20px; }
      .deck-signature-card {
        flex-direction: column;
        text-align: center;
        padding: 20px;
      }
    }
"""

# Insert editorial_css before </style>
if "/* Deck Container */" not in html:
    html = html.replace("</style>", editorial_css + "\n  </style>")

# 3. Create the HTML Presentation Deck component modeled precisely on the user's reference image
deck_html = """
        <!-- =======================================================================
             FIGMA EDITORIAL SLIDE DECK & TYPOGRAPHY SYSTEM (USER REFERENCE STYLE)
             ======================================================================= -->
        <div class="figma-deck-container" id="editorialShowcaseDeck">
          
          <!-- Mode Toggle Tabs (Reference Preview vs Live Tournament Telemetry) -->
          <div class="deck-mode-tabs">
            <button class="deck-tab-pill active" id="btnDeckModeTournament" onclick="switchDeckContent('tournament')">
              <span class="status-dot"></span>
              <span>TOURNAMENT EDITORIAL (2026)</span>
            </button>
            <button class="deck-tab-pill" id="btnDeckModeDesign" onclick="switchDeckContent('design')">
              <i data-lucide="sparkles" style="width: 14px; height: 14px;"></i>
              <span>ORIGINAL REFERENCE EXACT COPY</span>
            </button>
          </div>

          <!-- SLIDE 1: GIANT 128 / 10 DUOS BACKLIT SILHOUETTE CARD -->
          <div class="deck-slide-card slide-1-bg" id="slideCard1">
            <!-- 4 Corners -->
            <div class="deck-corner-meta deck-corner-tl" id="s1MetaTL">slide</div>
            <div class="deck-corner-meta deck-corner-tr" id="s1MetaTR">figma</div>
            <div class="deck-corner-meta deck-corner-bl" id="s1MetaBL">@pollytlg</div>
            <div class="deck-corner-meta deck-corner-br" id="s1MetaBR">graphic design</div>

            <!-- Giant Backlit Silhouette Number -->
            <div class="giant-silhouette-backdrop">
              <div class="giant-silhouette-num" id="s1GiantNum">128</div>
            </div>

            <!-- Floating Glass Chips -->
            <div class="deck-floating-chip chip-pos-1" id="s1Chip1">
              <span class="status-dot"></span>
              <span id="s1Chip1Text">2000 year (12s)</span>
            </div>
            <div class="deck-floating-chip chip-pos-2" id="s1Chip2">
              <span class="status-dot" style="background-color: var(--neon-lime);"></span>
              <span id="s1Chip2Text">2025 year (8s)</span>
            </div>

            <!-- Left Editorial Subhead -->
            <div class="deck-editorial-headline" id="s1Headline">
              The average<br>
              attecntion span<br>
              of a consumer
            </div>
          </div>

          <!-- SLIDE 2: 72% / 8 PM CRISP WHITE DISPLAY & GEOMETRIC LIGHTNING CUTOUT -->
          <div class="deck-slide-card slide-2-bg" id="slideCard2">
            <!-- 4 Corners -->
            <div class="deck-corner-meta deck-corner-tl" id="s2MetaTL">slide #11</div>
            <div class="deck-corner-meta deck-corner-tr" id="s2MetaTR">figma</div>
            <div class="deck-corner-meta deck-corner-bl" id="s2MetaBL">@pollytlg</div>
            <div class="deck-corner-meta deck-corner-br" id="s2MetaBR">graphic design</div>

            <!-- Geometric Lightning Shard Graphic -->
            <div class="deck-lightning-shard"></div>

            <!-- Left White Numerals & Editorial Subhead -->
            <div style="position: relative; z-index: 10; margin: auto 0; max-width: 480px;">
              <div class="giant-white-stat-num" id="s2GiantNum">72%</div>
              <div class="deck-editorial-headline" id="s2Headline" style="max-width: 400px;">
                of people say that they get their best ideas in the shower
              </div>
            </div>
          </div>

          <!-- SIGNATURE GLASS BADGE (BOTTOM PROFILE) -->
          <div class="deck-signature-card" id="deckSignatureCard">
            <img src="assets/custom_player_1.jpg" alt="Author Avatar" class="deck-avatar-img" id="deckAvatarImg" onerror="this.src='assets/clean_round_logo.png'">
            <div class="deck-signature-content">
              <div class="deck-signature-name" id="deckAuthorName">КАВЕРЗНЕВА ПОЛИНА</div>
              <div class="deck-signature-tags" id="deckAuthorTags">web, mobile, лендинги, презентации, фирменный стиль</div>
              <div class="deck-signature-handle" id="deckAuthorHandle">телеграм: @pollytlg</div>
            </div>
          </div>

        </div>
"""

# Inject deck_html at the start of Page 1 (inside hero section or hero stage)
if 'id="editorialShowcaseDeck"' not in html:
    html = html.replace('<div class="hero-glass-stage">', '<div class="hero-glass-stage">\n' + deck_html)

# Add deck interaction script before </body>
deck_js = """
    // =========================================================================
    // EDITORIAL SLIDE DECK INTERACTION & CONTENT TOGGLE
    // =========================================================================
    let currentDeckContent = 'tournament';

    function switchDeckContent(mode) {
      currentDeckContent = mode;
      const btnTourn = document.getElementById('btnDeckModeTournament');
      const btnDesign = document.getElementById('btnDeckModeDesign');

      const s1TL = document.getElementById('s1MetaTL');
      const s1TR = document.getElementById('s1MetaTR');
      const s1BL = document.getElementById('s1MetaBL');
      const s1BR = document.getElementById('s1MetaBR');
      const s1Num = document.getElementById('s1GiantNum');
      const s1Chip1Text = document.getElementById('s1Chip1Text');
      const s1Chip2Text = document.getElementById('s1Chip2Text');
      const s1Headline = document.getElementById('s1Headline');

      const s2TL = document.getElementById('s2MetaTL');
      const s2TR = document.getElementById('s2MetaTR');
      const s2BL = document.getElementById('s2MetaBL');
      const s2BR = document.getElementById('s2MetaBR');
      const s2Num = document.getElementById('s2GiantNum');
      const s2Headline = document.getElementById('s2Headline');

      const authorName = document.getElementById('deckAuthorName');
      const authorTags = document.getElementById('deckAuthorTags');
      const authorHandle = document.getElementById('deckAuthorHandle');

      if (mode === 'design') {
        if (btnTourn) btnTourn.classList.remove('active');
        if (btnDesign) btnDesign.classList.add('active');

        // Exact Copy from User Reference Image
        if (s1TL) s1TL.innerText = 'slide';
        if (s1TR) s1TR.innerText = 'figma';
        if (s1BL) s1BL.innerText = '@pollytlg';
        if (s1BR) s1BR.innerText = 'graphic design';
        if (s1Num) s1Num.innerText = '128';
        if (s1Chip1Text) s1Chip1Text.innerText = '2000 year (12s)';
        if (s1Chip2Text) s1Chip2Text.innerText = '2025 year (8s)';
        if (s1Headline) s1Headline.innerHTML = 'The average<br>attecntion span<br>of a consumer';

        if (s2TL) s2TL.innerText = 'slide #11';
        if (s2TR) s2TR.innerText = 'figma';
        if (s2BL) s2BL.innerText = '@pollytlg';
        if (s2BR) s2BR.innerText = 'graphic design';
        if (s2Num) s2Num.innerText = '72%';
        if (s2Headline) s2Headline.innerHTML = 'of people say that they get their best ideas in the shower';

        if (authorName) authorName.innerText = 'КАВЕРЗНЕВА ПОЛИНА';
        if (authorTags) authorTags.innerText = 'web, mobile, лендинги, презентации, фирменный стиль';
        if (authorHandle) authorHandle.innerText = 'телеграм: @pollytlg';
      } else {
        if (btnTourn) btnTourn.classList.add('active');
        if (btnDesign) btnDesign.classList.remove('active');

        // Tournament Synchronized Telemetry Mode
        if (s1TL) s1TL.innerText = 'slide #01';
        if (s1TR) s1TR.innerText = 'suryodaya portal';
        if (s1BL) s1BL.innerText = '@suryodaya.badminton';
        if (s1BR) s1BR.innerText = 'men\'s doubles 2026';
        if (s1Num) s1Num.innerText = '10';
        if (s1Chip1Text) s1Chip1Text.innerText = '10 Confirmed Duos (20 Players)';
        if (s1Chip2Text) s1Chip2Text.innerText = 'Live Draw @ 9:00 PM Tonight';
        if (s1Headline) s1Headline.innerHTML = 'The official<br><span class="highlight-lime">badminton championship</span><br>of Suryodaya Park';

        if (s2TL) s2TL.innerText = 'slide #02';
        if (s2TR) s2TR.innerText = 'matchday fixture';
        if (s2BL) s2BL.innerText = '@suryodaya.badminton';
        if (s2BR) s2BR.innerText = 'prime evening clashes';
        if (s2Num) s2Num.innerText = '8 PM';
        if (s2Headline) s2Headline.innerHTML = 'of resident players vote for weekend floodlit clashes over standard weekdays';

        if (authorName) authorName.innerText = 'SURYODAYA BADMINTON COMMITTEE';
        if (authorTags) authorTags.innerText = 'Official Draws • Dynamic Knockout Trees • Court 1 & 2 Live Fixtures';
        if (authorHandle) authorHandle.innerText = 'portal: http://localhost:3000';
      }
      if (window.lucide) lucide.createIcons();
    }
"""

if "switchDeckContent" not in html:
    html = html.replace("</script>\n</body>", deck_js + "\n  </script>\n</body>")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully injected Editorial Slide Deck and Aura Typography into badminton.html")
