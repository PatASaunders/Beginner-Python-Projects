prime=1
non_prime=0
def prime_testing(count,non_prime):
    test=1
    while test <= prime:
        if prime % test != 0:
            test = test+1
        elif test == prime:
            count = count + 1
            print("here is prime number number " + str(count) + ": " + str(prime))
            break
        else:
            non_prime=1
            break
while True:
    if non_prime==0:
        answer = input("Press Enter to generate the next prime number.")
    prime_testing(0,0)
    prime=prime+1