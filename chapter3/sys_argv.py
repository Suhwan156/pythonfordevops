#!/usr/bin/env python3
"""
sys.argv를 사용한 간단한 명령줄 툴
"""
import sys
def say_it(greeting, target):
    message = f'{greeting} {target}'
    print(message)

if __name__ == '__main__':    # 현재 명령줄에서 실행중인지 테스트
    greeting = 'Hello'    # 여기 두 라인에서 기본값 설정
    target = 'Joe'

    if '--help' in sys.argv:    # 인수 목록에 --help 문자열이 있는지 확인
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()    # 도움말 출력 이후 프로그램 종료

    if '--name' in sys.argv:
        #name 플래그 다음의 위치 얻기
        name_index = sys.argv.index('--name') + 1    # 플래그 뒤에 이어지는 값의 위치 파악
        if name_index < len(sys.argv):    # 인수 리스트 길이 테스트, 플래그 뒤에 값이 없다면 길이가 부족한 것으로 나타남
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        #greeting 플래그 다음의 위치 얻기
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)    # 인수에 따라 수정된 값으로 호출


