from tabulate import tabulate

class Cache(object):

    def __init__(self, l, k, n):
        self.l = l
        self.k = k
        self.n = n
        self.cache_array = [['Empty']*k for x in range(n)]
        self.bits = [[0]*(k-1) for x in range(n)]
        print(tabulate(self.cache_array))
        print(tabulate(self.bits))

    def calculate_hits(self, address_list):
        hits = 0
        misses = 0
        print('Address\t  Tag\tSet\tHit/Miss')

        for address in address_list:
            set_num = int(address[2], 16) % self.n
            tag = address[:3]
            if tag in self.cache_array[set_num]:
                result = "Hit"
                hits += 1
            else:
                result = "Miss"
                misses += 1
                self.insert_line(set_num, tag)

            print(address + ':\t ', tag ,'\t' , set_num , '\t', result)

        print('Hits:', hits, 'Misses:', misses)

    def insert_line(self, set_num, tag):
        if self.k == 1:
            self.cache_array[set_num] = tag
        elif self.k == 2:
            if self.bits[set_num][0] == 0:
                self.cache_array[set_num][0] = tag
                self.bits[set_num][0] = 1
            else:
                self.cache_array[set_num][1] = tag
                self.bits[set_num][0] = 0



    # def generate_lru_lines(self, k, n):
    #     matrix = [[0 for i in range(k)] for i in range(k)]
    #     grids = [matrix]*n
    #     print(matrix)
    #     print(grids)

def main():
    addresses = ['0000', '0004', '000C', '2200', '00D0', '00E0', '1130', '0028',
                 '113C', '2204', '0010', '0020', '0004', '0040', '2208', '0008',
                 '00A0', '0004', '1104', '0028', '000C', '0084', '000C', '3390',
                 '00B0', '1100', '0028', '0064', '0070', '00D0', '0008', '3394']

    cache = Cache(16, 2, 4)
    cache.calculate_hits(addresses)
    print(tabulate(cache.cache_array))

if __name__ == '__main__':
    main()
