import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math
import random

W, H = 1200, 1680
strip_w = W // 4  # 300px each

# 1. Load player images
im_lindan = Image.open('assets/lin_dan.jpg')
im_lcw = Image.open('assets/lee_chong_wei.jpg')
im_viktor = Image.open('assets/viktor_axelsen.jpg')
im_sindhu = Image.open('assets/pv_sindhu.jpg')

def crop_player(im, center_x_ratio, center_y_ratio, target_w, target_h):
    scale = max(target_w / im.width, target_h / im.height)
    nw, nh = int(im.width * scale), int(im.height * scale)
    im_scaled = im.resize((nw, nh), Image.Resampling.LANCZOS)
    
    cx = int(nw * center_x_ratio)
    cy = int(nh * center_y_ratio)
    
    left = max(0, min(nw - target_w, cx - target_w // 2))
    top = max(0, min(nh - target_h, cy - target_h // 2))
    return im_scaled.crop((left, top, left + target_w, top + target_h))

strip_h = int(H * 0.82) # 1375px

# Optimal crop centers for portrait tension matching reference
strip1 = crop_player(im_lindan, 0.48, 0.28, strip_w, strip_h)
strip2 = crop_player(im_lcw, 0.47, 0.28, strip_w, strip_h)
strip3 = crop_player(im_viktor, 0.44, 0.32, strip_w, strip_h)
strip4 = crop_player(im_sindhu, 0.50, 0.26, strip_w, strip_h)

def apply_duotone(img, shadow_c, mid_c, high_c, contrast=1.45, brightness=1.05):
    enh_c = ImageEnhance.Contrast(img).enhance(contrast)
    enh_b = ImageEnhance.Brightness(enh_c).enhance(brightness)
    
    gray = np.array(enh_b.convert('L'), dtype=np.float32) / 255.0
    # Sigmoid curve for deep sports contrast
    gray = np.clip(1.0 / (1.0 + np.exp(-11.5 * (gray - 0.47))), 0.0, 1.0)
    
    s = np.array(shadow_c, dtype=np.float32)
    m = np.array(mid_c, dtype=np.float32)
    h = np.array(high_c, dtype=np.float32)
    
    rows, cols = gray.shape
    out = np.zeros((rows, cols, 3), dtype=np.float32)
    
    mask_low = gray < 0.5
    t_l = (gray[mask_low] / 0.5)[:, None]
    out[mask_low] = s * (1.0 - t_l) + m * t_l
    
    mask_high = ~mask_low
    t_h = ((gray[mask_high] - 0.5) / 0.5)[:, None]
    out[mask_high] = m * (1.0 - t_h) + h * t_h
    
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

# Color palettes closely matching reference:
# 1. Dark red / crimson
# 2. Searing amber-crimson (like Varane in ref)
# 3. Rich crimson / scarlet (like Bruno in ref)
# 4. Vibrant deep crimson (like Gabriel/Saka in ref)
duo1 = apply_duotone(strip1, (12, 1, 2), (180, 22, 18), (255, 210, 190), contrast=1.5, brightness=1.08)
duo2 = apply_duotone(strip2, (18, 4, 1), (210, 58, 12), (255, 230, 180), contrast=1.45, brightness=1.12)
duo3 = apply_duotone(strip3, (14, 2, 4), (190, 24, 24), (255, 215, 195), contrast=1.55, brightness=1.08)
duo4 = apply_duotone(strip4, (16, 2, 6), (215, 28, 40), (255, 220, 205), contrast=1.5, brightness=1.05)

# Create canvas
canvas = Image.new('RGB', (W, H), (8, 1, 2))

# Paste strips
canvas.paste(duo1, (0, 0))
canvas.paste(duo2, (strip_w, 0))
canvas.paste(duo3, (strip_w * 2, 0))
canvas.paste(duo4, (strip_w * 3, 0))

# Seam borders between panels (dark etched lines)
draw = ImageDraw.Draw(canvas)
for i in [1, 2, 3]:
    x = i * strip_w
    draw.line([(x-1, 0), (x-1, strip_h)], fill=(2, 0, 1), width=3)
    draw.line([(x+1, 0), (x+1, strip_h)], fill=(25, 2, 4), width=1)

# Arena court/stand blend at bottom
arena = Image.open('assets/badminton_hero.jpg').resize((W, int(H * 0.38)), Image.Resampling.LANCZOS)
arena_duo = apply_duotone(arena, (4, 0, 1), (110, 12, 12), (180, 60, 45), contrast=1.7, brightness=0.7)

y_start = int(H * 0.68)
arena_crop = arena_duo.crop((0, arena_duo.height - (H - y_start), W, arena_duo.height))

# Mask with smooth ease-in gradient
mask = Image.new('L', (W, H - y_start))
for y in range(H - y_start):
    prog = y / (H - y_start)
    alpha = int(255 * (prog ** 1.1))
    for x in range(W):
        mask.putpixel((x, y), alpha)

canvas.paste(arena_crop, (0, y_start), mask)

# Dark overlays for text readability:
# 1. Center band behind MATCH DAY (subtle black smoke)
smoke = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(smoke)
for y in range(int(H * 0.45), int(H * 0.85)):
    # bell curve alpha
    mid = (H * 0.65)
    dist = abs(y - mid) / (H * 0.20)
    if dist < 1.0:
        a = int(70 * (1.0 - dist**2))
        sdraw.line([(0, y), (W, y)], fill=(4, 0, 1, a))
canvas.paste(smoke, (0, 0), smoke)

# 2. Bottom shadow
bot_vignette = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bdraw = ImageDraw.Draw(bot_vignette)
for y in range(H - 320, H):
    dist = (y - (H - 320)) / 320.0
    a = int(230 * dist)
    bdraw.line([(0, y), (W, y)], fill=(3, 0, 1, a))
canvas.paste(bot_vignette, (0, 0), bot_vignette)

# 3. Top shadow for badges
top_vignette = Image.new('RGBA', (W, H), (0, 0, 0, 0))
tdraw = ImageDraw.Draw(top_vignette)
for y in range(260):
    dist = 1.0 - (y / 260.0)
    a = int(140 * dist)
    tdraw.line([(0, y), (W, y)], fill=(5, 0, 1, a))
canvas.paste(top_vignette, (0, 0), top_vignette)

# -------------------------------------------------------------
# CREATE BADGES (Team 1: LEGENDS, Team 2: TITANS)
# -------------------------------------------------------------
def make_shield_badge(team_name, sub_name, is_round=True):
    # Render at 4x for high anti-aliasing
    S = 600
    b_im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(b_im)
    cx, cy = S // 2, S // 2
    
    font_bold = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 46)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 28)
    font_stars = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 38)
    
    if is_round:
        # Round Crest (similar to Manchester United crest in ref)
        # Outer gold/white rings
        r_out = 270
        b_draw.ellipse([cx - r_out, cy - r_out, cx + r_out, cy + r_out], fill=(15, 1, 3, 230), outline=(245, 245, 245, 240), width=8)
        b_draw.ellipse([cx - r_out + 14, cy - r_out + 14, cx + r_out - 14, cy + r_out - 14], outline=(230, 200, 130, 220), width=4)
        
        # Center shield
        pts = [
            (cx - 150, cy - 140),
            (cx + 150, cy - 140),
            (cx + 150, cy + 30),
            (cx, cy + 180),
            (cx - 150, cy + 30)
        ]
        b_draw.polygon(pts, fill=(180, 20, 20, 220), outline=(255, 255, 255, 230))
        
        # Badminton Shuttlecock silhouette in center
        # Crown
        b_draw.polygon([(cx - 70, cy - 80), (cx + 70, cy - 80), (cx + 35, cy + 30), (cx - 35, cy + 30)], fill=(255, 255, 255, 240))
        # Lines on feathers
        for ox in [-40, -15, 15, 40]:
            b_draw.line([(cx + ox, cy - 75), (cx + ox//2, cy + 25)], fill=(180, 20, 20, 200), width=3)
        # Cork base
        b_draw.ellipse([cx - 35, cy + 10, cx + 35, cy + 70], fill=(240, 240, 240, 255), outline=(180, 20, 20), width=2)
        
        # Top banner text
        b_draw.text((cx, cy - 200), team_name, font=font_bold, fill=(255, 255, 255, 255), anchor="mm")
        # Bottom banner text
        b_draw.text((cx, cy + 205), sub_name, font=font_sub, fill=(240, 210, 150, 255), anchor="mm")
        # 3 stars
        b_draw.text((cx, cy - 145), "★   ★   ★", font=font_stars, fill=(255, 220, 100, 240), anchor="mm")
        
    else:
        # Pointed Shield Crest (similar to Arsenal crest in ref)
        pts_out = [
            (cx - 210, cy - 230),
            (cx + 210, cy - 230),
            (cx + 210, cy + 80),
            (cx, cy + 260),
            (cx - 210, cy + 80)
        ]
        b_draw.polygon(pts_out, fill=(12, 1, 2, 230), outline=(255, 255, 255, 240), width=8)
        
        pts_in = [
            (cx - 190, cy - 210),
            (cx + 190, cy - 210),
            (cx + 190, cy + 70),
            (cx, cy + 235),
            (cx - 190, cy + 70)
        ]
        b_draw.polygon(pts_in, fill=(195, 25, 25, 230), outline=(255, 255, 255, 180), width=4)
        
        # Team name banner inside shield
        b_draw.rectangle([cx - 180, cy - 200, cx + 180, cy - 130], fill=(10, 1, 2, 220))
        b_draw.text((cx, cy - 165), team_name, font=font_bold, fill=(255, 255, 255, 255), anchor="mm")
        
        # Crossed Badminton Rackets & Lightning / Shuttlecock
        b_draw.line([(cx - 100, cy - 80), (cx + 100, cy + 120)], fill=(255, 255, 255, 240), width=8)
        b_draw.line([(cx + 100, cy - 80), (cx - 100, cy + 120)], fill=(255, 255, 255, 240), width=8)
        b_draw.ellipse([cx - 120, cy - 105, cx - 75, cy - 50], outline=(255, 255, 255, 240), width=6)
        b_draw.ellipse([cx + 75, cy - 105, cx + 120, cy - 50], outline=(255, 255, 255, 240), width=6)
        
        # Golden Shuttlecock in center
        b_draw.polygon([(cx - 45, cy - 20), (cx + 45, cy - 20), (cx + 20, cy + 50), (cx - 20, cy + 50)], fill=(255, 220, 110, 240))
        b_draw.ellipse([cx - 20, cy + 40, cx + 20, cy + 75], fill=(255, 255, 255, 255))
        
        # Bottom subtitle
        b_draw.text((cx, cy + 140), sub_name, font=font_sub, fill=(255, 255, 255, 230), anchor="mm")
        b_draw.text((cx, cy + 180), "★ ★ ★", font=font_stars, fill=(255, 220, 100, 240), anchor="mm")
        
    return b_im.resize((150, 150), Image.Resampling.LANCZOS)

badge1 = make_shield_badge("LEGENDS", "LIN DAN • LCW", is_round=True)
badge2 = make_shield_badge("TITANS", "AXELSEN • SINDHU", is_round=False)

# Center X is W // 2 = 600
center_x = W // 2

# Place Badge 1 (Team Legends)
canvas.paste(badge1, (center_x - 75, 120), badge1)

# Place "VS" in bold white condensed font
font_vs = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 72)
draw.text((center_x, 320), "VS", font=font_vs, fill=(255, 255, 255), anchor="mm")

# Place Badge 2 (Team Titans)
canvas.paste(badge2, (center_x - 75, 380), badge2)

# -------------------------------------------------------------
# MASSIVE "MATCH DAY" TYPOGRAPHY (Exact replica of reference)
# -------------------------------------------------------------
# In the reference, MATCH and DAY are bold condensed uppercase, stark white, tight leading
font_match = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 270)
font_day = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 290)

# Add drop shadow / grit outline
y_match = 830
y_day = 1070

# Draw subtle shadow for 3D depth
for ox, oy in [(-2, 2), (2, 2), (-3, 3), (3, 3), (0, 4)]:
    draw.text((center_x + ox, y_match + oy), "MATCH", font=font_match, fill=(10, 0, 2), anchor="mm")
    draw.text((center_x + ox, y_day + oy), "DAY", font=font_day, fill=(10, 0, 2), anchor="mm")

# Draw solid white text
draw.text((center_x, y_match), "MATCH", font=font_match, fill=(255, 255, 255), anchor="mm")
draw.text((center_x, y_day), "DAY", font=font_day, fill=(255, 255, 255), anchor="mm")

# -------------------------------------------------------------
# BOTTOM MATCH DETAILS & SIGNATURE (Exact layout of reference)
# -------------------------------------------------------------
# Bottom Right: 3 lines stacked, right aligned
# In reference:
# KICK-OFF 15:30 (GMT)
# SUNDAY
# OLD TRAFFORD STADIUM

font_details_bold = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 34)
font_details_norm = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 28)

