import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math

W, H = 1200, 1680
strip_w = W // 4  # 300px each
strip_h = 1260

# -------------------------------------------------------------
# 1. PREPARE 4 NATURAL COLOR PLAYER PORTRAITS (NO FILTER ON FACES)
# -------------------------------------------------------------

# Player 1 (custom_player_1.jpg: sunglasses & printed shirt)
im1 = Image.open('assets/custom_player_1.jpg').convert('RGB')
# Balanced portrait bust: head, sunglasses, smile, collar & printed shirt
c1 = im1.crop((265, 115, 395, 295)) # 130 x 180
scale1 = strip_w / float(c1.width)
nw1, nh1 = strip_w, int(c1.height * scale1)
p1_port = c1.resize((nw1, nh1), Image.Resampling.LANCZOS)
p1_port = ImageEnhance.Sharpness(p1_port).enhance(1.4)
p1_port = ImageEnhance.Color(p1_port).enhance(1.05)

strip1 = Image.new('RGB', (strip_w, strip_h), (14, 2, 3))
strip1.paste(p1_port, (0, 70))
fade_h1 = 140
base_y1 = 70 + nh1
for y in range(base_y1 - fade_h1, min(strip_h, base_y1)):
    alpha = (y - (base_y1 - fade_h1)) / float(fade_h1)
    for x in range(strip_w):
        orig_px = strip1.getpixel((x, y))
        dark_px = (14, 2, 3)
        strip1.putpixel((x, y), tuple(int(orig_px[i] * (1.0 - alpha) + dark_px[i] * alpha) for i in range(3)))

# Player 2 (custom_player_2.jpg: Yonex jersey, racket, tilak)
im2 = Image.open('assets/custom_player_2.jpg').convert('RGB')
c2 = im2.crop((60, 20, 780, 960)) # 720 x 940
scale2 = strip_w / float(c2.width)
nw2, nh2 = strip_w, int(c2.height * scale2)
c2_res = c2.resize((nw2, nh2), Image.Resampling.LANCZOS)
strip2 = Image.new('RGB', (strip_w, strip_h), (14, 2, 3))
strip2.paste(c2_res, (0, 65))
fade_h2 = 140
base_y2 = 65 + nh2
for y in range(base_y2 - fade_h2, min(strip_h, base_y2)):
    alpha = (y - (base_y2 - fade_h2)) / float(fade_h2)
    for x in range(strip_w):
        orig_px = strip2.getpixel((x, y))
        dark_px = (14, 2, 3)
        strip2.putpixel((x, y), tuple(int(orig_px[i] * (1.0 - alpha) + dark_px[i] * alpha) for i in range(3)))

# Player 3 (custom_player_3.jpg: green jacket, smiling)
im3 = Image.open('assets/custom_player_3.jpg').convert('RGB')
c3 = im3.crop((200, 70, 710, 700)) # 510 x 630
scale3 = strip_w / float(c3.width)
nw3, nh3 = strip_w, int(c3.height * scale3)
c3_res = c3.resize((nw3, nh3), Image.Resampling.LANCZOS)
strip3 = Image.new('RGB', (strip_w, strip_h), (14, 2, 3))
strip3.paste(c3_res, (0, 65))
fade_h3 = 140
base_y3 = 65 + nh3
for y in range(base_y3 - fade_h3, min(strip_h, base_y3)):
    alpha = (y - (base_y3 - fade_h3)) / float(fade_h3)
    for x in range(strip_w):
        orig_px = strip3.getpixel((x, y))
        dark_px = (14, 2, 3)
        strip3.putpixel((x, y), tuple(int(orig_px[i] * (1.0 - alpha) + dark_px[i] * alpha) for i in range(3)))

# Player 4 (custom_player_4.jpg: black Puma hoodie)
im4 = Image.open('assets/custom_player_4.jpg').convert('RGB')
c4 = im4.crop((120, 180, 660, 840)) # 540 x 660
scale4 = strip_w / float(c4.width)
nw4, nh4 = strip_w, int(c4.height * scale4)
c4_res = c4.resize((nw4, nh4), Image.Resampling.LANCZOS)
strip4 = Image.new('RGB', (strip_w, strip_h), (14, 2, 3))
strip4.paste(c4_res, (0, 65))
fade_h4 = 140
base_y4 = 65 + nh4
for y in range(base_y4 - fade_h4, min(strip_h, base_y4)):
    alpha = (y - (base_y4 - fade_h4)) / float(fade_h4)
    for x in range(strip_w):
        orig_px = strip4.getpixel((x, y))
        dark_px = (14, 2, 3)
        strip4.putpixel((x, y), tuple(int(orig_px[i] * (1.0 - alpha) + dark_px[i] * alpha) for i in range(3)))

