#n이 주어졌을 때, 1부터n까지 합을 구하는 프로그램을 작성하시오
n=int(input('Input an integer: '))
1<=n<=100
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.     
testcase=int(input())
for i in range(testcase):
    a,b=map(int,input('숫자 2개를 띄어쓰기 기준으로 입력하시오: ').split())
    print(a+b)

#첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
n=int(input())
for i in range(1,n+1):
    print(i)

#첫번째 줄부터 N번째 줄 까지 차례대로 출력한다.
n=int(input())
for i in range(n,0,-1):
    print(i)

#각 테스트 케이스마다 Case #x:를 출력한 다음, A+B를 출력한다.
n=int(input()) 
for i in range(1,n+1):
    a,b=map(int,input('숫자 2개를 띄어쓰기 기준으로 입력하시오: ').split())
    print('case #'+str(i)+':',a+b)

#각 테스트 케이스마다 Case #x:A+B=C 형시으로 출력한다.
n=int(input())
for x in range(1,n+1):
    a,b=map(int,input('숫자 2개를 띄어쓰기 기준으로 입력하시오: ').split())
    print('Case #'+str(x)+':',str(a)+' + '+str(b)+' =',a+b)

#첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
n=int(input())
for i in range(1,n+1):
    print('*'*i)

#첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
n=int(input())
for i in range(1,n+1):
    print((' '*(n-i))+(i*'*'))

#x보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.
#x보다 작은 수는 적어도 하나 존재한다.

x=int(int(input('x=')))
n=int(input())
numbers=[]
for i in range(n):
    s=input()
    numbers.append(int(s))
for i in numbers:
    if i<x:
        print(i)

x,count=map(int,input().split())
numbers=list(map(int,input().split()))
for i in range(count):
    if numbers[i]<x:
        print(numbers[i],end=' ')