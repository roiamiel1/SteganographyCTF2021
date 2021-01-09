import wave
from BitPool import BitPool


def plant_file(read_wave, write_wave, file_path):
    write_wave.setparams(read_wave.getparams())

    bit_pool = BitPool()
    bit_pool.set_source(file_path)

    for i in range(read_wave.getnframes()):
        frame = int(read_wave.readframes(1).hex(), 16)

        if bit_pool.eof:
            bit = 0
        else:
            bit = bit_pool.pull(1)[0]

        frame = ((frame >> 1) << 1) + bit

        write_wave.writeframesraw(frame.to_bytes(2, 'big'))


read_wave = wave.open("sound.wav", "rb")
write_wave = wave.open("out_sound.wav", "wb")

plant_file(read_wave, write_wave, "Untitled.pdf")

read_wave.close()
write_wave.close()
