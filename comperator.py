from PIL import Image

imageA = Image.open("old.bmp")
imageB = Image.open("new.bmp")

for x in range(imageA.width):
    for y in range(imageB.height):
        rA, gA, bA = imageA.getpixel((x, y))
        rB, gB, bB = imageB.getpixel((x, y))

        s = abs(rA - rB) + abs(gA - gB) + abs(bA - bB)
        color = int((0xFF / 3) * s)

        imageA.putpixel((x, y), (color, color, color))


imageA.save("diff.bmp")
