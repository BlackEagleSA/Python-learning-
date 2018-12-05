# @Author: Turki A Alrifaie
# @Date:   2018-12-05T10:04:18-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: threded.py
# @Last modified by:   Turki A Alrifaie
# @Last modified time: 2018-12-05T10:59:27-05:00
# @License: Free


import threading


def series(start, end, lock):
    global sum
    for i in range(start, end):
        lock.acquire()
        sum = sum + i ** i
        lock.release()

def run():
    global ans, sum
    ans = ""
    sum = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=series, args = (1,250, lock))
    t2 = threading.Thread(target=series, args = (251, 500, lock))
    t3 = threading.Thread(target=series, args = (501,750, lock))
    t4 = threading.Thread(target=series, args = (751,1000, lock))

    #Start threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    #Finished threads
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    temp = str(sum)

    end = len(temp)
    start = end - 10

    for i in range(start, end):
        ans = ans + temp[i]
        
    ans = int(ans)

if __name__ == "__main__":
    run()
    print("The last 10 digits of the series  {0}".format(ans))
