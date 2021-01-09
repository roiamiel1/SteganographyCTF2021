from PIL import Image
from BitPool import BitPool


def decode_channel(channel, bits):
    bits.append((channel >> 1) & 1)
    bits.append(channel & 1)


def extract_text(image):
    bit_pool = BitPool()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))

            bits = []
            decode_channel(r, bits)
            decode_channel(g, bits)
            decode_channel(b, bits)
            bit_pool.push(bits)

    return bytes(bit_pool.pool_bytes())


image = Image.open("new.bmp")

f = open("level1.wav", "wb")
f.write(extract_text(image))
f.close()
