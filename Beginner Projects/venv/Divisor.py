while True:
    try:
        divided = int(input("Please enter a number between 1 and 100"))
        if 0<divided<=100:
            break
    except ValueError:
        continue
x = 101
divisors=[]
while x!=1:
    x=x-1
    if divided%x==0:
        divisors.append(x)
    else:
        continue
print(divisors)