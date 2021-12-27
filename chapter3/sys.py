"""
파이썬 버전 체크별 구문 출력
"""
import sys

if sys.version_info.major < 3:
    print("You need to update your Python version")
elif sys.version_info.minor < 7:
    print("You ar not running the latest version of Python")
else:
    print("good")