import random, math

def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

allGeneratedPairs = 0
comprimeNumbers = 0

for i in range(10000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    
    if NWD(a, b) == 1:
        allGeneratedPairs += 1
        comprimeNumbers += 1
    else:
        allGeneratedPairs += 1

cesaroTheorem = comprimeNumbers/allGeneratedPairs
print(f"Approximate value of pi is: {math.sqrt(6/cesaroTheorem)}")
