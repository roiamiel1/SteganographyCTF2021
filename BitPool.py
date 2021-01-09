class BitPool:
    def __init__(self):
        self.file = None
        self.pool = []
        self.eof = False

    @staticmethod
    def __to_bits__(char):
        if len(char) == 0:
            char = '\x00'
        return [int(bit) for bit in bin(ord(char))[2:].zfill(8)]

    @staticmethod
    def __from_bits__(bits):
        chars = []
        for b in range(len(bits) // 8):
            byte = bits[(b * 8):((b + 1) * 8)]
            byte = int(''.join([str(bit) for bit in byte]), 2)
            if byte == 0:
                break

            chars.append(chr(byte))
        return ''.join(chars)

    @staticmethod
    def __bytes_from_bits__(bits):
        bytes = []
        for b in range(len(bits) // 8):
            byte = bits[(b * 8):((b + 1) * 8)]
            byte = int(''.join([str(bit) for bit in byte]), 2)
            bytes.append(byte)
        return bytes

    def pool_str(self):
        return self.__from_bits__(self.pool)

    def pool_bytes(self):
        return self.__bytes_from_bits__(self.pool)

    def set_source(self, filename):
        self.file = open(filename, "rb")

    def push(self, bits):
        self.pool.extend([bit & 1 for bit in bits])

    def pull(self, length):
        pool_size = len(self.pool)
        if pool_size < length and not self.eof:
            char = self.file.read(1)

            if not char:
                self.pool.extend([0] * (length - pool_size))
                self.eof = True
            else:
                self.pool.extend(self.__to_bits__(char))

        return [self.pool.pop(0) for i in range(length)]

    def size(self):
        return len(self.pool)

    def close(self):
        if self.file is not None:
            self.file.close()

    def __del__(self):
        self.close()
