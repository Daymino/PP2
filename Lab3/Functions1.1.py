#Exercise 1

def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

grams = float(input())
print(grams_to_ounces(grams))