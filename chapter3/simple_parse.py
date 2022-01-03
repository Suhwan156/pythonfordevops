#!/usr/bin/env python3
"""
argparse를 사용한 명령줄 툴
"""
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input')    # 메시지와 함께 파서 객체 생성
    parser.add_argument('message',
                        help='Message to echo')    # 도움말 메시지와 위치 기반 명령 추가

    parser.add_argument('--twice', '-t',
                        help='Do it twice',
                        action='store_true')    # 옵션 인수 추가, 옵션 인수에 불린값 저장

    args = parser.parse_args()    # 파서를 사용한 인수 파싱

    print(args.message)
    if args.twice:
        print(args.message)