import random

print(random.random())  # generates random number between 0-1
# OUTPUT: 0.626077867208037

# randint(a,b) -> Return random integer in range [a, b]
print(random.randint(0, 23))
# OUTPUT: 17

#! Generating a List of numbers Using For Loop
randomList = []

for x in range(0, 46):  # range(start, stop, step)
    n = random.randint(1, 346579347596)
    randomList.append(n)

print(sum(randomList))
