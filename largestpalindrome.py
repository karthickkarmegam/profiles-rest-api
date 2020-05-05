def reversenumber(value):
    num = 0
    reversig=0
    while value>0:
        reversig = value%10
        num = num*10+reversig
        value =value//10

    return num


def palindrome(value):
    if value==reversenumber(value):
        return True
    return False

def createpalindrome():
    sum=0
    previous=0
    for i in range(1,1000):
        for n in range(1,1000):
            sum = i*n
            if palindrome(sum) and sum>previous:
                previous=sum
                print(sum)

createpalindrome()