details_x = W - 60
details_y = H - 150

draw.text((details_x, details_y), "MATCH TIME: 20:00 (IST)", font=font_details_bold, fill=(255, 255, 255), anchor="rm")
draw.text((details_x, details_y + 36), "TONIGHT • 8:00 PM", font=font_details_norm, fill=(245, 205, 110), anchor="rm")
draw.text((details_x, details_y + 70), "SURYODAYA PARK CENTRE COURT", font=font_details_bold, fill=(255, 255, 255), anchor="rm")

# Bottom Left: Signature Script Logo (like 'Kwesi' in reference)
# Let's draw stylized 'Suryodaya' or 'SPBC Super-Clash'
font_sig = ImageFont.truetype('C:/Windows/Fonts/arialbi.ttf', 44)
font_sig_sub = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 20)

draw.text((70, H - 110), "Suryodaya", font=font_sig, fill=(255, 255, 255), anchor="lm")
draw.text((72, H - 72), "BADMINTON CHAMPIONSHIP 2026", font=font_sig_sub, fill=(230, 80, 80), anchor="lm")

# Add subtle player names on the 4 columns
font_player = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 24)
players = [
    ("LIN DAN", 0 * strip_w + strip_w // 2),
    ("LEE CHONG WEI", 1 * strip_w + strip_w // 2),
    ("VIKTOR AXELSEN", 2 * strip_w + strip_w // 2),
    ("P. V. SINDHU", 3 * strip_w + strip_w // 2),
]

for pname, px in players:
    # Small pill tag behind player name
    bbox = font_player.getbbox(pname)
    tw = bbox[2] - bbox[0] + 20
    th = 28
    py = 50
    draw.rectangle([px - tw//2, py - th//2, px + tw//2, py + th//2], fill=(10, 1, 2, 190), outline=(220, 40, 40, 140))
    draw.text((px, py), pname, font=font_player, fill=(255, 255, 255), anchor="mm")

# -------------------------------------------------------------
# FILM GRAIN / GRITTY SPORTS NOISE OVERLAY (Matches reference grit)
# -------------------------------------------------------------
noise = np.random.normal(0, 14, (H, W, 3)).astype(np.float32)
arr = np.array(canvas, dtype=np.float32)
arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
final_poster = Image.fromarray(arr)

# Save high-res poster
output_path = 'assets/suryodaya_match_day_poster.jpg'
final_poster.save(output_path, quality=94)
print(f"Match Day Poster successfully saved to {output_path} ({W}x{H})")
