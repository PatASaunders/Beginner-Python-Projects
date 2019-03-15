import matplotlib.pyplot as plt
while True:
    try:
        start_num = int(input("Please input a starting number to commence the collatz conjecture"))
        if start_num > 1:
            break
    except ValueError:
        continue
steps_int=0
steps=[0]
number=[start_num]
while start_num!=1:
    steps_int=steps_int+1
    if start_num%2==0:
        start_num=start_num/2
    else:
        start_num=(start_num*3)+1
    steps.append(steps_int)
    number.append(start_num)
print(number)
plt.plot(steps, number)
plt.show()