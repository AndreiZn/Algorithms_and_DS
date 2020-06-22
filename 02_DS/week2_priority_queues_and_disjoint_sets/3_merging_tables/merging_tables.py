# python3

import os


class Database:
    def __init__(self, row_counts):
        self.row_counts = list(row_counts)
        self.max_row_count = max(self.row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def union(self, i, j):
        i_id = self.get_parent(i)
        j_id = self.get_parent(j)

        if i_id == j_id:
            return
        if self.ranks[i_id] > self.ranks[j_id]:
            self.parents[j_id] = i_id
            self.row_counts[i_id] += self.row_counts[j_id]
            if self.row_counts[i_id] > self.max_row_count:
                self.max_row_count = self.row_counts[i_id]
        else:
            self.parents[i_id] = j_id
            self.row_counts[j_id] += self.row_counts[i_id]
            if self.row_counts[j_id] > self.max_row_count:
                self.max_row_count = self.row_counts[j_id]
            if self.ranks[i_id] == self.ranks[j_id]:
                self.ranks[j_id] += 1


    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        self.union(src, dst)
        # update max_row_count with the new maximum table size
        #num_rows_merged = self.row_counts[src] + self.row_counts[dst]
        #self.row_counts[src] = num_rows_merged
        #self.row_counts[dst] = num_rows_merged

        #a = list(self.row_counts)
        #self.max_idx = a.index(self.max_row_count)
        return True

    def get_parent(self, table):
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():

    # test_dir = '/Users/andreizn/Desktop/Algorithms_and_DS/02_DS/week2_priority_queues_and_disjoint_sets/3_merging_tables/tests/'
    # test_files = sorted(os.listdir(test_dir))
    # #print(test_files)
    # for file_id in range(0, len(test_files), 2):
    #     test_filename = test_dir + test_files[file_id]
    #     # print(test_filename)
    #     f = open(test_filename, "r")
    #     correct_ans_filename = test_dir + test_files[file_id + 1]
    #     f_cor = open(correct_ans_filename, "r")
    #     correct_ans = f_cor.readlines()
    #     text = f.readlines()
    #     nums = list(map(int, text[0].split()))
    #     n_tables, n_queries = nums[0], nums[1]
    #     counts = list(map(int, text[1].split()))
    #     assert len(counts) == n_tables
    #     db = Database(counts)
    #     for i in range(n_queries):
    #         dst, src = map(int, text[i+2].split())
    #         db.merge(dst - 1, src - 1)
    #         correct_max_count = list(map(int, correct_ans[i].split()))[0]
    #         assert db.max_row_count == correct_max_count
    #         if i % 1000 == 0:
    #             print(i)


        # print('test ', file_id, 'passed')
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
