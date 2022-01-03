#!/usr/bin/env python3
"""
argparse를 사용한 명령줄 툴
"""
import argparse

def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maritime control')    # 최상위 레벨 파서 생성

    parser.add_argument('--twice', '-t',
                        help='Do it twice',
                        action='store_true')    # 해당 파서 계층 아래에서 어떠한 명령과도 사용할 수 있는 최상위 인수 추가

    subparsers = parser.add_subparsers(dest='func')    # 서브파서들을 담을 수 있는 객체 생성, dest는 서브파서 선택에 사용될 속성의 이름

    ship_parser = subparsers.add_parser('ships',
                                        help='Ship related commands')    # ships 서브파서 추가
    ship_parser.add_argument('command',
                             choices=['list', 'sail'])    # ships 서브파서 명령 추가, choices 파라미터는 해당 명령에서 선택 가능한 목록

    sailor_parser = subparsers.add_parser('sailors',
                                        help='Talk to sailor')    # sailors 서브파서 추가
    sailor_parser.add_argument('name',
                               help='Sailors name')    # sailors 서브파서에 필요한 위치 인수 추가
    sailor_parser.add_argument('--greeting', '-g',
                               help='Greeting',
                               default='Ahoy there')

    args = parser.parse_args()
    if args.func == 'sailors':    # 어느 서브파서가 func 값 확인에 사용됐는지 체크
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()