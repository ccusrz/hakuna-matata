#SPOJ: HS08PAUL (simplified: reduced limits due to poor machine features)

def check(n):
    
    while n > 10000:
        print("n must be < 10000. You've got another chance.")
        n = int(input().strip())
    return n

def operation(n):
    
    count = 0
    for i in range(n):
        if pow(i,2) <= n: 
            for j in range(n):
                if pow(j,4) <= n:
                    operation = pow(i,2) + pow(j,4)
                    if operation > 1 and operation <= n:
                        for z in range(2, operation):
                            if (operation % z) == 0:
                                break
                        else:
                            count += 1
                else:
                    continue
        else:
            continue
    return count
      
def main():

    T = int(input().strip())
    while T > 10000:
        print("T must be ≤ 10000. You've got another chance.")
        T = int(input().strip())

    n_numbers = [check(int(input().strip())) for i in range(T)]
    
    print("")
    for i in n_numbers:
        print(operation(i))

if __name__ == '__main__':
    main()
