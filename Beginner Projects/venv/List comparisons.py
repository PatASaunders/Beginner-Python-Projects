#unfinished.
import random
list_1=[]
list_2=[]
for x in range(20):
    list_1.append(random.randint(1,5))
    list_2.append(random.randint(1,5))
print(list_1)
print(list_2)
search=1
new_list=[]
set(list_1) & set(list_2)
print(new_list)