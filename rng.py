class LinearCongruentialGenerator:
    def __init__(self, seed):
        self.state = seed
        # params
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

seed = 12345
rng = LinearCongruentialGenerator(seed)

for _ in range(10):
    print(rng.next())

class MersenneTwister:
    def __init__(self, seed):
        self.MT = [0] * 624
        self.index = 0
        self.MT[0] = seed
        for i in range(1, 624):
            self.MT[i] = (0x6c078965 * (self.MT[i - 1] ^ (self.MT[i - 1] >> 30)) + i) & 0xffffffff

    def extract_number(self):
        if self.index == 0:
            self.twist()

        y = self.MT[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= y >> 18

        self.index = (self.index + 1) % 624
        return y

    def twist(self):
        for i in range(624):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i + 1) % 624] & 0x7fffffff)
            self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.MT[i] ^= 0x9908b0df

    def next(self):
        return self.extract_number()

seed = 12345
mt = MersenneTwister(seed)
print(mt.next())
