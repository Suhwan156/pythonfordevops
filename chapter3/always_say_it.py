"""
셸 스크립트를 실행 가능하게 만들기
파일의 맨 위에 #!/usr/bin/env python 한줄 넣어주면 명령줄에서 python을 명시적으로 호출하지 않고
스크립트를 실행할 수 있음
"""
#!/usr/bin/env python

def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message = f'{greeting} {target}'
    print(message)

if __name__ == '__main__':
    say_it()

""" 그런 다음 chmod를 사용하여 파일 실행 권한 부여함

$ chmod +x say_it.py`
$ ./say_it.py

Hello Joe
"""