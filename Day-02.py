# Bit wise manipulation 
# xor = 0
# for i in range(10):
#     xor ^= i
# print(xor)

# def xoring(num):
#     if num % 4 == 0:
#         return num
#     elif num%4 ==1:
#         return 1
#     elif num%4 == 2:
#         return num + 1
#     else:
#         return 0
     
# # to find xor betweeen 5^.....^10
# m = 3
# n = 10
# print(xoring(n) ^ xoring(m-1))

#method 01

# m = int(input())
# for i in range(32):
#     if (1 << i) == m: 
#         print("yes")
#         break
# else:print("no")

#method 02
# print((m & (m-1)) == 0)

# #method 03
# while m != 1:
#     if m/2 != m//2:
#         break
#     m//=2
# if m == 1: print("yes")
# else: print("No")
# nums1 = [2,2,4,4,6,6,7, 8,8,9,9]
# left = 0
# right = len(nums1)-1

# while left < right:
#     mid = left + ((right - left) >> 1)
#     if nums1[mid-1] != nums1[mid] != nums1[mid+1]:
#         break
#     elif mid > 0 and nums1[mid] == nums1[mid-1] and mid & 1:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(nums1[mid])


# FRinfin
# while left < right:
#     mid = left + (right - left) >> 1
#     if mid & 1:
#         mid -=1
#     if nums1[mid] == nums1[mid+1]:
#         left = mid+2
#     else:
#         right = mid
# print(left) 
        
        
# maxi = 1
# nums1 = [2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
# # nums1=[1,2,3,2,3,4,5,6,7,8,9]
# left = 0
# for right in range(1,len(nums1)):
#     if nums1[right-1] + 1 != nums1[right]:
#         maxi= max(maxi,right-left)
#         left = right
# maxi= max(maxi, len(nums1) - left)# one of the edges case here must be careful 
# print(maxi)

# string = "aaabbaaaacccddeff"
# string="abbacbababc"
# left = 0
# for right in range(1,len(string)):
#     if string[right] != string[right-1]:
#         print(string[right-1],right-left,end=" ")
#         left = right
# print(string[right],len(string)-left,end=" ")
        
        
    
            
    
        

        
        
        
    
    

        
