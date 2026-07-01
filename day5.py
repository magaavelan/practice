##Reverse a Number using function
# def reverse_number(num):
#     rev=0
#     while num > 0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     print(rev)
# reverse_number(123456)
##Palindrome Number using function
# def palindrome(num):
#     original=num
#     rev=0
#     while num > 0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     if original == rev:
#         print("palindrome")
#     else:
#         print("non-palindrome")
# palindrome(121)
##leapyear
# def leapyear(n):
#     if n%400 == 0:
#         print("leapyear")
#     elif n%4 == 0:
#         print("leapyear")
#     elif n%100 == 0:
#         print("its not a leap year")
#     else:
#         print("its not a leap year")
# leapyear(2024)
##Swap Two Numbers using function
# def swap(a,b):
#     print("before swapping")
#     print(a)
#     print(b)

#     temp=a
#     a=b
#     b=temp

#     print("a:",a)
#     print("b:",b)
# swap(1,2)
##Find Smallest Number in a List without min()
# def smallnumber(n):
#     small=n[0]
#     for i in n:
#         if i < small:
#             small=i
#     print(small)
# smallnumber([1,2,3,4,5,6,7,8])
##Linear Search using function
# def linear_search(n,target):
#     for i in n:
#         if i == target:
#             print("found")
#             return
#     print("not found")
# linear_search([1,2,3,4,5,6,7,8],(4))
## Bubble Sort using function
# def bubblesort(nums):
#     n=len(nums)
#     for i in range(n):
#         for j in range(n-1):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#     print(nums)
# bubblesort([1,2,3,8,7,6,5,4,3,6,3])