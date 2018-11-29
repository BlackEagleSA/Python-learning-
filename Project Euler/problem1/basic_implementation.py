# @Author: Turki Alrifaie
# @Date:   2018-11-29T13:02:17-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: basic_implementation.py
# @Last modified by:   Turki Alrifaie
# @Last modified time: 2018-11-29T13:16:05-05:00

"""
This is a simple and quick implementation to find the solution for problem 1 in project Euler
"""

def find_sum(num):
    global ans
    i = 1
    ans = 0
    while ( i < num):
        if(i%3==0 or i%5 ==0):
            ans = ans + i
        i +=1

if __name__ == "__main__":
    x = int(input("Enter range: "))
    find_sum(x)
    print("The final sum is {0}".format(ans))
