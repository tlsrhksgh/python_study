# 시스템 명령어를 실행하는 방법에는 os.system, os.spawn 등이 있지만, 사용 방법이 다양하고 유연한 subprocess를 사용하는 것이 가장 일반적인 방법이다.
# 실제로 파이썬 문서에도 os.system. 대신 subprocess를 사용할 것을 추천한다.
# 새로운 프로세스를 실행하기 위해 도와주고, 프로세스의 입출력/에러결과에 대한 리턴코드를 유저가 직접 제어할 수 있게 하는 것.
# ex)) 쉘 결과를 파일로 저장하기

import subprocess as sp

output = sp.check_output("tasklist")
data = output.decode('cp949')
lines = data.splitlines()

for line in lines:
    print(line)