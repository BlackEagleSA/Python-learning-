# importing libraries
import numpy as np

# importing the data set manually as arrays 
country = np.array(["Great Britain", "China", "Russia", "United States", "Korea", "Japan", "Germany"])
coutrny_code = np.array(["GBR", "CHN", "RUS", "US", "KOR", "JPN", "GER"])
year = np.array([2012,2012,2012,2012,2012,2012,2012])
Gold = np.array([29, 38, 24, 46, 13, 7, 11])
Silver = np.array([17, 28, 25, 28, 8, 14, 11])
Bronze = np.array([19, 22, 32, 29, 7, 17, 14])

high_gold = np.argmax(Gold)
print("Country with highest gold medal is: " + country[high_gold])

twenty = np.where(Gold > 20)

for i in twenty:
    print(country[i])

for i in country:
    j = np.where(country == i)
    sum = Gold[j] + Silver[j] + Bronze[j]
    print(i, int(Gold[j]), int(sum))