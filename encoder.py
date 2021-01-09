from PIL import Image
from BitPool import BitPool


def encode_channel(channel, bits):
    channel = (channel >> len(bits))

    for bit in bits:
        channel = (channel << 1) + (bit & 1)

    return channel


def plant_file(image, file_path):
    bit_pool = BitPool()
    bit_pool.set_source(file_path)

    for y in range(image.height):
        for x in range(image.width):
            if bit_pool.eof:
                bits = [0, 0, 0, 0, 0, 0]
            else:
                bits = bit_pool.pull(6)

            r, g, b = image.getpixel((x, y))

            r = encode_channel(r, bits[0:2])
            g = encode_channel(g, bits[2:4])
            b = encode_channel(b, bits[4:6])

            image.putpixel((x, y), (r, g, b))

    assert(bit_pool.size() == 0)



image = Image.open("old.bmp")

plant_file(image, "out_sound.wav")

image.save("new.bmp")
