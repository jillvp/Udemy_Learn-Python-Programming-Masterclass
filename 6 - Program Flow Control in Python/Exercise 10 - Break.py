# Coding Exercise 10 - Break

# Modify the code inside this loop to stop when i is exactly divisible by 11

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
