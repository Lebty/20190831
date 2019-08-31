#dictionary.py

#중괄호를 이용하여 딕셔너리를 생성할 수 있다.
#각 쌍의 키와 값 사이에 콜론(:)을 사용한다.
#len() 함수는 딕셔너리에 있는 키-값 쌍의 수를 센다.
dic1={'one':1,'two':2,'three':3}
dic2={3:'red',4:'green',5:'blue'}
print(dic1)
print(dic2)
print("dic1 has {!s} elements".format(len(dic1)))
print(dic1['one'])
print(dic2[3])