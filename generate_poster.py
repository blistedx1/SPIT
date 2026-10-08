import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

W, H = 1200, 1680
strip_w = W // 4  # 300px each

# 1. Load player images
im_lindan = Image.open('assets/lin_dan.jpg')
im_lcw = Image.open('assets/lee_chong_wei.jpg')
im_viktor = Image.open('assets/viktor_axelsen.jpg')
im_sindhu = Image.open('assets/pv_sindhu.jpg')

# Helper: Smart crop player to strip_w x (H * 0.8)
def crop_player(im, center_x_ratio, center_y_ratio, target_w, target_h):
    # scale so target fits
    scale = max(target_w / im.width, target_h / im.height)
    nw, nh = int(im.width * scale), int(im.height * scale)
    im_scaled = im.resize((nw, nh), Image.Resampling.LANCZOS)
    
    cx = int(nw * center_x_ratio)
    cy = int(nh * center_y_ratio)
    
    left = max(0, min(nw - target_w, cx - target_w // 2))
    top = max(0, min(nh - target_h, cy - target_h // 2))
    return im_scaled.crop((left, top, left + target_w, top + target_h))

strip_h = int(H * 0.78) # 1310px

# Let's crop each player
# Lin Dan: face is centered, top 35%
strip1 = crop_player(im_lindan, 0.50, 0.32, strip_w, strip_h)
# Lee Chong Wei: face is center-left, top 32%
strip2 = crop_player(im_lcw, 0.48, 0.32, strip_w, strip_h)
# Viktor Axelsen: face is upper center
strip3 = crop_player(im_viktor, 0.45, 0.38, strip_w, strip_h)
# PV Sindhu: face is upper center
strip4 = crop_player(im_sindhu, 0.50, 0.30, strip_w, strip_h)

# Duotone color schemes:
# Strip 1 (Lin Dan): deep crimson red
# Strip 2 (Lee Chong Wei): warm fiery amber-red
# Strip 3 (Viktor Axelsen): rich blood red
# Strip 4 (PV Sindhu): deep ruby-red
schemes = [
    # shadow, mid, high
    ((15, 2, 4), (185, 20, 20), (255, 215, 195)),      # Strip 1: Crimson / Peach
    ((22, 6, 2), (210, 55, 10), (255, 230, 180)),      # Strip 2: Fiery Amber-Red
    ((16, 2, 5), (195, 25, 25), (255, 215, 200)),      # Strip 3: Blood Red / Peach
    ((20, 4, 8), (220, 30, 45), (255, 220, 210)),      # Strip 4: Ruby Red
]

def apply_duotone(img, shadow_c, mid_c, high_c, contrast=1.4, brightness=1.05):
    # Enhance contrast and brightness
    enh_c = ImageEnhance.Contrast(img).enhance(contrast)
    enh_b = ImageEnhance.Brightness(enh_c).enhance(brightness)
    
    gray = np.array(enh_b.convert('L'), dtype=np.float32) / 255.0
    # Sigmoid curve for dramatic sports poster shadows and highlights
    gray = np.clip(1.0 / (1.0 + np.exp(-11.0 * (gray - 0.46))), 0.0, 1.0)
    
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

duo1 = apply_duotone(strip1, *schemes[0], contrast=1.45, brightness=1.1)
duo2 = apply_duotone(strip2, *schemes[1], contrast=1.40, brightness=1.1)
duo3 = apply_duotone(strip3, *schemes[2], contrast=1.50, brightness=1.1)
duo4 = apply_duotone(strip4, *schemes[3], contrast=1.45, brightness=1.05)

# Create canvas
canvas = Image.new('RGB', (W, H), (10, 2, 3))

# Paste 4 strips side by side
canvas.paste(duo1, (0, 0))
canvas.paste(duo2, (strip_w, 0))
canvas.paste(duo3, (strip_w * 2, 0))
canvas.paste(duo4, (strip_w * 3, 0))

# Thin dark seams between vertical panels (just like reference)
draw = ImageDraw.Draw(canvas)
for i in [1, 2, 3]:
    x = i * strip_w
    draw.line([(x-1, 0), (x-1, strip_h)], fill=(5, 1, 1), width=2)
    draw.line([(x+1, 0), (x+1, strip_h)], fill=(20, 2, 4), width=1)

# Lower 25%: Arena floor/stands silhouette
# Load badminton_hero or create an atmospheric badminton court floor
arena = Image.open('assets/badminton_hero.jpg').resize((W, int(H * 0.35)), Image.Resampling.LANCZOS)
arena_duo = apply_duotone(arena, (5, 1, 1), (120, 15, 15), (200, 70, 50), contrast=1.6, brightness=0.75)

# Gradient fade for arena at the bottom
y_start = int(H * 0.70)
arena_crop = arena_duo.crop((0, arena_duo.height - (H - y_start), W, arena_duo.height))

# Alpha blend arena onto canvas
mask = Image.new('L', (W, H - y_start))
for y in range(H - y_start):
    alpha = int(255 * (y / (H - y_start)) ** 0.8)
    for x in range(W):
        mask.putpixel((x, y), alpha)

canvas.paste(arena_crop, (0, y_start), mask)

# Dark vignette on edges and top
top_vignette = Image.new('RGBA', (W, H), (0, 0, 0, 0))
top_draw = ImageDraw.Draw(top_vignette)
for y in range(250):
    a = int(180 * (1.0 - y / 250.0))
    top_draw.line([(0, y), (W, y)], fill=(8, 1, 2, a))
canvas.paste(top_vignette, (0, 0), top_vignette)

# Bottom dark gradient to ensure text readability
bot_vignette = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bot_draw = ImageDraw.Draw(bot_vignette)
for y in range(H - 350, H):
    dist = (y - (H - 350)) / 350.0
    a = int(210 * dist)
    bot_draw.line([(0, y), (W, y)], fill=(4, 0, 1, a))
canvas.paste(bot_vignette, (0, 0), bot_vignette)

canvas.save('assets/test_base.jpg', quality=95)
print('Base composited successfully!')
