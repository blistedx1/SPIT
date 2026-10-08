import re

html_path = r"c:\test\badminton.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_css = """  <style>
    :root {
      --bg-base: #02120b;
      --bg-surface: #042115;
      --bg-card: rgba(4, 28, 19, 0.82);
      --bg-card-hover: rgba(6, 38, 26, 0.95);
      --bg-card-active: rgba(8, 48, 33, 0.98);
      --border-subtle: rgba(52, 211, 153, 0.22);
      --border-glow: rgba(16, 185, 129, 0.5);
      --border-bright: #10b981;
      --accent-emerald: #10b981;
      --accent-mint: #34d399;
      --accent-mint-light: #6ee7b7;
      --accent-gold: #f59e0b;
      --accent-gold-light: #fef08a;
      --accent-coral: #ff334b;
      --text-main: #ffffff;
      --text-ivory: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --font-serif: 'Playfair Display', 'Fraunces', Georgia, serif;
      --font-display: 'Fraunces', 'Playfair Display', serif;
      --font-main: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif;
      --font-mono: 'Space Grotesk', monospace, sans-serif;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      background-color: var(--bg-base);
      background-image: 
        radial-gradient(ellipse 90% 50% at 50% 0%, rgba(16, 185, 129, 0.16) 0%, transparent 60%),
        radial-gradient(ellipse 70% 60% at 50% 100%, rgba(2, 18, 11, 0.95) 0%, transparent 70%),
        url('assets/emerald_silk_bg.jpg');
      background-attachment: fixed;
      background-position: center;
      background-size: cover;
      background-repeat: no-repeat;
      color: var(--text-main);
      font-family: var(--font-main);
      overflow-x: hidden;
      line-height: 1.55;
    }

    /* Ambient atmospheric soft emerald glows */
    .ambient-glow-1 {
      position: fixed;
      top: -120px;
      left: 50%;
      transform: translateX(-50%);
      width: 1000px;
      height: 600px;
      background: radial-gradient(circle, rgba(16, 185, 129, 0.2) 0%, rgba(5, 150, 105, 0.08) 50%, rgba(2, 18, 11, 0) 75%);
      pointer-events: none;
      z-index: 0;
      filter: blur(100px);
    }

    .ambient-glow-2 {
      position: fixed;
      top: 40%;
      right: -120px;
      width: 700px;
      height: 700px;
      background: radial-gradient(circle, rgba(52, 211, 153, 0.16) 0%, rgba(2, 18, 11, 0) 70%);
      pointer-events: none;
      z-index: 0;
      filter: blur(110px);
    }

    .ambient-glow-3 {
      position: fixed;
      bottom: 0;
      left: -120px;
      width: 800px;
      height: 700px;
      background: radial-gradient(circle, rgba(16, 185, 129, 0.14) 0%, rgba(2, 18, 11, 0) 70%);
      pointer-events: none;
      z-index: 0;
      filter: blur(120px);
    }

    /* Subtle light technical coordinate grid */
    .grid-bg {
      position: fixed;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(52, 211, 153, 0.035) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(52, 211, 153, 0.035) 1px, transparent 1px);
      background-size: 80px 80px;
      pointer-events: none;
      z-index: 1;
      mask-image: radial-gradient(ellipse 90% 80% at 50% 35%, black 25%, transparent 90%);
      -webkit-mask-image: radial-gradient(ellipse 90% 80% at 50% 35%, black 25%, transparent 90%);
    }

    .container {
      max-width: 1380px;
      margin: 0 auto;
      padding: 0 32px;
      position: relative;
      z-index: 2;
    }

    /* Floating Island Header Bar (Dark Emerald Glass) */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 16px 28px 0;
      background: transparent;
      pointer-events: none;
    }

    .header-inner {
      max-width: 1240px;
      margin: 0 auto;
      padding: 14px 28px;
      background: rgba(3, 22, 15, 0.88);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      border: 1.5px solid rgba(52, 211, 153, 0.3);
      border-radius: 24px;
      box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.7), 0 0 30px rgba(16, 185, 129, 0.12);
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      pointer-events: auto;
      transition: all 0.3s ease;
    }

    .header-inner:hover {
      border-color: rgba(52, 211, 153, 0.5);
      box-shadow: 0 20px 45px -5px rgba(0, 0, 0, 0.85), 0 0 40px rgba(16, 185, 129, 0.2);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: #ffffff;
      flex-shrink: 0;
    }

    .brand-icon {
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.3) 0%, rgba(5, 150, 105, 0.5) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      border: 1px solid rgba(52, 211, 153, 0.5);
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.25);
    }

    .brand-icon svg {
      width: 22px;
      height: 22px;
      stroke: var(--accent-mint);
      fill: none;
    }

    .brand-name {
      font-family: var(--font-serif);
      font-size: 17px;
      font-weight: 800;
      letter-spacing: 0.02em;
      color: #ffffff;
      display: block;
      line-height: 1.2;
    }

    .brand-sub {
      font-size: 10.5px;
      color: var(--accent-mint);
      font-family: var(--font-mono);
      font-weight: 700;
      letter-spacing: 0.16em;
      display: block;
    }

    /* Desktop Navigation */
    .desktop-nav {
      display: block;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 32px;
      list-style: none;
    }

    .nav-links a {
      color: #cbd5e1;
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      transition: all 0.25s ease;
      letter-spacing: 0.01em;
      position: relative;
      padding: 6px 0;
    }

    .nav-links a:hover, .nav-links a.active {
      color: var(--accent-mint);
      text-shadow: 0 0 12px rgba(52, 211, 153, 0.5);
    }

    .nav-links a.active::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 2px;
      background: var(--accent-mint);
      border-radius: 99px;
      box-shadow: 0 0 8px var(--accent-mint);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      background: rgba(4, 30, 20, 0.85);
      border: 1px solid rgba(52, 211, 153, 0.35);
      border-radius: 9999px;
      font-size: 12px;
      color: var(--accent-mint);
      font-weight: 700;
      letter-spacing: 0.06em;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .badge-pill:hover {
      border-color: var(--accent-mint);
      box-shadow: 0 0 20px rgba(52, 211, 153, 0.3);
    }

    .status-dot {
      width: 8px;
      height: 8px;
      background-color: var(--accent-mint);
      border-radius: 50%;
      box-shadow: 0 0 10px rgba(52, 211, 153, 0.85);
      animation: pulse-dot 2s infinite ease-in-out;
    }

    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px rgba(52, 211, 153, 0.85); }
      50% { opacity: 0.4; transform: scale(0.85); box-shadow: 0 0 4px rgba(52, 211, 153, 0.3); }
    }

    /* Mobile Hamburger Menu Button */
    .mobile-menu-btn {
      display: none;
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: rgba(4, 30, 20, 0.9);
      border: 1px solid rgba(52, 211, 153, 0.4);
      color: var(--accent-mint);
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.25s ease;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }

    .mobile-menu-btn:hover, .mobile-menu-btn:active {
      border-color: var(--accent-mint);
      background: rgba(6, 42, 28, 0.95);
      color: #ffffff;
    }

    .mobile-menu-btn svg {
      width: 22px;
      height: 22px;
    }

    /* Mobile Nav Drawer (Floating Rounded Card) */
    .mobile-nav-drawer {
      display: block;
      max-height: 0;
      opacity: 0;
      overflow: hidden;
      transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
      max-width: 1240px;
      margin: 8px auto 0;
      background: rgba(3, 24, 16, 0.97);
      border: 1.5px solid rgba(52, 211, 153, 0.4);
      border-radius: 24px;
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 35px rgba(16, 185, 129, 0.15);
      pointer-events: none;
    }

    .mobile-nav-drawer.is-open {
      max-height: 520px;
      opacity: 1;
      pointer-events: auto;
    }

    .mobile-nav-inner {
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .mobile-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 11.5px;
      color: var(--accent-mint);
      font-family: var(--font-mono);
      font-weight: 700;
      letter-spacing: 0.08em;
      background: rgba(4, 30, 20, 0.85);
      padding: 6px 14px;
      border-radius: 9999px;
      border: 1px solid rgba(52, 211, 153, 0.35);
      width: fit-content;
    }

    .mobile-nav-links {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .mobile-nav-links li a {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 12px 16px;
      border-radius: 12px;
      color: #e2e8f0;
      text-decoration: none;
      font-size: 15px;
      font-weight: 600;
      transition: all 0.2s ease;
      background: transparent;
    }

    .mobile-nav-links li a svg {
      width: 18px;
      height: 18px;
      color: var(--accent-mint);
      transition: transform 0.2s ease;
    }

    .mobile-nav-links li a:hover, .mobile-nav-links li a:active {
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-mint);
      transform: translateX(4px);
    }

    .mobile-nav-footer {
      display: flex;
      flex-direction: column;
      gap: 14px;
      padding-top: 14px;
      border-top: 1px solid rgba(52, 211, 153, 0.2);
    }

    .mobile-reg-btn {
      width: 100%;
      justify-content: center;
      padding: 12px 20px;
    }

    .mobile-court-info {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-size: 12px;
      color: var(--text-muted);
    }

    .mobile-court-info svg {
      width: 14px;
      height: 14px;
      color: var(--accent-mint);
    }

    /* =========================================================================
       LUXURY EDITORIAL EMERALD SILK HERO SECTION
       ========================================================================= */
    .hero-section {
      min-height: calc(100vh - 100px);
      padding: 50px 0 70px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      text-align: center;
      z-index: 10;
    }

    /* Master Glassmorphic Hero Stage Card */
    .hero-glass-stage {
      position: relative;
      width: 100%;
      max-width: 1180px;
      margin: 0 auto;
      background: rgba(3, 20, 14, 0.72);
      backdrop-filter: blur(40px);
      -webkit-backdrop-filter: blur(40px);
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      border-radius: 44px;
      padding: clamp(52px, 8vw, 92px) clamp(28px, 6vw, 72px);
      box-shadow: 
        0 40px 100px -20px rgba(0, 0, 0, 0.9),
        0 0 70px rgba(16, 185, 129, 0.18),
        inset 0 1px 0 rgba(255, 255, 255, 0.15);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 36px;
      overflow: hidden;
      text-align: center;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hero-glass-stage::before {
      content: '';
      position: absolute;
      top: 0;
      left: -50%;
      width: 200%;
      height: 100%;
      background: radial-gradient(circle at 50% 0%, rgba(16, 185, 129, 0.22) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }

    /* Hero Eyebrow Emerald Pill */
    .hero-eyebrow-pill {
      position: relative;
      z-index: 2;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 8px 24px;
      background: rgba(4, 30, 20, 0.88);
      border: 1.5px solid rgba(52, 211, 153, 0.45);
      border-radius: 9999px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
      font-family: var(--font-mono);
      font-size: clamp(11.5px, 1.3vw, 13.5px);
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--accent-mint);
      animation: float-soft 4s ease-in-out infinite;
    }

    @keyframes float-soft {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-4px); }
    }

    /* EDITORIAL DISPLAY GRAND HEADLINE */
    .hero-sign-container {
      position: relative;
      z-index: 2;
      max-width: 1080px;
    }

    .hero-grand-sign {
      font-family: var(--font-display);
      font-size: clamp(3.4rem, 8vw, 7.5rem);
      line-height: 0.95;
      letter-spacing: -0.035em;
      color: #ffffff;
      margin: 0;
      text-align: center;
    }

    .hero-sign-title {
      display: block;
      font-style: italic;
      font-weight: 700;
      color: #f1f5f9;
      text-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
    }

    .hero-sign-flourish {
      display: inline-block;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: -0.04em;
      position: relative;
      text-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
    }

    .coral-dot {
      display: inline-block;
      width: clamp(14px, 1.8vw, 24px);
      height: clamp(14px, 1.8vw, 24px);
      background: #ff334b;
      border-radius: 50%;
      margin-left: 6px;
      box-shadow: 0 0 24px rgba(255, 51, 75, 0.95), 0 0 10px rgba(255, 51, 75, 0.6);
      vertical-align: baseline;
      position: relative;
      bottom: 2px;
      animation: dot-glow 3s infinite ease-in-out;
    }

    @keyframes dot-glow {
      0%, 100% { transform: scale(1); box-shadow: 0 0 24px rgba(255, 51, 75, 0.95); }
      50% { transform: scale(1.18); box-shadow: 0 0 35px rgba(255, 51, 75, 1); }
    }

    .hero-editorial-sub {
      margin-top: 20px;
      font-family: var(--font-mono);
      font-size: clamp(12px, 1.4vw, 15px);
      font-weight: 700;
      letter-spacing: 0.38em;
      color: #e2e8f0;
      text-transform: uppercase;
      opacity: 0.92;
      text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
    }

    /* MOTTO LUXURY GLASS CARD */
    .hero-motto-glasscard {
      position: relative;
      z-index: 2;
      max-width: 940px;
      margin: 8px auto 0;
      background: rgba(4, 30, 20, 0.82);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      border-radius: 28px;
      padding: 30px 44px;
      box-shadow: 
        0 25px 60px -10px rgba(0, 0, 0, 0.75),
        0 0 40px rgba(16, 185, 129, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hero-motto-glasscard:hover {
      transform: translateY(-4px);
      border-color: rgba(52, 211, 153, 0.65);
      box-shadow: 0 30px 70px -10px rgba(0, 0, 0, 0.9), 0 0 55px rgba(16, 185, 129, 0.25);
    }

    .motto-quote-mark {
      font-family: var(--font-serif);
      font-size: 56px;
      line-height: 0.6;
      color: var(--accent-mint);
      opacity: 0.9;
    }

    .hero-motto-text {
      font-family: var(--font-main);
      font-size: clamp(1.28rem, 2.2vw, 1.9rem);
      font-weight: 700;
      line-height: 1.44;
      letter-spacing: -0.015em;
      color: #ffffff;
      text-align: center;
      margin: 0;
    }

    .hero-motto-text .motto-highlight {
      color: #34d399;
      text-shadow: 0 0 25px rgba(52, 211, 153, 0.45);
    }

    .motto-meta-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 20px;
      background: rgba(2, 16, 11, 0.7);
      border: 1px solid rgba(52, 211, 153, 0.35);
      border-radius: 9999px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-mint);
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }

    /* MINIMALIST CIRCULAR ARROW ENTER WEBSITE BUTTON */
    .hero-enter-container {
      position: relative;
      z-index: 2;
      margin-top: 16px;
    }

    .btn-enter-website {
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: #f8fafc;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }

    .btn-enter-website .btn-enter-label {
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.32em;
      text-transform: uppercase;
      color: #e2e8f0;
      transition: all 0.3s ease;
    }

    .btn-enter-website .btn-enter-arrow {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      border: 1.5px solid rgba(255, 255, 255, 0.75);
      background: rgba(255, 255, 255, 0.06);
      backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 6px 25px rgba(0, 0, 0, 0.5);
    }

    .btn-enter-website:hover .btn-enter-label {
      color: var(--accent-mint);
      text-shadow: 0 0 14px rgba(52, 211, 153, 0.6);
      letter-spacing: 0.36em;
    }

    .btn-enter-website:hover .btn-enter-arrow {
      border-color: var(--accent-mint);
      background: rgba(52, 211, 153, 0.22);
      color: var(--accent-mint);
      transform: translateY(8px);
      box-shadow: 0 0 30px rgba(52, 211, 153, 0.5);
    }

    /* Generic Buttons & Actions */
    .btn-primary {
      display: inline-flex;
      align-items: center;
      gap: 14px;
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      border: 1px solid rgba(52, 211, 153, 0.4);
      border-radius: 9999px;
      padding: 10px 12px 10px 26px;
      color: #ffffff;
      text-decoration: none;
      font-size: 14.5px;
      font-weight: 700;
      letter-spacing: 0.02em;
      box-shadow: 0 10px 25px -4px rgba(16, 185, 129, 0.4);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }

    .btn-primary:hover {
      background: linear-gradient(135deg, #059669 0%, #047857 100%);
      box-shadow: 0 15px 35px -5px rgba(16, 185, 129, 0.55), 0 0 30px rgba(52, 211, 153, 0.35);
      transform: translateY(-2px);
    }

    .btn-circle-arrow {
      width: 36px;
      height: 36px;
      background: #ffffff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #047857;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    }

    .btn-circle-arrow svg {
      width: 18px;
      height: 18px;
      stroke-width: 2.5;
    }

    .btn-primary:hover .btn-circle-arrow {
      transform: translateX(3px) scale(1.06);
      background: #e6fffa;
      color: #065f46;
    }

    /* Countdown Bar (Luxury Emerald Silk Card) */
    .countdown-bar {
      margin-top: 44px;
      padding: 26px 36px;
      background: rgba(3, 22, 15, 0.88);
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      border-radius: 28px;
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 35px rgba(16, 185, 129, 0.12);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 24px;
      transition: all 0.3s ease;
    }

    .countdown-bar:hover {
      border-color: rgba(52, 211, 153, 0.55);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 45px rgba(16, 185, 129, 0.2);
    }

    .countdown-info {
      display: flex;
      align-items: center;
      gap: 18px;
    }

    .countdown-icon {
      width: 50px;
      height: 50px;
      border-radius: 14px;
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid rgba(52, 211, 153, 0.45);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--accent-mint);
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
    }

    .countdown-text h4 {
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      font-family: var(--font-serif);
      letter-spacing: 0.02em;
    }

    .countdown-text p {
      font-size: 13.5px;
      color: #94a3b8;
    }

    .countdown-timer {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .timer-unit {
      text-align: center;
    }

    .timer-val {
      font-size: 34px;
      font-weight: 800;
      font-family: var(--font-mono);
      color: #ffffff;
      min-width: 50px;
      line-height: 1;
      text-shadow: 0 0 18px rgba(52, 211, 153, 0.65);
    }

    .timer-lbl {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: var(--accent-mint);
      margin-top: 4px;
      font-weight: 700;
    }

    .timer-divider {
      font-size: 26px;
      color: rgba(52, 211, 153, 0.55);
      font-weight: 600;
      margin-top: -12px;
    }

    /* Section: Men's Doubles Structure */
    .division-section {
      padding: 90px 0;
      position: relative;
      z-index: 10;
      border-top: 1px solid rgba(52, 211, 153, 0.2);
    }

    .section-eyebrow {
      text-align: center;
      margin-bottom: 50px;
    }

    .section-eyebrow .badge-pill {
      margin-bottom: 16px;
    }

    .section-title {
      font-family: var(--font-serif);
      font-size: clamp(2.2rem, 4vw, 3.4rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
    }

    .section-desc {
      font-size: 15.5px;
      color: #94a3b8;
      max-width: 620px;
      margin: 12px auto 0;
      line-height: 1.6;
    }

    .division-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
      margin-top: 36px;
    }

    .doubles-feature-card {
      background: rgba(4, 28, 19, 0.82);
      border: 1.5px solid rgba(52, 211, 153, 0.28);
      border-radius: 24px;
      padding: 32px;
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.55);
    }

    .doubles-feature-card:hover {
      border-color: rgba(52, 211, 153, 0.65);
      transform: translateY(-6px);
      background: rgba(6, 38, 26, 0.95);
      box-shadow: 0 25px 55px -10px rgba(0, 0, 0, 0.75), 0 0 40px rgba(16, 185, 129, 0.22);
    }

    .doubles-feature-card .category-icon {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      background: rgba(16, 185, 129, 0.18);
      border: 1px solid rgba(52, 211, 153, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--accent-mint);
      margin-bottom: 20px;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.18);
    }

    .doubles-feature-card h3 {
      font-size: 19px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .doubles-feature-card p {
      font-size: 14px;
      color: #94a3b8;
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .card-footer-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(52, 211, 153, 0.18);
      padding-top: 16px;
      font-size: 12px;
      color: #94a3b8;
      font-family: var(--font-mono);
      font-weight: 600;
    }

    .card-footer-meta .slots {
      color: var(--accent-mint);
      font-weight: 700;
    }

    /* Official Draw & Chit Lottery Notice Banner */
    .draw-live-notice-banner {
      background: linear-gradient(145deg, rgba(4, 30, 20, 0.95) 0%, rgba(2, 18, 12, 0.95) 100%);
      border: 2px solid rgba(245, 158, 11, 0.5);
      border-radius: 28px;
      padding: clamp(28px, 4vw, 40px);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 40px rgba(245, 158, 11, 0.15);
      margin-bottom: 36px;
      position: relative;
      overflow: hidden;
      text-align: center;
    }

    .draw-live-notice-banner::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent, #f59e0b, #10b981, transparent);
    }

    .draw-banner-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 18px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.5);
      border-radius: 9999px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.12em;
      color: var(--accent-gold);
      margin-bottom: 16px;
    }

    .draw-banner-heading {
      font-family: var(--font-serif);
      font-size: clamp(22px, 3.2vw, 32px);
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 14px;
      line-height: 1.3;
    }

    .draw-banner-text {
      font-size: 15.5px;
      color: #e2e8f0;
      max-width: 820px;
      margin: 0 auto 16px;
      line-height: 1.6;
    }

    .draw-banner-subtext {
      font-size: 15px;
      font-weight: 600;
      color: var(--accent-mint);
      max-width: 820px;
      margin: 0 auto 24px;
      line-height: 1.6;
      border-top: 1px dashed rgba(52, 211, 153, 0.35);
      padding-top: 16px;
    }

    .draw-countdown-box {
      background: rgba(1, 12, 8, 0.95);
      border: 1.5px solid rgba(52, 211, 153, 0.4);
      border-radius: 20px;
      padding: 20px;
      max-width: 480px;
      margin: 0 auto;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
    }

    .draw-box-title {
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.12em;
      color: var(--accent-mint);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-bottom: 12px;
    }

    .draw-timer-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
    }

    .draw-time-cell {
      text-align: center;
      min-width: 60px;
    }

    .draw-time-number {
      font-family: var(--font-mono);
      font-size: 36px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1;
      display: block;
      text-shadow: 0 0 16px rgba(52, 211, 153, 0.6);
    }

    .draw-time-label {
      font-size: 11px;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
      margin-top: 4px;
      display: block;
    }

    .draw-time-colon {
      font-size: 26px;
      font-weight: 800;
      color: var(--accent-mint);
      margin-bottom: 16px;
    }

    /* Official Squad & Brackets Section */
    .squad-section {
      padding: 90px 0 60px;
      position: relative;
      z-index: 10;
      border-top: 1px solid rgba(52, 211, 153, 0.2);
    }

    .tournament-panel {
      background: rgba(3, 24, 16, 0.88);
      border: 1.5px solid rgba(52, 211, 153, 0.32);
      border-radius: 28px;
      padding: 26px 28px;
      box-shadow: 0 20px 55px rgba(0, 0, 0, 0.7), 0 0 35px rgba(16, 185, 129, 0.1);
      margin-top: 28px;
      position: relative;
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
    }

    .bracket-toolbar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      padding-bottom: 20px;
      border-bottom: 1.5px solid rgba(52, 211, 153, 0.22);
      margin-bottom: 22px;
    }

    .bracket-toolbar-left {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .bracket-toolbar-right {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }

    .bracket-tabs {
      display: inline-flex;
      background: rgba(2, 16, 11, 0.85);
      padding: 5px;
      border-radius: 16px;
      gap: 6px;
      border: 1px solid rgba(52, 211, 153, 0.3);
    }

    .bracket-tab-btn {
      padding: 9px 18px;
      font-size: 13.5px;
      font-weight: 700;
      color: #94a3b8;
      border-radius: 12px;
      background: transparent;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
      font-family: var(--font-main);
    }

    .bracket-tab-btn:hover {
      color: #ffffff;
      background: rgba(16, 185, 129, 0.1);
    }

    .bracket-tab-btn.active {
      background: rgba(16, 185, 129, 0.25);
      color: var(--accent-mint);
      border: 1px solid rgba(52, 211, 153, 0.45);
      box-shadow: 0 0 18px rgba(52, 211, 153, 0.35);
    }

    .action-btn-sm {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      font-size: 12.5px;
      font-weight: 700;
      border-radius: 12px;
      border: 1px solid rgba(52, 211, 153, 0.35);
      background: rgba(4, 30, 20, 0.85);
      color: #e2e8f0;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: var(--font-main);
    }

    .action-btn-sm:hover {
      background: rgba(16, 185, 129, 0.2);
      border-color: var(--accent-mint);
      color: #ffffff;
      box-shadow: 0 0 15px rgba(16, 185, 129, 0.25);
    }

    .action-btn-sm.primary {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #ffffff;
      border-color: #10b981;
      box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }

    .action-btn-sm.primary:hover {
      background: linear-gradient(135deg, #059669 0%, #047857 100%);
      transform: translateY(-1px);
    }

    /* Round Filter Pills */
    .round-filter-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: nowrap;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      padding-bottom: 6px;
      margin-bottom: 14px;
      scrollbar-width: none;
    }

    .round-filter-bar::-webkit-scrollbar {
      display: none;
    }

    .round-filter-pill {
      background: rgba(3, 20, 14, 0.85);
      border: 1px solid rgba(52, 211, 153, 0.3);
      color: #94a3b8;
      padding: 7px 16px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 700;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .round-filter-pill:hover {
      background: rgba(16, 185, 129, 0.18);
      color: #ffffff;
      border-color: var(--accent-mint);
    }

    .round-filter-pill.active {
      background: var(--accent-emerald);
      color: #ffffff;
      border-color: var(--accent-emerald);
      box-shadow: 0 0 18px rgba(16, 185, 129, 0.45);
    }

    /* Smooth Bracket View & Nodes */
    .bracket-scroll-nav-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 14px;
      flex-wrap: wrap;
    }

    .mobile-scroll-hint {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(52, 211, 153, 0.4);
      color: var(--accent-mint);
      padding: 6px 14px;
      border-radius: 10px;
      font-size: 11.5px;
      font-weight: 700;
      font-family: var(--font-mono);
    }

    .bracket-scroll-btns {
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .bracket-nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 14px;
      font-size: 12px;
      font-weight: 700;
      font-family: var(--font-mono);
      border-radius: 10px;
      background: rgba(4, 28, 19, 0.9);
      border: 1px solid rgba(52, 211, 153, 0.35);
      color: #e2e8f0;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .bracket-nav-btn:hover {
      background: rgba(16, 185, 129, 0.25);
      border-color: var(--accent-mint);
      color: var(--accent-mint);
    }

    .bracket-tree-wrapper {
      position: relative;
      width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      -webkit-overflow-scrolling: touch;
      padding: 10px 4px 20px;
      scroll-behavior: smooth;
      scrollbar-width: thin;
      scrollbar-color: #10b981 rgba(3, 20, 14, 0.8);
    }

    .bracket-tree-wrapper::-webkit-scrollbar {
      height: 8px;
    }

    .bracket-tree-wrapper::-webkit-scrollbar-track {
      background: rgba(3, 20, 14, 0.8);
      border-radius: 999px;
    }

    .bracket-tree-wrapper::-webkit-scrollbar-thumb {
      background: linear-gradient(90deg, #10b981, #059669);
      border-radius: 999px;
    }

    .bracket-tree-flow {
      display: flex;
      align-items: stretch;
      gap: 18px;
      width: max-content;
      min-width: 100%;
      padding: 0 4px;
    }

    .bracket-round-column {
      display: flex;
      flex-direction: column;
      flex: 1 1 240px;
      min-width: 230px;
      max-width: 290px;
    }

    .bracket-round-header {
      text-align: center;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1.5px solid rgba(52, 211, 153, 0.3);
      position: relative;
    }

    .bracket-round-title {
      font-size: 13px;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-family: var(--font-mono);
    }

    .bracket-round-sub {
      font-size: 10.5px;
      color: var(--accent-mint);
      margin-top: 2px;
      font-weight: 700;
      font-family: var(--font-mono);
    }

    .bracket-matches-list {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      flex-grow: 1;
      gap: 10px;
    }

    .bracket-match-node {
      background: rgba(4, 30, 20, 0.92);
      border: 1.5px solid rgba(52, 211, 153, 0.3);
      border-radius: 14px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
      overflow: hidden;
      transition: all 0.22s ease;
      position: relative;
    }

    .bracket-match-node:hover {
      border-color: rgba(52, 211, 153, 0.8);
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.7), 0 0 25px rgba(16, 185, 129, 0.25);
      transform: translateY(-2px);
    }

    .match-meta-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 5px 10px;
      background: rgba(2, 16, 11, 0.9);
      border-bottom: 1px solid rgba(52, 211, 153, 0.2);
      font-size: 10px;
      font-family: var(--font-mono);
      font-weight: 700;
      color: #94a3b8;
    }

    .match-court-tag {
      color: var(--accent-mint);
      background: rgba(16, 185, 129, 0.18);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 9.5px;
    }

    .match-team-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      cursor: pointer;
      transition: all 0.15s ease;
      border-bottom: 1px solid rgba(52, 211, 153, 0.12);
      user-select: none;
      min-height: 32px;
      gap: 8px;
    }

    .match-team-row:last-child {
      border-bottom: none;
    }

    .match-team-row:hover {
      background: rgba(16, 185, 129, 0.15);
    }

    .match-team-info {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-grow: 1;
      min-width: 0;
      overflow: hidden;
    }

    .match-seed-badge {
      width: 20px;
      height: 20px;
      border-radius: 6px;
      background: rgba(3, 20, 14, 0.85);
      color: #cbd5e1;
      font-size: 10px;
      font-weight: 800;
      font-family: var(--font-mono);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      border: 1px solid rgba(52, 211, 153, 0.25);
    }

    .match-team-name {
      font-size: 12px;
      font-weight: 700;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      line-height: 1.25;
    }

    .match-team-row.is-winner {
      background: rgba(16, 185, 129, 0.25);
    }

    .match-team-row.is-winner .match-seed-badge {
      background: #10b981;
      color: #ffffff;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.6);
    }

    .match-team-row.is-winner .match-team-name {
      color: #34d399;
      font-weight: 800;
    }

    .match-team-row.is-loser {
      opacity: 0.45;
    }

    /* Champion Podium Column */
    .champion-column {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      flex: 0 0 200px;
      min-width: 170px;
      max-width: 220px;
    }

    .champion-podium-card {
      background: linear-gradient(145deg, rgba(4, 35, 24, 0.95) 0%, rgba(3, 20, 14, 0.95) 100%);
      border: 2px solid rgba(245, 158, 11, 0.75);
      border-radius: 20px;
      padding: 22px 16px;
      text-align: center;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.85), 0 0 35px rgba(245, 158, 11, 0.3);
      width: 100%;
      position: relative;
    }

    .champion-trophy-icon {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: linear-gradient(135deg, #fef08a 0%, #facc15 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 12px;
      box-shadow: 0 4px 20px rgba(234, 179, 8, 0.5);
      color: #78350f;
    }

    .champion-title {
      font-size: 10.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #f59e0b;
      font-family: var(--font-mono);
      margin-bottom: 6px;
    }

    .champion-team-name {
      font-size: 14.5px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 10px;
      line-height: 1.3;
      word-break: break-word;
    }

    .champion-badge {
      display: inline-block;
      background: #f59e0b;
      color: #03140e;
      font-size: 9.5px;
      font-weight: 800;
      font-family: var(--font-mono);
      padding: 4px 12px;
      border-radius: 9999px;
      letter-spacing: 0.06em;
    }

    /* League Stage Tables & Pools */
    .league-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(440px, 1fr));
      gap: 32px;
      margin-top: 14px;
    }

    .pool-card {
      background: rgba(4, 28, 19, 0.88);
      border: 1.5px solid rgba(52, 211, 153, 0.3);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    }

    .pool-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 18px 24px;
      background: rgba(2, 16, 11, 0.9);
      border-bottom: 1.5px solid rgba(52, 211, 153, 0.25);
    }

    .pool-badge {
      width: 36px;
      height: 36px;
      border-radius: 12px;
      background: var(--accent-emerald);
      color: #ffffff;
      font-weight: 800;
      font-family: var(--font-mono);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 17px;
      box-shadow: 0 0 18px rgba(16, 185, 129, 0.45);
    }

    .standings-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }

    .standings-table th {
      padding: 14px 18px;
      text-align: left;
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent-mint);
      background: rgba(2, 16, 11, 0.7);
      border-bottom: 1px solid rgba(52, 211, 153, 0.22);
      font-family: var(--font-mono);
    }

    .standings-table td {
      padding: 14px 18px;
      border-bottom: 1px solid rgba(52, 211, 153, 0.12);
      color: #e2e8f0;
    }

    .standings-table tr:hover td {
      background: rgba(16, 185, 129, 0.1);
    }

    .standings-table tr.qualify-row td {
      font-weight: 700;
    }

    .standings-table tr.qualify-row td:first-child {
      border-left: 3.5px solid #10b981;
    }

    .qualify-dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      margin-right: 8px;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.9);
    }

    /* Roster Grid & Cards */
    .roster-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }

    .roster-card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 18px 22px;
      background: rgba(4, 28, 19, 0.88);
      border: 1.5px solid rgba(52, 211, 153, 0.3);
      border-radius: 18px;
      transition: all 0.25s ease;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.45);
    }

    .roster-card:hover {
      background: rgba(6, 38, 26, 0.98);
      border-color: var(--accent-mint);
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.7), 0 0 30px rgba(16, 185, 129, 0.25);
      transform: translateY(-3px);
    }

    .player-seed {
      width: 34px;
      height: 34px;
      border-radius: 10px;
      background: rgba(16, 185, 129, 0.22);
      color: var(--accent-mint);
      font-size: 13.5px;
      font-weight: 800;
      font-family: var(--font-mono);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid rgba(52, 211, 153, 0.45);
    }

    .player-name-text {
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
    }

    .inline-add-team-bar {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      background: rgba(2, 16, 11, 0.9);
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      padding: 18px;
      border-radius: 18px;
      margin-bottom: 24px;
      align-items: center;
    }

    .inline-input {
      flex: 1;
      min-width: 190px;
      padding: 11px 16px;
      border-radius: 12px;
      border: 1px solid rgba(52, 211, 153, 0.35);
      font-size: 14px;
      font-family: var(--font-main);
      outline: none;
      background: rgba(4, 28, 19, 0.85);
      color: #ffffff;
      transition: all 0.2s ease;
    }

    .inline-input:focus {
      border-color: var(--accent-mint);
      box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.25);
    }

    /* Modal Dark Emerald Glass */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(1, 10, 7, 0.85);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .modal-box {
      width: 100%;
      max-width: 560px;
      background: rgba(4, 26, 18, 0.96);
      border: 1.5px solid rgba(52, 211, 153, 0.45);
      border-radius: 32px;
      padding: 38px;
      box-shadow: 0 35px 85px rgba(0, 0, 0, 0.9), 0 0 55px rgba(16, 185, 129, 0.25);
      position: relative;
      max-height: 90vh;
      overflow-y: auto;
      color: #ffffff;
    }

    .modal-close-btn {
      position: absolute;
      top: 20px;
      right: 20px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(3, 20, 14, 0.85);
      border: 1px solid rgba(52, 211, 153, 0.35);
      color: #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .modal-close-btn:hover {
      background: rgba(239, 68, 68, 0.2);
      border-color: #ef4444;
      color: #ef4444;
    }

    /* Form Styles */
    .form-group {
      margin-bottom: 20px;
    }

    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 700;
      color: #cbd5e1;
      margin-bottom: 8px;
      font-family: var(--font-main);
    }

    .form-input {
      width: 100%;
      padding: 12px 16px;
      background: rgba(2, 16, 11, 0.85);
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      border-radius: 12px;
      color: #ffffff;
      font-size: 14px;
      font-family: var(--font-main);
      outline: none;
      transition: all 0.2s ease;
    }

    .form-input:focus {
      border-color: var(--accent-mint);
      box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.25);
    }

    /* Responsive */
    @media (max-width: 900px) {
      .desktop-nav, .hide-on-mobile {
        display: none !important;
      }
      .mobile-menu-btn {
        display: flex;
      }
      .league-grid {
        grid-template-columns: 1fr;
      }
      .countdown-bar {
        flex-direction: column;
        text-align: center;
        gap: 20px;
      }
      .countdown-info {
        flex-direction: column;
      }
      .hero-glass-stage {
        padding: 40px 20px;
        border-radius: 32px;
      }
    }
  </style>"""

# Replace from <style> to </style>
pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
new_content = pattern.sub(new_css, content, count=1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated CSS in badminton.html successfully!")
