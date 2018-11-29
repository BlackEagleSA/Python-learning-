""" This is a refined implementation of project Euler problem number 1 titled Multiples of 3 and 5
The problem has been solved without multi threading where this implementation aims at expanding the auther's knowledge with multi threading aspect

Author: Turki Alrifaie
Created on: 29-11-2018 11:13
"""
import threading
# global variable to save the sum
sum = 0

def sum_function (range_, counter, lock):
    global sum
    #debugging
    #print("args {0} {1}".format(range_, counter))
    while (counter != range_):
        if(counter % 3 == 0 or counter % 5 == 0):
            lock.acquire()
            sum = sum + counter
            lock.release()
        counter += 1

def start_funct(num):
    global ans, sum
    #divide the passed number into 4 and allocate that range to its proper thread
    remainder = 0
    num -= 1
    # check if for remainder and act approprietly
    while (num % 4 != 0):
        num -= 1
        remainder +=1
        #debugging
        #print("find range {0} {1}".format(num, remainder))

    divisor = num / 4
    ranges = [divisor, (divisor * 2), divisor * 4 + remainder]

    lock = threading.Lock()
    # create threads and pass the range of for each thread
    t1 = threading.Thread(target=sum_function, args=(ranges[0], 1, lock))
    t2 = threading.Thread(target=sum_function, args=(ranges[1], ranges[0], lock))
    t3 = threading.Thread(target=sum_function, args=(ranges[2], ranges[1], lock))

    #start the threads
    t1.start()
    t2.start()
    t3.start()

    #wait for threads to finish
    t1.join()
    t2.join()
    t3.join()

    ans = sum

if __name__ == "__main__":
    x = int(input("Enter range: "))
    start_funct(x)
    print("The final sum is {0}".format(ans))
