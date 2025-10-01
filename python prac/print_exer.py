int_var = 10
float_var = 20.5
str_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]

#1번 방법 그냥 선언하기
print("Integer Variable:", int_var)
print(int_var, type(int_var))
print(int_var, str_var)

#2번 방법 str.format() 메서드 선언하기
print("{}" .format(int_var))
print("숫자야 나와라 얍 : {}" .format(int_var))
print("숫자야 나와라 얍 : {n}".format(n = int_var))

#3번 방법 %d, %f, %s 선언하기 - 구식
print("%d" % int_var)
print("숫자야 나와라 얍 : %d" % int_var)

#4번 방법 f-string 선언하기 - ver.3.6 이상
print(f"{int_var}")
print(f"숫자야 나와라 얍 : {int_var}")

#5번 방법 f-string debug 표현(변수의 이름과 값을 함께 출력하고 싶을 때) - ver.3.8 이상
print(f"숫자야 나와라 얍 : {int_var=}")

#print sep
print(str_var, list_var, sep = "||")

#print end - 끝에 올 문자나 명령(없을 땐 \n)
print(str_var, end = "???")
print(list_var)
