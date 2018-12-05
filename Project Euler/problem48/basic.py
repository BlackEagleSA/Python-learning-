# @Author: Turki A Alrifaie
# @Date:   2018-12-05T10:04:08-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: basic.py
# @Last modified by:   Turki A Alrifaie
# @Last modified time: 2018-12-05T10:59:28-05:00
# @License: Free

"""

Problem Description
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""



def run():
    global ans
    sum = 0
    ans = ""
    for i in range(1, 1000):
        sum = sum + i ** i

    temp = str(sum)

    # start 10 digits before end the end
    end = len(temp)
    start = end - 10

    for i in range(start, end):

        ans = ans + temp[i]

    ans = int(ans)


if __name__ == "__main__":
    run()
    print("The last 10 digits of the series  {0}".format(ans))
