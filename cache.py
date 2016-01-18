from tabulate import tabulate

class Cache(object):

    def __init__(self, l, k, n):
        self.l = l
        self.k = k
        self.n = n
        self.cache_array = [['Empty']*k for x in range(n)]
        self.bits = [[0]*(k-1) for x in range(n)]
        #print(tabulate(self.cache_array))
        #print(tabulate(self.bits))

    def calculate_hits(self, address_list):
        hits = 0
        misses = 0
        print('Address\t Hit/Miss')

        for address in address_list:
            set_num = int(address[2], 16) % self.n
            tag = address[:3]

            # If there is a hit, make the current tag the most recent
            if tag in self.cache_array[set_num]:
                result = "Hit"
                hits += 1
                self.lru_update(set_num, tag)
            # If there is a Miss, insert current tag and adjust LRU
            else:
                result = "Miss"
                misses += 1
                self.insert_line(set_num, tag)

            print(address + '\t', result)

        print('Hits:', hits, 'Misses:', misses)

    # Adjusts the LRU in the set if there was a hit
    def lru_update(self, set_num, tag):
        if 'Empty' not in self.cache_array[set_num]:
            idx = self.cache_array[set_num].index(tag)
            temp_tag = self.cache_array[set_num][idx]

            while idx < self.k-1:
                self.cache_array[set_num][idx] = self.cache_array[set_num][idx+1]
                idx += 1
            self.cache_array[set_num][-1] = temp_tag

    # Inserts line and adjusts LRU. Leftmost element in cache_array is the LRU
    def insert_line(self, set_num, tag):
        # If direct-mapped, just insert into the set
        if self.k == 1:
            self.cache_array[set_num][0] = tag
        else:
            # If set is full, insert tag at the end of the array and shift all
            # elements to the left, getting rid of very left element
            if 'Empty' not in self.cache_array[set_num]:
                for i in range(self.k-1):
                    temp = self.cache_array[set_num][i+1]
                    self.cache_array[set_num][i] = temp
                self.cache_array[set_num][self.k-1] = tag
            # Insert at first empty space
            else:
                idx = self.cache_array[set_num].index('Empty')
                self.cache_array[set_num][idx] = tag

def main():
    addresses = ['0000', '0004', '000C', '2200', '00D0', '00E0', '1130', '0028',
                 '113C', '2204', '0010', '0020', '0004', '0040', '2208', '0008',
                 '00A0', '0004', '1104', '0028', '000C', '0084', '000C', '3390',
                 '00B0', '1100', '0028', '0064', '0070', '00D0', '0008', '3394']

    q1 = Cache(16, 1, 8)
    print("\nQ1(i): L=16, K=1, N=8")
    q1.calculate_hits(addresses)
    q2 = Cache(16, 2, 4)
    print("\nQ1(ii): L=16, K=2, N=4")
    q2.calculate_hits(addresses)
    q3 = Cache(16, 4, 2)
    print("\nQ1(iii): L=16, K=4, N=2")
    q3.calculate_hits(addresses)
    q4 = Cache(16, 8, 1)
    print("\nQ1(iv): L=16, K=8, N=1")
    q4.calculate_hits(addresses)

if __name__ == '__main__':
    main()
