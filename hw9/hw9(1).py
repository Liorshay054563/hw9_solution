# start
from os import remove

temps: list[float] = []


while True:
    temp: float = float(input('Enter temperature:'))
    if temp == -999:
        break
    if not -50 < temp < 50:
        continue
    temps.append(temp)
temps.extend([-20, 39.1 ,18.5])
# "+" --- only show the list with the new list, without change or save nothing// "extend" whoever save the new list
# - but not giving feedback
print(f"the highest temp is {max(temps)}")
print(f"the lowest temp is {min(temps)}")
if 18.5 in temps:
    print("True")
else:
    print("false")
temps.count(-20)
print(f"the average is {sum(temps) /len(temps)}")
for temp in temps:
    print(temp, end="")
    print()
print(temps.index(39.1))
print(temps)
del temps[0]
del temps [:2]
if 18.5 in temps:
    temps.remove(18.5) # you need allways to check it because if not the code get error
temp_last = temps.pop()
copy_list = temps.copy()
copy_list.sort()
print(copy_list)
reverse_list = copy_list.sort(reverse=True)
print(reverse_list)
print(temps)