# -------------------------------------------------------------
# 2. ASSEMBLE POSTER CANVAS (RED & BLACK SPORTS THEME)
# -------------------------------------------------------------
canvas = Image.new('RGB', (W, H), (10, 1, 2))

# Paste natural color strips side by side
canvas.paste(strip1, (0, 0))
canvas.paste(strip2, (strip_w, 0))
canvas.paste(strip3, (strip_w * 2, 0))
canvas.paste(strip4, (strip_w * 3, 0))

draw = ImageDraw.Draw(canvas)

# Vertical red & black seam lines between panels
for i in [1, 2, 3]:
    x = i * strip_w
    draw.line([(x-2, 0), (x-2, strip_h)], fill=(4, 0, 1), width=2)
    draw.line([(x, 0), (x, strip_h)], fill=(180, 20, 25), width=2)
    draw.line([(x+2, 0), (x+2, strip_h)], fill=(4, 0, 1), width=2)

# Bottom Arena & Court silhouette in deep red & black
arena = Image.open('assets/badminton_hero.jpg').resize((W, int(H * 0.40)), Image.Resampling.LANCZOS)
gray_arena = np.array(arena.convert('L'), dtype=np.float32) / 255.0
gray_arena = np.clip(1.0 / (1.0 + np.exp(-10.0 * (gray_arena - 0.45))), 0.0, 1.0)
s = np.array([5, 0, 1], dtype=np.float32)
m = np.array([130, 15, 18], dtype=np.float32)
h = np.array([210, 65, 45], dtype=np.float32)
arena_arr = np.zeros((gray_arena.shape[0], gray_arena.shape[1], 3), dtype=np.float32)
mask_low = gray_arena < 0.5
tl = (gray_arena[mask_low] / 0.5)[:, None]
arena_arr[mask_low] = s * (1.0 - tl) + m * tl
mask_high = ~mask_low
th = ((gray_arena[mask_high] - 0.5) / 0.5)[:, None]
arena_arr[mask_high] = m * (1.0 - th) + h * th
arena_duo = Image.fromarray(np.clip(arena_arr, 0, 255).astype(np.uint8))

y_start = int(H * 0.68)
arena_crop = arena_duo.crop((0, arena_duo.height - (H - y_start), W, arena_duo.height))
mask_court = Image.new('L', (W, H - y_start))
for y in range(H - y_start):
    prog = y / float(H - y_start)
    mask_court.putpixel((0, y), int(255 * (prog ** 1.2)))
mask_court = mask_court.resize((W, H - y_start))
canvas.paste(arena_crop, (0, y_start), mask_court)

# Dark gradient at the bottom for match info
bot_grad = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bdraw = ImageDraw.Draw(bot_grad)
for y in range(H - 350, H):
    dist = (y - (H - 350)) / 350.0
    a = int(240 * dist)
    bdraw.line([(0, y), (W, y)], fill=(6, 1, 2, a))
canvas.paste(bot_grad, (0, 0), bot_grad)

# Subtle top shadow for logo / badges
top_grad = Image.new('RGBA', (W, H), (0, 0, 0, 0))
tdraw = ImageDraw.Draw(top_grad)
for y in range(250):
    dist = 1.0 - (y / 250.0)
    a = int(140 * dist)
    tdraw.line([(0, y), (W, y)], fill=(6, 1, 2, a))
canvas.paste(top_grad, (0, 0), top_grad)

# -------------------------------------------------------------
# 3. OFFICIAL TOURNAMENT LOGO (CLEAN ROUND PNG WITH TRANSPARENCY)
# -------------------------------------------------------------
logo = Image.open('assets/clean_round_logo.png').convert('RGBA')
logo_size = 195
logo_resized = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

