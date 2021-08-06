# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).


def pronicNumber(n):
    a=0
    for i in range(n):
        if i*(i+1)==n:
            a=1
            break
    return a==1

def nthpronicNumber(n):
    a=0
    count=1
    while(count<=n):
        a+=1
        if(pronicNumber(a)):
            count=count+1
    return a
print(nthpronicNumber(11))
 





























# def pronicnumber(n):
#     a=0
#     for i in range(n):
#         if i *(i+1)==n:
#             a=1
#             break
#     return a==1
 
# def nthpronicnumber(n):
#     found=1
#     guess=0
#     while(found<=n):
#         guess+=1
#         if(pronicnumber(guess)):
#             found+=1
#     return guess
 
# print(nthpronicnumber(1))