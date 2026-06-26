#Write a Python program to remove duplicate values from a list.
nums=[1,2,2,2,3,4,5,5]
dup=[]
for i in nums:
    if i not in dup:
        dup.append(i)
print(dup)
#Find the sum of all numbers in a list
nums=[1,2,2,2,3,4,5,5]
total=0
for i in nums:
    total=i+total
print(total)
# Count words in a sentence
text="i am a fresher to this job"
words=text.split()
count=len(words)
print(count)
#Find the factorial of a number
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)
#Check prime number
num = 7 
prime=True
if num <=1:
    prime=False
else:
    for i in range(2,num):
       if num % i == 0:
        prime=False
        break
if prime:
    print("prime")
else:
    print("non-prime")