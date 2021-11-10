from random import *
import time as t
from matplotlib import pyplot as plt
import math
words = ["Chaima", "sana", "Mouna", "Sihem", "Najet", "Leila", "programmer"]
word = choice(words)
x = []
y = ["1", "2", "3", "4", "5"]
mistakes = 0
print("This programme will helpe you type faster. ")
for i in range(5):
    t1 = t.localtime().tm_sec
    word_type =input(f"Write {word} : ")
    t2 = t.localtime().tm_sec
    speed = abs(t2 - t1)
    print(f"Speed : {speed}sec")
    x.append(speed)
    if word_type != word.lower():
        mistakes = mistakes + 1


print(f"You made {mistakes} mistake(s) ")
print("Now let's see your evolution !")
t.sleep(3)

plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your typing evolution")
plt.plot(y, x)
plt.show()
