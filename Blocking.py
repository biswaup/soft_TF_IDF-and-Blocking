import Dictionary as dict

class Blocking:
    def CreateHashTable(self, data):
        hash_table = dict.my_dictionary()
        count = -1

        for d in data:
            key = self.CreateHashKey(d)
            count = count + 1
            d = d + ',' + str(count)
            # check if key exists
            if key in hash_table:
                hash_table.update(key, d)
            else:
                hash_table.add(key, d)
        return hash_table


    def CreateHashKey(self, name):
        key = ''
        for w in name.split():
            key = key + w[0]
        key = ''.join(sorted(key))

        return key


    def FindKeys(self, key):
        size = 1 << len(key)
        num = len(key)
        lstKeys = []

        for i in range(1, size-1, 1):
            val = bin(i)[2:].zfill(num)
            tot = ''
            for j in range(0, len(val)):
                if j < num:
                    if val[j] == '1':
                        if not key[j].isdigit():
                            tot = tot + key[j]
            lstKeys.append(tot)
        return list(set(lstKeys))

