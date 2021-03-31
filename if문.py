#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오
A,B=map(int,input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')

#시험점수를 입력받아 90~100점은 A, 80~89점은 B, 70~79점은 C, 60~69점은 D, 나머지 점수는 F를
#입력하는 프로그램을 작성하시오
test_score=int(input())
if 90<=test_score<=100:
    print('A')
elif 80<=test_score<=89:
    print('B')
elif 70<=test_score<=79:
    print('C')
elif 60<=test_score<=69:
    print('D')
else:
    print('F')

#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오
year=int(input())
if (year%4==0 and year%100!=0):
    print('1')
elif (year%4==0 and year%400==0):
    print('1')
else:
    print('0')

#점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
#단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
x=int(input())
y=int(input())
if x>0 and y>0:
    print('제 1사분면')
elif x>0 and y<0:
    print('제 4사분면')
elif x<0 and y>0:
    print('제 2사분면')
else:
    print('제 3사분면')

#설정되어 있는 알람을 45분 앞서는 시간으로 바꿔 언제로 고쳐야하는지를 구하시오
H,M=map(int,input().split())
if (0<=H<=24 and 45<=M<=60):
    print(H,M-45)
elif (1<=H<=24 and 0<=M<45):
    print(H-1,60-(45-M))
else:
    print('23',60-(45-M))