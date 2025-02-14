
def romantointeger(s):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res=0
    for i in range(len(s)):
        
        current_value=roman[s[i]]
        if i + 1 < len(s) and current_value < roman[s[i+1]]:
            res -=current_value
        else :
           res+=current_value
    return res

#1994
# 1000 100 1000 10 100 1 5
s = "MCMXCIV"
print(romantointeger(s))
    # if roman[i]<:














# s="MCMXCIV"
# x=0
# while True:
#     if 'IV' in s :
#         x+=4
#         s= s = s.replace("IV",'')
#     elif 'IX' in s:
#         x+=9
#         s= s.replace("IX",'')
#     elif 'XL' in s:     
#         x+=40
#         s = s.replace("XL",'')
#     elif 'XC' in s:
#         x+=90
#         s = s.replace("XC",'')
#     elif 'CD' in s:
#         x+=400
#         s= s.replace("CD",'')
#     elif 'CM' in s:
#         x+=900
#         s= s.replace("CM",'')
#     elif s is not None:
#         for i in s:
#             x+=roman[s]
#             s.replace(i,'')
#             if s is None:
#                 False
#                 break
        

# print(x)
# print(x)
    
# for i in s[1::2]:
    # for i2 in s:
    # for ii in s:
        # print(i2)
        # print(ii)
        # x+=roman[i]
    # y.append(i)

        
    # print(x)
# print(x)
