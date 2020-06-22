# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.hash_table = [[]]*self.bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c) + self._prime) % self._prime
        return (ans + self.bucket_count) % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query_naive(self, query):

        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_query(self, query):

        if query.type == "check":
            hs = query.ind
            hs_list = self.hash_table[hs]
            if hs_list:
                self.write_chain(hs_list_cur for hs_list_cur in reversed(hs_list))
            else:
                print(' ')
        else:
            st = query.s  # string from the query
            hs = self._hash_func(st)
            hs_list = self.hash_table[hs]

            if query.type == "add":
                if st not in hs_list:
                    cur_list = list(self.hash_table[hs])
                    cur_list.append(st)
                    self.hash_table[hs] = cur_list


            elif query.type == "del":
                if st in hs_list:
                    new_list = []
                    for idx in range(len(hs_list)):
                        cur_s = hs_list[idx]
                        if cur_s != st:
                            new_list.append(cur_s)
                    self.hash_table[hs] = new_list

            else:
                if st in hs_list:
                    print('yes')
                else:
                    print('no')

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
