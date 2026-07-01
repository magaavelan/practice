#Fibonacci Series
# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         c=a+b
#         a=b
#         b=c
# fibonacci(10)
##armstrong number
# def armstrong(num):
#     temp=num
#     total=0

#     while temp > 0:
#         digits=temp%10
#         total=total+digits**3
#         temp=temp//10
#     if total == num:
#         print("armstrong")
#     else:
#         print("not-armstrong")
# armstrong(153)
##
# def perfect_number(num):
#     total=0
#     for i in range (1,num):
#         if num % i == 0:
#             total=total+i
#     if num == total:
#         print("perfectnumber")
#     else:
#         print("non_perfectnumer")
# perfect_number(6)
##Count Digits in a Number
# def count_numbers(num):
#     count=0
#     while num > 0:
#         count+=1
#         num=num//10
#     print(count)
# count_numbers(123456)
##Sum of Digits using function
# def sum(num):
#     total=0
#     while num > 0:
#         digit=num%10
#         total=total+digit
#         num=num//10
#     print(total)
# sum(1234567890)
