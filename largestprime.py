def isprime(limit):

    for i in range(2,limit):
        # print(i)
        if limit%i==0:
            return False
    return True

def acceptprime(limiting):
    for i in range(2,limiting):
        print("limiting",i)
        if (limiting%i==0):
            if isprime(i):
                print(i)


acceptprime(int(600851475143))
