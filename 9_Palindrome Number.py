# x= 1112
x= 121

def ax(x):
    x=str(x)
    y=[i for i in x]
    z=[i for i in x[::-1]]
    if y==z:
        print('true')
    else:
        print('false')
    
        
ax(x)