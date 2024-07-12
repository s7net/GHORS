ending = lambda: input("\n\nPress Any key to exit app ...")

times = input("please input times (enter for ending) : ")
times = [i for i in times.split(" ") if bool(i) == True]
sum_min = 0
sum_sec = 0
for i in range(len(times)):
    temp = times[i].split(":")
    sum_min += int(temp[0])
    sum_sec += int(temp[1])

sum_min += sum_sec // 60
sum_sec = sum_sec % 60
sum_hou = sum_min // 60
sum_min = sum_min % 60
print(f"\n \nsum of times : {sum_hou}:{sum_min}:{sum_sec}")
ending()
