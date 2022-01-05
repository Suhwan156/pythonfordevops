#!/usr/bin/env python3
"""
fire를 사용한 명령줄 툴
"""
import fire
class Ships():    # ship 명령 위한 클래스 정의
    def sail(self):
        ship_name = 'Your Ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Cliper', 'Pequod']
        print(f"Ships: {','.join(ships)}")

def sailors(greeting, name):    # sailors는 하위명령이 없으므로 함수로 정의될 수 있음
    message = f'{greeting} {name}'
    print(message)

class Cli():    # 최상위 그룹 역할을 하는 클래스 정의, 클래스 속성으로 sailors 함수와 ships 추가
    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()

if __name__ == '__main__':
    fire.Fire(Cli)    # 최상위 그룹 역할을 하는 클래스를 fire.Fire로 호출