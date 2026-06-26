#Find largest number without max()
nums=[11,22,33,44]
largest=nums[0]
for i in nums:
    if i < largest:
        largest=i
print(i)
#Count even and odd numbers in a list
nums=[1,2,3,4,5,6,7,8,9,10,11]
even_num=[0]
odd_num=[0]
for i in nums:
    if i%2==0:
        even_num+=1
    else:
        odd_num+=1
print("even-count",even_num)
print("odd-count",odd_num)
#Count vowels in a string
text="magaa velan"
vowels="aeiou"
count=0
for i in text:
    if i in vowels:
        count+=1
print(count)
#Reverse a string
text="homelander"
Rtext=text[::-1]
print(Rtext)
without string
text="buther"
Rtext=""
for i in text:
    Rtext=i+Rtext
print(Rtext)
#Check palindrome string
text=input("")
if text==text[::-1]:
    print("palindrome")
else:
    print("non-palindrome")