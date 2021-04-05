#정수n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오
def print_sum(result):
    count=0
    numbers=list()
    while count<x:
        s=input('정수를 입력하시오: ')
        numbers.append(int(s))
        count+=1
    i=0
    while count<x:
        result+=numbers[i]
        count+=1 
        i+=1  
    return result
x=int(input('정수의 개수를 입력하시오: '))
print_sum(result)