center_x = W // 2
logo_y = 95

# Circular dark glow backing behind logo
glow = Image.new('RGBA', (logo_size + 40, logo_size + 40), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
gdraw.ellipse([6, 6, logo_size + 34, logo_size + 34], fill=(8, 1, 2, 240), outline=(220, 25, 30, 220), width=4)
canvas.paste(glow, (center_x - (logo_size + 40)//2, logo_y - 20), glow)
# Paste logo using its alpha channel
canvas.paste(logo_resized, (center_x - logo_size//2, logo_y), logo_resized)

# "VS" below official logo
font_vs = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 72)
font_team = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 22)

# Pill badge behind VS
vs_y = logo_y + logo_size + 45
pill_w, pill_h = 110, 56
draw.rounded_rectangle([center_x - pill_w//2, vs_y - pill_h//2, center_x + pill_w//2, vs_y + pill_h//2], radius=12, fill=(10, 1, 2), outline=(220, 30, 35), width=3)
draw.text((center_x, vs_y - 1), "VS", font=font_vs, fill=(255, 255, 255), anchor="mm")

# Team badges on left and right
# Left: TEAM 1
draw.rounded_rectangle([center_x - 390, 48, center_x - 140, 88], radius=8, fill=(10, 1, 2, 230), outline=(200, 30, 35), width=2)
draw.text((center_x - 265, 67), "TEAM 1 • MEN'S DOUBLES", font=font_team, fill=(255, 225, 225), anchor="mm")

# Right: TEAM 2
draw.rounded_rectangle([center_x + 140, 48, center_x + 390, 88], radius=8, fill=(10, 1, 2, 230), outline=(200, 30, 35), width=2)
draw.text((center_x + 265, 67), "TEAM 2 • MEN'S DOUBLES", font=font_team, fill=(255, 225, 225), anchor="mm")

# -------------------------------------------------------------
# 4. MASSIVE "MATCH DAY" TYPOGRAPHY (Stark white, condensed)
# -------------------------------------------------------------
font_match = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 265)
font_day = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 285)

y_match = 830
y_day = 1065

# Deep 3D drop shadow
for ox, oy in [(-4, 3), (4, 3), (-5, 5), (5, 5), (0, 7), (0, 9)]:
    draw.text((center_x + ox, y_match + oy), "MATCH", font=font_match, fill=(4, 0, 1), anchor="mm")
    draw.text((center_x + ox, y_day + oy), "DAY", font=font_day, fill=(4, 0, 1), anchor="mm")

# Solid crisp white letters
draw.text((center_x, y_match), "MATCH", font=font_match, fill=(255, 255, 255), anchor="mm")
draw.text((center_x, y_day), "DAY", font=font_day, fill=(255, 255, 255), anchor="mm")

# -------------------------------------------------------------
# 5. BOTTOM MATCH DETAILS & OFFICIAL LOGO BRANDING
# -------------------------------------------------------------
font_details_bold = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 34)
font_details_norm = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 28)

details_x = W - 60
details_y = H - 150

draw.text((details_x, details_y), "MATCH TIME: 20:00 (IST)", font=font_details_bold, fill=(255, 255, 255), anchor="rm")
draw.text((details_x, details_y + 36), "TONIGHT • 8:00 PM", font=font_details_norm, fill=(245, 205, 110), anchor="rm")
draw.text((details_x, details_y + 70), "SURYODAYA PARK CENTRE COURT", font=font_details_bold, fill=(255, 255, 255), anchor="rm")

# Bottom Left: Small official badge + typography
small_logo = logo.resize((92, 92), Image.Resampling.LANCZOS)
canvas.paste(small_logo, (60, H - 162), small_logo)

font_brand_title = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 38)
font_brand_sub = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 20)

draw.text((168, H - 135), "SURYODAYA PARK", font=font_brand_title, fill=(255, 255, 255), anchor="lm")
draw.text((170, H - 98), "OFFICIAL BADMINTON TOURNAMENT 2026", font=font_brand_sub, fill=(235, 70, 75), anchor="lm")

# Save high-res poster
output_path = 'assets/suryodaya_match_day_poster.jpg'
canvas.save(output_path, quality=95)
print(f"Match Day Poster successfully saved at {output_path} ({W}x{H})")
