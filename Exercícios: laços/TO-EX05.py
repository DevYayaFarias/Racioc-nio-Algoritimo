popuA = 5000000
popuB = 7000000
anos = 0

while popuA <= popuB:
    popuA *= 1.03
    popuB *= 1.02
    anos += 1

print(f"Anos necessários: {anos}")
