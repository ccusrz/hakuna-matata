#Russian approach of two positive integers product

def rus_mul(a, b, sums):
    if a == 1:
        sums += b
        return sums
    elif a % 2 > 0:
        sums += b
    return rus_mul(a // 2, b * 2, sums)
    
ints = list(map(int, input().split()))
if ints[0] > 0 and ints[1] > 0:
    print(rus_mul(ints[0], ints[1], 0))
else:
    print("0")
