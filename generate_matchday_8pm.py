import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

# 1. Load original reference poster
orig_poster = Image.open('assets/reference_matchday_poster.jpg').convert('RGB')
w, h = orig_poster.size
arr = np.array(orig_poster)

# 2. Extract accurate text mask for MATCH DAY
text_mask = (arr[:, :, 0] > 230) & (arr[:, :, 1] > 230) & (arr[:, :, 2] > 230) & (np.arange(h)[:, None] > 515) & (np.arange(h)[:, None] < 845)

# 3. Clean Center Column (x: 327 to 491, y: 110 to 495)
col_top = np.mean(arr[95:110, 335:485], axis=(0,1))
col_bot = np.mean(arr[495:510, 335:485], axis=(0,1))
for y in range(110, 495):
    t = (y - 110) / (495.0 - 110.0)
    base_color = col_top * (1.0 - t) + col_bot * t
    for x in range(327, 492):
        noise = np.random.randint(-3, 4)
        arr[y, x] = np.clip(base_color + noise, 0, 255).astype(np.uint8)

for y in range(105, 115):
    alpha = (y - 105) / 10.0
    for x in range(327, 492):
        arr[y, x] = (arr[y, x] * (1.0 - alpha) + col_top * alpha).astype(np.uint8)
for y in range(490, 500):
    alpha = (y - 490) / 10.0
    for x in range(327, 492):
        arr[y, x] = (col_bot * (1.0 - alpha) + arr[y, x] * alpha).astype(np.uint8)

# 4. Clean the entire Strip 3 area (x: 491 to 654) down to y=785
for y in range(0, 785):
    t = y / 785.0
    r = int(24 * (1.0 - t) + 8 * t)
    g = int(3 * (1.0 - t) + 1 * t)
    b = 0
    for x in range(491, 654):
        noise = np.random.randint(-2, 3)
        arr[y, x] = [max(0, r + noise), max(0, g + noise), 0]

# 5. Crop Person 3 with heroic portrait framing
im_p = Image.open('assets/custom_player_1.jpg')
c_p3 = im_p.crop((270, 60, 380, 350))
w_s3 = 654 - 491 # 163 px
h_s3 = int(c_p3.height * (w_s3 / float(c_p3.width))) # ~430 px
p3_res = c_p3.resize((w_s3, h_s3), Image.Resampling.LANCZOS)
p3_res = ImageEnhance.Sharpness(p3_res).enhance(1.5)

def apply_strip4_amber(img):
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0
    gray = np.clip(1.0 / (1.0 + np.exp(-11.5 * (gray - 0.46))), 0.0, 1.0)
    s = np.array([12, 1, 0], dtype=np.float32)
    m = np.array([215, 75, 14], dtype=np.float32)
    h = np.array([255, 230, 175], dtype=np.float32)
    out = np.zeros((gray.shape[0], gray.shape[1], 3), dtype=np.float32)
    mask_low = gray < 0.5
    tl = (gray[mask_low] / 0.5)[:, None]
    out[mask_low] = s * (1.0 - tl) + m * tl
    mask_high = ~mask_low
    th = ((gray[mask_high] - 0.5) / 0.5)[:, None]
    out[mask_high] = m * (1.0 - th) + h * th
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

p3_amber = apply_strip4_amber(p3_res)
p3_arr = np.array(p3_amber)

# Paste p3_amber at y=30
y_top = 30
for y in range(h_s3):
    dest_y = y_top + y
    if dest_y >= 785: break
    alpha = 1.0
    if y > h_s3 - 90:
        alpha = (h_s3 - y) / 90.0
    for x in range(w_s3):
        dest_x = 491 + x
        orig_val = arr[dest_y, dest_x]
        arr[dest_y, dest_x] = (p3_arr[y, x] * alpha + orig_val * (1.0 - alpha)).astype(np.uint8)

# 6. Restore MATCH DAY text (crisp white)
for y in range(515, 845):
    for x in range(300, 660):
        if text_mask[y, x]:
            arr[y, x] = [255, 255, 255]

# 7. Seam borders
result = Image.fromarray(arr)
draw = ImageDraw.Draw(result)

draw.line([(491, 0), (491, 785)], fill=(32, 3, 2), width=2)
draw.line([(654, 0), (654, 785)], fill=(32, 3, 2), width=2)

# 8. Center Column Typography: '8 PM TONIGHT'
center_x = (327 + 491) // 2 # 409
font_time = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 56)
font_tonight = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 42)
font_pill = ImageFont.truetype('C:/Windows/Fonts/ARIALNB.TTF', 18)

y_mid = 265
badge_w, badge_h = 132, 28
draw.rounded_rectangle([center_x - badge_w//2, y_mid - 90, center_x + badge_w//2, y_mid - 62], radius=7, fill=(18, 2, 2), outline=(235, 165, 45), width=1)
draw.text((center_x, y_mid - 76), 'MATCH TIME', font=font_pill, fill=(250, 205, 95), anchor='mm')

for ox, oy in [(-3, 2), (3, 2), (-3, 4), (3, 4), (0, 4)]:
    draw.text((center_x + ox, y_mid - 22 + oy), '8 PM', font=font_time, fill=(8, 0, 0), anchor='mm')
    draw.text((center_x + ox, y_mid + 32 + oy), 'TONIGHT', font=font_tonight, fill=(8, 0, 0), anchor='mm')

draw.text((center_x, y_mid - 22), '8 PM', font=font_time, fill=(255, 255, 255), anchor='mm')
draw.text((center_x, y_mid + 32), 'TONIGHT', font=font_tonight, fill=(250, 195, 55), anchor='mm')

draw.line([(center_x - 52, y_mid + 70), (center_x + 52, y_mid + 70)], fill=(235, 165, 45), width=2)

out_file = 'assets/suryodaya_matchday_8pm_poster.jpg'
result.save(out_file, quality=96)
print(f'Successfully updated {out_file}')
