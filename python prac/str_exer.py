str1 = "baby eunbin"
print(str1[-6:8])

#출력문 안에 기호를 넣는 방법
print("hello 'world'")
print('hello "world"')
print("hello \"world\"")
print("""hello "world" """)

#raw string(\를 그냥 문자로 인식)
print(r"/Users/jun/Documents/git_file/ktcloud_genai/python prac/str_exer.py") #현재 소스코드의 경로

#멀티라인-1
str2 = """
안녕하세여
멀티라인이 잘 테스트 되는지 
살펴보는 중입니다.
"""
print(str2)
#멀티라인-2(깔끔하게 적고 싶을 때)
str3 = \
"""
줄바꿈도 잘 되는지

테스트해보는 중입니다.
"""
print(str3)

#문자열 인덱싱 및 슬라이싱
str4 = "KTcloud_techup"
print(str4[7]) #문자열은 리스트 형태로써 인덱스 번호로 호출 가능
print(str4[3:9]) #인덱싱 번호를 통해 슬라이싱 가능
print(str4[3:-5]) #음수 인덱싱도 가능(역순으로 뒤에서부터 셈)
print(str4[::2]) #step 기능을 사용할 수 있음(2칸씩 건너뛰기)
print(str4[::-1]) #문자열 뒤집기

#문자열 연산
str5 = "extensions"
str6 = "curl"

print(str5 + str6) #문자열 더하기
print(str5 * 3) #문자열 곱하기
print("leg" in str6) #문자열 포함 여부 확인(True/False)
print(len(str6)) #문자열 길이 확인

#다양한 문자열 함수
str7 = "python programming"
print(str7.upper()) #모두 대문자로 변환
print(str7.lower()) #모두 소문자로 변환
print(str7.title()) #각 단어의 첫 글자만 대문자로 변환
print(str7.split('p')) #특정 문자를 기준으로 문자열 나누기(리스트 형태로 반환)

str8 = "010-1234-5678"
print(str8.replace('-', '.')) #특정 문자 바꾸기

