s="()[]{}"
validation={')':'(','}':'{',']':'['}
s=list(s)
for _ in s:
    current_val= s.pop()
    if validation[current_val] in s:
        s.remove(validation[current_val])
        print('True')
    else :
        print('False')
    


# for _ in s:
#     current_val= s.pop()
#     if validation.get(current_val) is None :
#         print('false')
#         break
    
#     elif s_res.index(current_val)<s_res.index(validation.get(current_val)):
#         print('false')
#         break
#     else :
#         print('true')
#         break
        


# None

# if not validation.get(key):
#     false  