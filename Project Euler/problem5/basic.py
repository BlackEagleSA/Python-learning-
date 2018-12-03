# @Author: Turki A Alrifaie
# @Date:   2018-12-03T11:38:21-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: basic.py
# @Last modified by:   Turki A Alrifaie
# @Last modified time: 2018-12-03T13:11:28-05:00
# @License: Free

"""
    Brute force method. The program need around 7 seconds to find the solution
"""


def run():
    global ans
    #var declaration
    notfound = 1 #flag
    num = 20 # we ignore the first 19 numbers because there is not a number that is evenly divisble by range 1:20

    while(notfound):
        #print("outside for at num {0}".format(num))
        for i in range (1, 20):
            #print("inside for {0}".format(i))
            if num % i != 0:
                #print("broke on {0}".format(i))
                num += 20
                break
        else:
            notfound = 0
    ans = num



if __name__ == "__main__":
    run()
    print("The largest number is {0}".format(ans))
