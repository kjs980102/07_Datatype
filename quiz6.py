#판매가가 저장된 리스트가 있을 때 부가세가 포홤된 가격을 리스트로 반환하는 함수를 작성하시오.
def vat(x):
    result_list = []
    result = 0
    for a in x:
        result=int(a*1.1)
        result_list.append(result)
    return result_list

numbers=[100,200,300]
print(vat(numbers))


