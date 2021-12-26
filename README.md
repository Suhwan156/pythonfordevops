### os 모듈

- 상당수의 로우 레벨 OS 시스템 콜 처리하며 여러 OS에서 일관된 인터페이스 제공하고자 하는데, 모든 기반 시스템에서 구동해야하는 APP에는 매우 중요한 일임
- 여러 플랫폼에서는 불가하고 특정 OS에서만 사용 가능한 기능 제공
    - 앱이 OS간 포팅이 없다고 확신하는 경우 사용

```python
import os
os.listdir('.')    # 디렉터리 목록 보여주기
os.rename('_crud_handler', 'crud_handler')    # 파일 또는 디렉터리 이름 바꾸기
os.chmod('my_script.py', 0o777)    # 파일 또는 디렉터리 권한 설정 변경
os.mkdir('/tmp/holding')    # 디렉터리 생성
os.makedirs('/Usrs/kbehrman/tmp/scripts/devops')    # 재귀적으로 디렉터리 경로 생성
os.remove('my_script.py')    # 단일 디렉터리 삭제
os.removedirs('/Usrs/kbehrman/tmp/scripts/devops')    # 최하위 경로에서부터 시작하여 디렉터리 트리 삭제하기, 비어있지 않은 디렉터리가 나타나면 연산 멈춤
os.stat('.ssh')    #파일 또는 디렉터리의 상탯값 구하기, 이 값에는 파일 타입과 권한을 나타내는 st_mode와 해당 항목에 마지막으로 접근한 시간을 나타내는 st_atime이 포함되어있음
os.stat_result(st_mode=16832, st_ino=16777344, st_dev=51714, st_nlink=2, st_uid=0, st_gid=0, st_size=29, st_atime=1640335637, st_mtime=1640334913, st_ctime=1640334913)
```

### os.path를 활용한 파일 및 디렉터리 관리

- os.path 모듈은 문자열로 경로를 생성하고 다루는데 필요한 경로 관련 메서드를 넘치도록 제공
- 유닉스 계열의 시스템에서는 슬래시, 윈도우는 역슬래시 사용해 경로 구분함
- 프로그램에서는 현재 수행중인 시스템이 무엇이든 그에 맞게 경로를 생성할 수 있음
- 경로를 쉽게 나누고 결합하는 기능이 os.path에서 가장 많이 사용되는 기능!
    - 3개 메서드: split, basename, dirname

```python
In [1]: import os

In [2]: cur_dir = os.getcwd()    # 현재 작업중인 디렉터리 구하기

In [3]: cur_dir
Out[3]: '/root'

In [4]: os.path.split(cur_dir)    # 최하위 경로와 상위 경로 나누기
Out[4]: ('/', 'root')

In [5]: os.path.dirname(cur_dir)    # 상위경로 반환
Out[5]: '/'

In [6]: os.path.basename(cur_dir)    # 최하위 경로 반환
Out[6]: 'root'
```

