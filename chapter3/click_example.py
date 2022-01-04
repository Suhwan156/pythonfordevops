#!/usr/bin/env python3
"""
click를 사용한 명령줄 툴
"""
import click

@click.group()    # 다른그룹들과 명령이 위치할 최상의 그룹 만들기
def cli():    # 최상위 그룹 역할을 하는 함수 생성. click.group 메서드가 함수를 그룹으로 변환
    pass

@click.group(help='Ship related commands')    # ships를 보유할 그룹 생성
def ships():
    pass

cli.add_command(ships)    # ships를 최상위 그룹의 명령으로 추가, cli 함수는 이제 add_command 메서드와 한 그룹임

@ships.command(help='Sail a ship')    # ships 그룹에 명령 추가, ships.command는 click.command 대신에 사용됨
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

@ships.command(help='List all of the ships')
def list_ship():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

@cli.command(help='Talk to sailor')    # cli 그룹에 명령 추가
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli()    # 최상위 그룹 호출