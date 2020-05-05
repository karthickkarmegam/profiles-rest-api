def prime_factor():
    prime_number = 20
    list_of_list_of_pimenumber = []
    for i in range(2,prime_number+1):

        list_of_prime = []
        potential_number =2
        while i>1:
            if i%potential_number==0:
                list_of_prime.append(potential_number)
                i = i/potential_number
            else:
                potential_number +=1
        list_of_list_of_pimenumber.append(list_of_prime)
    print(list_of_list_of_pimenumber)

    prime_single =[]
    for primes in list_of_list_of_pimenumber:
        for prime in primes:
            if prime not in prime_single:
                prime_single.append(prime)
    print(prime_single)
    answer =1

    for prime in prime_single:
        maxcount = 0
        for primes in list_of_list_of_pimenumber:
            count = 0
            for i in primes:
               if i==prime:
                   count +=1
            if count >maxcount:
                maxcount = count
        answer *= prime ** maxcount
    print(answer)

prime_factor()