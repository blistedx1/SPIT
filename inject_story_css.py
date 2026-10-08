import re

html_path = r"c:\test\badminton.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's add the 3-page story styles and structure
story_css = """
    /* =========================================================================
       3-PAGE / STORY MULTI-SCREEN SYSTEM
       ========================================================================= */
    .story-progress-container {
      position: sticky;
      top: 0;
      left: 0;
      right: 0;
      z-index: 120;
      background: rgba(2, 18, 11, 0.92);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      padding: 12px 24px 10px;
      border-bottom: 1px solid rgba(52, 211, 153, 0.25);
    }

    .story-progress-bars {
      max-width: 960px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .story-bar-segment {
      flex: 1;
      height: 5px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 999px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.3s ease;
    }

    .story-bar-segment.active {
      background: #10b981;
      box-shadow: 0 0 12px #34d399;
    }

    .story-bar-segment.active::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, #34d399, #6ee7b7);
    }

    .story-nav-labels {
      max-width: 960px;
      margin: 8px auto 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #94a3b8;
    }

    .story-nav-label-item {
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 6px;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .story-nav-label-item:hover, .story-nav-label-item.active {
      color: var(--accent-mint);
      background: rgba(16, 185, 129, 0.15);
    }

    /* Screen Pages Wrapper */
    .app-screens-wrapper {
      position: relative;
      width: 100%;
      min-height: calc(100vh - 120px);
    }

    .app-screen-page {
      display: none;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.35s ease, transform 0.35s ease;
      padding: 30px 0 80px;
    }

    .app-screen-page.active-page {
      display: block;
      opacity: 1;
      transform: translateY(0);
    }

    /* Page 2: Dedicated Timer Dashboard */
    .timer-page-stage {
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 32px;
    }

    .timer-master-card {
      background: rgba(3, 22, 15, 0.88);
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      border-radius: 32px;
      padding: clamp(32px, 5vw, 54px);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.8), 0 0 50px rgba(16, 185, 129, 0.15);
      position: relative;
      overflow: hidden;
    }

    .timer-master-card.gold-border {
      border: 2px solid rgba(245, 158, 11, 0.6);
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.85), 0 0 45px rgba(245, 158, 11, 0.2);
    }

    .timer-hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 30px;
      align-items: center;
    }

    .giant-clock-display {
      background: rgba(1, 12, 8, 0.95);
      border: 2px solid rgba(52, 211, 153, 0.4);
      border-radius: 24px;
      padding: 32px 24px;
      text-align: center;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.7);
    }

    .giant-clock-display.gold-accent {
      border-color: rgba(245, 158, 11, 0.55);
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), 0 0 30px rgba(245, 158, 11, 0.2);
    }

    .giant-clock-digits {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin: 16px 0;
    }

    .giant-clock-unit {
      text-align: center;
      min-width: 70px;
    }

    .giant-clock-val {
      font-family: var(--font-mono);
      font-size: clamp(38px, 5.5vw, 62px);
      font-weight: 800;
      color: #ffffff;
      line-height: 1;
      text-shadow: 0 0 25px rgba(52, 211, 153, 0.7);
    }

    .giant-clock-val.gold {
      color: #fbbf24;
      text-shadow: 0 0 25px rgba(245, 158, 11, 0.8);
    }

    .giant-clock-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--accent-mint);
      margin-top: 6px;
    }

    .giant-clock-colon {
      font-size: 36px;
      font-weight: 800;
      color: var(--accent-mint);
      margin-bottom: 20px;
    }

    /* Floating Story Navigation Bottom Dock */
    .story-bottom-dock {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 110;
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(3, 22, 15, 0.94);
      border: 1.5px solid rgba(52, 211, 153, 0.45);
      border-radius: 9999px;
      padding: 8px 16px;
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.85), 0 0 30px rgba(16, 185, 129, 0.25);
    }

    .dock-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 18px;
      border-radius: 9999px;
      border: 1px solid rgba(52, 211, 153, 0.35);
      background: rgba(4, 30, 20, 0.85);
      color: #e2e8f0;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .dock-btn:hover {
      background: rgba(16, 185, 129, 0.25);
      border-color: var(--accent-mint);
      color: #ffffff;
    }

    .dock-btn.primary {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      border-color: #10b981;
      color: #ffffff;
      box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }

    .dock-indicator-text {
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-mint);
      padding: 0 6px;
    }
"""

# Insert story CSS before </style>
if "/* =========================================================================" in content and "3-PAGE / STORY MULTI-SCREEN SYSTEM" not in content:
    content = content.replace("</style>", story_css + "\n  </style>")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added 3-page story styles!")
