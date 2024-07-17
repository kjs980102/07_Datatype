#학점 변환기 함수

def score(x):
    result=""
    if 80<x<=100:
        print('A학점입니다.')
        result='A'
    elif 60<x<=80:
        print('B학점입니다.')
        result='B'
    elif 40<x<=60:
        print('C학점입니다.')
        result='C'
    elif 20<x<=40:
        print('D학점입니다.')
        result='D'
    elif 0<=x<=20:
        print('E학점입니다.')
        result='E'
    else:
        print('다시 입력해주세요.')
    return result
text=int(input('학점을 입력해주세요.:'))
var=score(text)
print(var)