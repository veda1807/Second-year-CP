def addDigit(num):
    temp="0"
    sum=0
    for ele in num:
        if(ele.isdigit()):
            temp=temp+ele
        else:
            sum=sum+int(temp)
            temp="0"
    return sum+int(temp)
num=input()
print(addDigit(num))