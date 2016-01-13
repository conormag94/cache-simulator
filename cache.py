class Cache(object):

    def __init__(self, l, k, n):
        self.l = l
        self.k = k
        self.n = n

    def calculate(self):
        print(self.l, self.k, self.n)

def main():
    cache = Cache(16, 2, 4)
    cache.calculate()

if __name__ == '__main__':
    main()
