#홀수 짝수 판별기

def ppp(x):
    result=""
    if x%2==0:
        print('짝수입니다.')
        result='짝수'
    else :
        print('홀수입니다.')
        result='홀수'
    return result
num=int(input('숫자를 입력하세요:'))
v=ppp(num)
print(v)