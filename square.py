def list_of_prime():
    list = []
    number_range =2000000
    x=2
    while len(list)<number_range:
        if all(x%prime for prime in list):
            list.append(x)
        x+=1
    print(list)

list_of_prime()