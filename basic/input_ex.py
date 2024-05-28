'''
* 표준 입력함수 input()
- 함수 괄호 안에 사용자에게 질문할 내용을 문자열 형태로
작성합니다.
- input()과 함께 항상 변수를 선언해서 입력값을 받아주셔야 하며
입력받은 데이터의 타입은 str로 리턴됩니다.
'''

nick = input('별명 : ')
print(nick, 'ㅎㅇ')

# 입력값이 정수, 실수라면
# input 함수 자체를 int(), float() 함수로 감싸주면 된다
# 리턴된 문자열 입력값을 해당 타입으로 변환하는 내장 함수
price = int(input('가격 : '))
people = int(input('인원수 : '))

print('지불할 가격 : ', price*people, '원')