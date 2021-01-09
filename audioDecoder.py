import wave
from BitPool import BitPool


def extract_file(read_wave):
    bit_pool = BitPool()

    for i in range(read_wave.getnframes()):
        frame = int(read_wave.readframes(1).hex(), 16)
        bit_pool.push([frame & 1])

    return bytes(bit_pool.pool_bytes())


read_wave = wave.open("level1.wav", "rb")

f = open("level2.pdf", "wb")
f.write(extract_file(read_wave))
f.close()

read_wave.close()
