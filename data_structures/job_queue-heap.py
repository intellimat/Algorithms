# python3
'''
PROBLEM DESCRIPTION

Task:
You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚
jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately
takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop
until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the
thread with smaller index takes the job. For each job you know exactly how long will it take any thread
to process this job, and this time is the same for all the threads. You need to determine for each job
which thread will process it and when will it start processing.

Input Format: 
The first line of the input contains integers 𝑛 and 𝑚.
The second line contains 𝑚 integers 𝑡𝑖 — the times in seconds it takes any thread to process 𝑖-th job.
The times are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting from 0.

Constraints:
1 ≤ 𝑛 ≤ 105; 1 ≤ 𝑚 ≤ 105; 0 ≤ 𝑡𝑖 ≤ 109.

Output Format: 
Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two spaceseparated
integers — the 0-based index of the thread which will process the 𝑖-th job and the time
in seconds when it will start processing that job.
'''




from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Thread():
    def __init__(self, id, finish_time):
        self.id = id
        self.finish_time = finish_time


class MinHeap():
    def __init__(self, list_of_values=[]):
        self.tree = [value for value in list_of_values]

        if len(self.tree) > 0:
            # heapify the received values
            self.build_heap()

    def build_heap(self):
        data = self.tree
        heap_size = len(data)

        i = heap_size // 2
        while i >= 0:
            self.sift_down(i)
            i -= 1

    def sift_down(self, i):
        if i >= 0 and i < len(self.tree):
            data = self.tree
            heap_size = len(data)

            # current node is placed at i index
            left_child_index = i*2 + 1

            right_child_index = i*2 + 2

            _min = data[i].finish_time # suppose the current node is the minimum
            _min_index = i

            if left_child_index < heap_size and data[left_child_index].finish_time < _min:
                _min_index = left_child_index
                _min = data[_min_index].finish_time

            if  right_child_index < heap_size and data[right_child_index].finish_time < _min:
                _min_index = right_child_index
                _min = data[_min_index].finish_time

            if left_child_index < heap_size and data[left_child_index].finish_time == _min:
                _min_index = left_child_index if data[left_child_index].id < data[_min_index].id else _min_index

            if right_child_index < heap_size and data[right_child_index].finish_time == _min:
                _min_index = right_child_index if data[right_child_index].id < data[_min_index].id else _min_index
                

            if _min_index != i:
                self.__swap(i, _min_index)
                self.sift_down(_min_index)
    
    def sift_up(self, i):
        def parent_index(index):
            return (index-1) // 2

        while i > 0 and i < len(self.tree) and (self.tree[i].finish_time < self.tree[parent_index(i)].finish_time or
            self.tree[i].finish_time == self.tree[parent_index(i)].finish_time and self.tree[i].id < self.tree[parent_index(i)].id):
            self.__swap(i, parent_index(i))
            i = parent_index(i)

    def insert(self, value):
        self.tree.append(value)
        last_leaf_index = len(self.tree) - 1
        self.sift_up(last_leaf_index)

    def extract_min(self):
        # swap first
        if len(self.tree) > 0:
            _min = self.tree[0]
            last_leaf_index = len(self.tree) - 1
            self.__swap(0, last_leaf_index)
            self.tree.pop(last_leaf_index)
            if len(self.tree) > 0:
                self.sift_down(0)
            return _min
        
        return None

    def __swap(self, i, j):
        data = self.tree
        temp = data[i]
        data[i] = data[j]
        data[j] = temp

def assign_jobs(n_workers, jobs):
    assigned_jobs = []
    min_heap = MinHeap()
    for n in range(n_workers):
        min_heap.insert(Thread(n, 0))       # T(n) = nlog n

    for i in range(len(jobs)):
        job = jobs[i]
        thread = min_heap.extract_min()
        assigned_jobs.append(AssignedJob(thread.id, thread.finish_time))
        thread.finish_time += job
        min_heap.insert(thread)
    
    return assigned_jobs





def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
