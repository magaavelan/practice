#Find the second largest number in a list (without sort())
# num=[1,2,33,44,5,6,7,8]
# lar=num[0]
# sec=num[0]
# for i in num:
#     if i > lar:
#         sec = lar
#         lar = i
#     elif i > sec and i != sec:
#         sec = i
# print(lar)
# print(sec)
##Find frequency of each character in a string.
# text="magaavelan"
# f={}
# for i in text:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(f)
## Check whether two strings are anagrams.
str1="listen"
str2="slient"
if sorted(str1)==sorted(str2):
    print("anagrams")
else:
    print("n-anagrams")
##Find the Intersection of Two Lists
list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print(common)
##Merge two lists without duplicates
list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8]
merge=[]
for i in list1:
    if i not in merge:
        merge.append(i)
for i in list2:
    if i not in merge:
        merge.append(i)
print(merge)
##Find common elements without duplicates
list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8]
common=[]
for i in list1:
    if i in list2 and common not in list2:
        common.append(i)
print(common)
