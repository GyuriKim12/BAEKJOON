#두 정수 A와 B를 입력받은 다음,A+B를 출력하는 프로그램을 작성하시오
count=0
while count<5:
    a,b=map(int,input().split())
    print(a+b)
    count+=1
print('0 0')

#주어진 숫자가 10보다 작으면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리 숫자를 더한다.
#그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를
#이어 붙이면 새로운 수를 만들 수 있다.
count=0
while True:
    n=int(input())
    a=n//10
    b=n%10
    c=a+b
    str_=int(str(n%10)+str(c%10))
    count+=1
    str_=n
    if n==str_:
        break
print(count)