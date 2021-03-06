"""
ㅇ 런타임에 애플리케이션 설정 위해 파일 사용하는 것은 일반적인 관행임
ㅇ 유닉스 계열 시스템에서 파일들은 규약에 따라 rc로 끝나느 도트 파일로 이름 정해짐
ex) vim - vimrc, bash - .bashrc
ㅇ 이 파일들은 각기 다른 위치에 저장할 수 있는데, 보통 프로그램에 이 파일을 확인할 위치의 순서가 정의되어 있음
"""
import pathlib

"""
아래 예시는 같은 위치에서 rc파일을 찾기 위해 시도하는 것을 보여줌
ㅇ 파일에서 파이썬 코드를 실행할 때 파이썬이 자동으로 설정하는 file 변수 사용
ㅇ 이 변수는 절대 경로 또는 전체 경로가 아닌 현재 작업중인 디렉터리의 상대 경로에 위치함
ㅇ 파이썬은 유닉스 계열의 시스템처럼 경로를 자동 확장해주지 않으므로 rc파일을 확인할 경로를 구성하기 전에 해당 경로 확장해야 함
ㅇ 마찬가지로 파이썬은 경로에서 환경 변수를 자동으로 확장하지 않으므로 이를 명시적 확장해줘야함
"""

import os
from pathlib import Path

def find_rc(rc_name=".examplerc"):
    #Env 변수 확인
    var_name = "EXAMPLERC_DIR"
    if var_name in os.environ:    # 해당 환경 변수가 존재하는지 확인
        var_path = os.path.join(f"${var_name}", rc_name)    # join을 사용해 $EXAMPLERC_DIR/.examplerc와 같은 형태가 되도록 구성
        config_path = os.path.expandvars(var_path)    # 경로에 해당 값이 포함되도록 환경 변수 확장
        print(f"Checking {config_path}")
        if os.path.exists(config_path):    # 파일 존재 여부 확인
            return config_path

    # 현재 작업중인 디렉터리 확인
    config_path = os.path.join(os.getcwd(), rc_name)    # 현재 작업중인 디렉터리를 활용해 경로 구성
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    #사용자 홈 디렉터리 확인
    home_dir = os.path.expanduser("~/")    # expanduser 통해 홈 디렉터리 구하기
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # 이 파일의 디렉터리 확인
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.pathjoin(parent_path, rc_name)
    print(f"checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")

# os.path 대신 pathlib 사용
def findpathlib_rc(rc_name=".examplerc"):

    # Env 변수 확인
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)    # 이 위치까지는 pathlib가 환경변수를 확장하지 않은 상태, 대신 os.environ으로 변수 값 구함
    if example_dir:
        dir_path = pathlib.Path(example_dir)    # 이 부분에서 현재 실행중인 OS에 맞는 pathlib.Path 객체 생성
        config_path = dir_path / rc_name    # 상위 경로와 슬래쉬, 문자열로 새로운 pathlib.Path 객체 생성
        print(f"Checking {config_path}")
        if config_path.exists():    # pathlib.Path 객체에는 자체적으로 exists 메서드가 있음
            return config_path.as_postix()    # as_postix를 호출해 경로를 문자열로 반환하며, 경우에 따라 pathlib.Path 객체 자체를 반환할 수도 있음

    # 현재 작업중인 디렉터리 확인
    config_path = pathlib.Path.cwd() / rc_name    # 클래스 메서드인 pathlib.Path.cwd는 현재 작업중인 디렉터리의 pathlib.Path 객체를 반환, 이 객체는 문자열 rc_name과 합쳐져 config_path 생성
    print(f"Checking{config_path}")
    if config_path.exists():
        return config_path.as_postix()

    # 사용자 홈 디렉터리 확인
    config_path = pathlib.Path.home() / rc_name    # 클래스 메서드인 pathlib.Path.home은 현재 사용자의 홈 디렉터리의 pathlib.Path 객체 반환
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_postix()

    # 이 파일의 디렉터리 확인
    file_path = pathlib.Path(__file__).resolve()    # file에 저장된 상대 경로를 사용해 pathlib.Path객체 생성하고, 해당 객체의 절대 경로를 구하기 위해 resolve 메서드 호출
    parent_path = file_path.parent    # 해당 객체의 상위 pathlib.Path 객체를 직접 반환환
    config_pat = parent_path / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_postix()

    print(f"File {rc_name} has not been found")