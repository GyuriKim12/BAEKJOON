#수 정렬하기
# n=int(input())
# List=[]
# for i in range(5):
#     a=int(input())
#     List.append(a)
# List.sort()
# for i in List:
#     print(i)

#소트인사이드
# n=input()
# num=list(n)
# num.sort()
# for i in num:
#     print(i,end="")
# print()

#수 정렬하기2
# n=int(input())
# List=[]
# for i in range(n):
#     List.append(int(input()))
# List.sort()
# for i in List:
#     print(i)

#좌표 정렬하기
# def addList():
#     cd=[]
#     x,y=map(int,input().split())
#     cd.append(x)
#     cd.append(y)

#     return cd
# def makeList(n):
#     List=[]
#     for i in range(n):
#         List.append(addList())
    
    
#     return List

# def listSort(x):
#     for i in range(1,len(x)):
#         j=i
#         while j>0 and x[j-1][0]>=x[j][0]:
#             x[j-1],x[j]=x[j],x[j-1]
#             if x[j-1][0]==x[j][0]:
#                 if x[j-1][1]>x[j][1]:
#                     x[j-1],x[j]=x[j],x[j-1]
#                 else:
#                     x[j-1],x[j]=x[j-1],x[j]
#             j-=1
            
#     return x 

# n=int(input())
# x=makeList(n)
# y=listSort(x)
# for i in y:
#     for j in i:
#         print(j,end=" ")
#     print()

#좌표 정렬하기2
# def addList():
#     cd=[]
#     x,y=map(int,input().split())
#     cd.append(x)
#     cd.append(y)

#     return cd
# def makeList(n):
#     List=[]
#     for i in range(n):
#         List.append(addList())
    
    
#     return List

# def listSort(x):
#     for i in range(1,len(x)):
#         j=i
#         while j>0 and x[j-1][1]>=x[j][1]:
#             x[j-1],x[j]=x[j],x[j-1]
#             if x[j-1][1]==x[j][1]:
#                 if x[j-1][0]>x[j][0]:
#                     x[j-1],x[j]=x[j],x[j-1]
#                 else:
#                     x[j-1],x[j]=x[j-1],x[j]
#             j-=1
            
#     return x 

# n=int(input())
# x=makeList(n)
# y=listSort(x)
# for i in y:
#     for j in i:
#         print(j,end=" ")
#     print()

#나이순 정렬
# def addList():
#     cd=[]
#     x,y=input().split()
#     x=int(x)
#     cd.append(x)
#     cd.append(y)

#     return cd
# def makeList(n):
#     List=[]
#     for i in range(n):
#         List.append(addList())
    
    
#     return List

# def listSort(x):
#     for i in range(1,len(x)):
#         j=i
#         while j>0 and x[j-1][0]>=x[j][0]:
#             x[j-1],x[j]=x[j],x[j-1]
#             if x[j-1][0]==x[j][0]:
#                 x[j-1],x[j]=x[j-1],x[j]
#             j-=1
            
#     return x 

# n=int(input())
# x=makeList(n)
# y=listSort(x)
# i=0
# while i<len(y):
#     print(y[i][0],end=" ")
#     print(y[i][1])
#     i+=1
# print()

#국영수
def addList():
    cd=[]
    x,y,z,w=input().split()
    y,z,w=int(y),int(z),int(w)
    cd.append(x)
    cd.append(y)
    cd.append(z)
    cd.append(w)

    return cd

def makeList(n):
    List=[]
    for i in range(n):
        List.append(addList())
    
    
    return List

def listSort(x):
    List=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','w','y','z']
    for i in range(1,len(x)):
        j=i
        while j>0 and x[j-1][1]>=x[j][1]:
            x[j-1],x[j]=x[j-1],x[j]
                
            if x[j-1][1]==x[j][1]:
                if x[j-1][2]>x[j][2]: 
                    x[j-1],x[j]=x[j],x[j-1]
                    
                if x[j-1][2]<x[j][2]:
                    x[j-1],x[j]=x[j-1],x[j]
                    
                if x[j-1][2]==x[j][2]:
                    if x[j-1][3]>x[j][3]:
                        x[j-1],x[j]=x[j-1],x[j]
                        
                    if x[j-1][3]<x[j][3]:
                        x[j-1],x[j]=x[j],x[j-1]
                        
                    if x[j-1][3]==x[j][3]:
                        a=islow(x[j-1][0])
                        b=islow(x[j][0])
                        for i in range(len(List)):
                            if List[i]==a[0]:
                                a=int(List.index(List[i]))
                            else:
                                pass
                        for i in range(len(List)):
                            if List[i]==b[0]:
                                b=int(List.index(List[i]))
                            else:
                                pass
                        if a>b:
                            x[j-1],x[j]=x[j],x[j-1]
                        else:
                            x[j-1],x[j]=x[j-1],x[j]
            j-=1
            
    return x 


def islow(s):
    s=s.lower()
    ans=''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans+=c
    return ans
    
n=int(input())
x=makeList(n)
y=listSort(x)
for i in range(len(y)):
    print(y[i][0])

#수 정렬하기3
# def addList(n):
#     List=[]
#     for i in range(n):
#         a=int(input())
#         List.append(a)
        
#     return List

# def listSort(x):
#     for i in range(1,len(x)):
#         j=i
#         while j>0 and x[j-1]>x[j]:
#             x[j-1],x[j]=x[j],x[j-1]
#             j-=1   
#     return x

# n=int(input())
# x=addList(n)
# y=listSort(x)
# for i in y:
#     print(i)

#카드
# n=int(input())
# List=[]
# for i in range(n):
#     a=int(input())
#     List.append(a)

# count={}
# for i in List:
#     try:
#         count[i]+=1
#     except:
#         count[i]=1

# def my_max():
#     i=0
#     a=count[List[0]]
#     num=List[0]
#     while i<len(List):
#         if a<count[List[i]]:
#             a=count[List[i]]
#             num=List[i]
#         i+=1
#     return num

# print(my_max())

#k번째 수
# n,k=map(int,input().split())
# nums=list(map(int,input().split()))
# nums.sort()
# print(nums[k-1])