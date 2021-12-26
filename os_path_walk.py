#!/usr/bin/env python

# 대용량 파일이나 사용하지 않는 파일을 식별 가능

import fire
import os

def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)    # os.listdir은 디렉터리 내에 있는 항목들을 반환

    for child in childs:
        child_path = os.path.join(parent_path, child)    # 각 항목을 상위 디렉터리를 포함하는 전체 경로로 구성
        if os.path.isfile(child_path):    # 해당 경로의 항목이 파일인지 확인
            last_access = os.path.getatime(child_path)    # 파일의 마지막 접근시간
            size = os.path.getsize(child_path)    # 파일의 크기
            print(f"File: {child_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
        elif os.path.isdir(child_path):    # 해당 경로의 항목이 디렉터리인지 확인
            walk_path(child_path)    # 해당 디렉터리의 하위 트리 확인

# 위 함수 원리에서 os.walk 이용
def walk_new_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)  # 파일의 마지막 접근시간
            size = os.path.getsize(file_path)  # 파일의 크기
            print(f"File: {file_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")



if __name__ = '__main__':
    fire.Fire()