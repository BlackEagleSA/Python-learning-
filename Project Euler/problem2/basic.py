# @Author: Turki Alrifaie
# @Date:   2018-11-29T12:58:23-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: basic.py
# @Last modified by:   Turki A Alrifaie
# @Last modified time: 2018-12-03T11:43:13-05:00

def evennumberSum():
    global total
    # Variable inits
    counter = 1 #keeps track of the number we are currently at
    total = 0
    current = 0
    prev = 0
    temp = 0
    #while the count is has not exceeded 4E6
    while (counter <= 4E6):
        #Fibonacci series starts at 1
        #We initialze the next and previous variables and check if the next number is even
        if counter == 1:
            current = counter + 1
            prev = counter
            temp = current #2
        #We have built our base case
        #temp is the sum of the previous and current
        else:
            temp = prev + current
            prev = current
            current = temp
        #check temp to see if it is even
        if temp%2 == 0:
            #inc total when true
            total = total + temp
        #counter is equal to the sum
        counter = total


if __name__ == "__main__":
    evennumberSum() #run the program
    print("The final sum is {0}".format(total))
