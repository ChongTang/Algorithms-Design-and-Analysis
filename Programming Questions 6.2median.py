'''
Programming Questions 6.2:

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 5 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.

@author: Renat Alimbekov
'''

import heapq

heap_low = None
heap_high = None
y = 0

def MedianMaintenance_init():
    
    global heap_low, heap_high
    
    heap_low = []
    heap_high = []
    
    
def MedianMaintenance_insert(x):
    
    global heap_low, heap_high,y
    
 
    if (len(heap_low) == 0):
        heapq.heappush(heap_low, -x)
    else:
        m = -heap_low[0]
        if x > m:
            heapq.heappush(heap_high, x)
            if len(heap_high) > len(heap_low):
                y = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -y)
        else:
            heapq.heappush(heap_low, -x)
            if len(heap_low) - len(heap_high) > 1:
                y = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, y)
    
    return -heap_low[0]


def test():
    
    data = [1,5,2,4,3]
    
    MedianMaintenance_init()
    
    for x in data:
        print(MedianMaintenance_insert(x))
        

def main():
    
    lines = open('Median.txt').read().splitlines()
    data = map(lambda x: int(x), lines)
    medians = []
    
    MedianMaintenance_init()
    
    for x in data:
        median = MedianMaintenance_insert(x)
        medians.append(median)
    print(reduce(lambda x,y: (x) % 10000, medians))


if __name__ == '__main__':
    main()
    

