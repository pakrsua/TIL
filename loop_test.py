number = [5,6,9,10,15,457]

for i in number:
    print(i)

for i in range(len(number)):
    print(number[i])

print(range(len(number)))
print(list(range(len(number))))

#range(끝값+1)
#range(시작값, 끝값+1)
#range(시작값, 끝값+1,step)