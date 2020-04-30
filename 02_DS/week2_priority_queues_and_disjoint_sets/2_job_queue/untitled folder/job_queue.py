# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def Parent(i):
    return int((i-1)/2)

def LeftChild(i):
    return 2*i + 1

def RightChild(i):
    return 2*i + 2

def Swap (arr, p, m):
    t = arr[p]
    arr[p] = arr[m]
    arr[m] = t
    return arr

def SiftDown(i, data):

    size = len(data)
    min_idx = i
    l = LeftChild(i)
    if l <= size-1:
        if data[l] < data[min_idx]:
            min_idx = l

    r = RightChild(i)
    if r <= size-1:
        if data[r] < data[min_idx]:
            min_idx = r

    if min_idx != i:
        data = Swap(data, i, min_idx)
        data = SiftDown(min_idx, data)
    return data

def SiftUp(i, data):

    while i > 0 and data[Parent(i)] > data[i]:
        data = Swap(data, i, Parent(i))
        i = Parent(i)

    return data


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    size = len(data)
    for i in range(int(size/2)-1, -1, -1):
        #print(i)
        data = SiftDown(i, data)
    return data

"""
Naive solution works in num_workers (threads) * n_jobs
My solution is log(num_workers) * n_jobs:
create a heap - initially, node values are indices of threads;
thus, we want to always use the root node as the next thread;
after we assign a job to the root node, we need to make it "heavy" and apply the SiftDown() function;
to do this, I change the value of the root node to root + job[0] * 1e9  (notice that the num_workers and n_jobs is limited to 1e5);

finally, the only thing to take care of is the situation when all nodes are heavy. In other words, when (root - cur_t*int(1e9)) // int(1e9) > 0.
increase cur_t in this case.
    
"""

def assign_jobs(n_workers, jobs):
    result = []
    threads = list(range(n_workers))
    heap = build_heap(threads)
    heap_size = len(heap)
    cur_t = 0
    p = 0

    #print(heap)

    while True:
        if p == len(jobs):
            break
        else:
            job = jobs[p]
            root = heap[0]
            #print(root)
            if (root - cur_t*int(1e9)) // int(1e9) > 0:
                cur_t += (root - cur_t*int(1e9)) // int(1e9)
                #heap[0] -= int(1e9)
                #for heap_idx in range(heap_size):
                    #heap[heap_idx] -= int(1e9)
                    #if heap[heap_idx] // int(1e9) == 0:
                        # heap = SiftUp(heap_idx, heap)
            else:
                # print(heap)
                if job == 0:
                    result.append(AssignedJob(heap[0]-cur_t*int(1e9), cur_t))
                else:
                    result.append(AssignedJob(heap[0]-cur_t*int(1e9), cur_t))
                    heap[0] += int(job*1e9)
                    heap = SiftDown(0, heap)
                p += 1

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
