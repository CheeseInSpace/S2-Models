from PIL import Image

img = Image.open("glados_eye.png")

w, h = img.size
tile_w = w // 4
tile_h = h // 4

count = 0

for y in range(4):
    for x in range(4):
        tile = img.crop((
            x * tile_w,
            y * tile_h,
            (x + 1) * tile_w,
            (y + 1) * tile_h
        ))

        tile.save(f"tile_{count:02d}.png")
        count += 1