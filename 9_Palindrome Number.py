x=121
x = [i for i in str(x)]
xx=[i for i in x]
pop_backword=[]
frontword=[]

for i in xx:
    pop_backword.append(x.pop())
    frontword.append(i)
    
if pop_backword == frontword:
    print(True)
else:
    print(False)























# x= 1112
# x= 121

# def ax(x):
#     x=str(x)
#     y=[i for i in x]
#     z=[i for i in x[::-1]]
#     if y==z:
#         print('true')
#     else:
#         print('false')
    
        
# ax(x)