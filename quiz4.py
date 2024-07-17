# #리스트 변수의 평균 값을 구하는 함수를 작성하시오. 리스트의 길이는 매번 달라집니다.
def list_ave(x):
    result=0
    for i in x:
        result=result+i
    avg=result/len(x)
    return avg
list=[10,5]
var=list_ave(list)
print(var)
