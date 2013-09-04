'''
Algorithms - design and analysis (Stanford), Part II.

Programming Question 1:

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below. 

For this problem, use the same data set as in the previous problem. Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

@author: Renat Alimbekov
'''

f = open('jobs.txt', 'r')
num = int(f.readline().strip())
jobs = []
for l in f:
    l = l.strip().split()
    jobs.append((int(l[0]), int(l[1])))
jobs.sort(key=lambda x:x[0])

def keyfun1(a,b):
    #print (a)
    val1 = a[0] - a[1]
    print (b)
    #val2 = b[0] - b[1]
    #if val1 == val2:
    #    return int(a[0] - b[0])
    #else:
    #    return int(val1 - val2)

def compare(jobs, factor):
    if factor == 'd':
        #print(jobs)
        jobs = sorted(jobs, key=keyfun1, reverse=True)
        #print ("!")
    elif factor == 'r':
        jobs = sorted(jobs, key=lambda x: x[0]/float(x[1]), reverse=True)
    return jobs
    
def ws(jobs):
    val = 0
    acc = 0
    for index, j in enumerate(jobs):
        value = j[0] * (acc+j[1])
        acc += j[1]
        val += value
    return  val


jobs = compare(jobs, 'd')
print (ws(jobs))
jobs = compare(jobs, 'r')
print (ws(jobs))
f.close()
