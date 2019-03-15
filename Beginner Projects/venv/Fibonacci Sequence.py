while True:
    try:
        repetitions = int(input("Please enter a number n to generate the Fibonacci for n terms"))
        if 0 <= repetitions <= 17:
            break
    except ValueError:
        continue
term_1=0
term_2=1
turns=0
fib_seq=[]
fib_seq.append(term_1)
fib_seq.append(term_2)
while True:
    turns=turns+1
    term_1=term_1+term_2
    fib_seq.append(term_1)
    print(fib_seq)
    if turns==repetitions:
        break
    turns = turns + 1
    term_2=term_1+term_2
    fib_seq.append(term_2)
    print(fib_seq)
    if turns==repetitions:
        break