class Cache(object):

    def __init__(self, l, k, n):
        self.l = l
        self.k = k
        self.n = n
        self.cache_array = [['Empty']*k for x in range(n)]

    def calculate(self, address_list):
        hits = 0
        misses = 0
        print('Address\t  Tag\tSet\tHit/Miss')

        for address in address_list:
            set_num = int(address[2], 16) % self.n
            tag = address[:3]
            result = self.check_line(tag, set_num)

            if result is 'Hit':
                hits += 1
            elif result is 'Miss':
                misses += 1
            print(address + ':\t ', tag ,'\t' , set_num , result)

        print('Hits:', hits, 'Misses:', misses)

    def check_line(self, tag, set_num):
        if self.cache_array[set_num] == tag:
            return 'Hit'
        else:
            self.cache_array[set_num] = tag
            return 'Miss'


def main():
    addresses = ['0000', '0004', '000C', '2200', '00D0', '00E0', '1130', '0028',
                 '113C', '2204', '0010', '0020', '0004', '0040', '2208', '0008',
                 '00A0', '0004', '1104', '0028', '000C', '0084', '000C', '3390',
                 '00B0', '1100', '0028', '0064', '0070', '00D0', '0008', '3394']

    cache = Cache(16, 1, 8)
    cache.calculate(addresses)

if __name__ == '__main__':
    main()
