from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager

image = Image.new('RGB', (640, 360), (255, 255, 255))
drawer = ImageDraw.Draw(image)

font_list = matplotlib.font_manager.fontManager.ttflist


def size_to_line_height(fontpath, size):
    font_sample = ImageFont.truetype(fontpath, size)
    sample_size = drawer.textsize("Hello python language", font=font_sample)
    offset = font_sample.getoffset("Hello python language")
    print(sample_size, offset)
    return sample_size[1] + offset[1]


def drawText(text, x, y, font):
    size = drawer.textsize(text, font=font)
    offset = font.getoffset(text)
    print("size", size)
    print("offset", offset)
    print("size+offest", size[0] + offset[0], size[1] + offset[1])
    drawer.text((x, y), text, fill='black', font=font)
    drawer.rectangle(
        (x, y, x + size[0] + offset[0], y + size[1] + offset[1]), outline='black')

# drawing text

font_size = size_to_line_height('/Library/Fonts/ヒラギノ角ゴ Pro W6.otf', 40)

print("font size", font_size)

font = ImageFont.truetype('/Library/Fonts/ヒラギノ角ゴ Pro W6.otf', 40)

drawText("Hello", 0, 0, font)
drawText("Hello python", 0, 50, font)
drawText("Hello python language", 0, 100, font)
drawText("Hello あいうエオ漢字", 0, 150, font)

# drawing rectangle surrounding text

image.save('example.png', 'PNG')
