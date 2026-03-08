def add(*total):
    
    sum = 0
    for n in total:
        sum += n
    return sum

print(add(5, 7, 8, 5, 8))