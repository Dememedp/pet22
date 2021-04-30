print("input your string")
word = input()
length = len(word) - 1
i=0
flag = True
while i<length:
    if (word[i] == word[length]): 
        length -=1
        i +=1
    else:
        print("not a polymdrome")
        flag = False
        break
if flag:
    print("is a polyndrome")