#문자메시지 길이에 따라 문자 요금이 결정되는 프로그램
#메세지의 길이가 20이하이면 50원 20을 초과하면 100원

def find_len(x):
    result=0
    if len(x)<=20:
        print('50원')
        result= 50
    elif len(x)>20:
        print('100원')
        result= 100
    return result
text=input('문자 메시지를 입력해주세요.')
var=find_len(text)
print(var)