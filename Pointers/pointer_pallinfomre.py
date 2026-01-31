value = "m,alaAlam "

start, end = 0, len(value)-1

while start < end:
    while start < end and not value[start].isalpha():
        start +=1
    while start < end and not value[end].isalpha():
        end -=1
    print(f"comparing{value[start], value[end]}")
    if value[start].lower() == value[end].lower():
        start+=1
        end-=1
        print("pallibdrome") # put a flag
        continue
    print("not pallindrome break")
    break
