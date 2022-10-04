## 리눅스 bash shellscript 기초편 강의
### 리눅스와 쉘(Bash)
```
- Tab : 명령 자동완성
- Ctrl + c : 인터럽트 시그널을 보내 실행 중인 프로세스를 중단
- Ctrl + a : 라인 맨 앞으로 커서 이동
- Ctrl + e : 라인 맨 뒤로 커서 이동
- Ctrl + r : history 검색
```

### 실습 환경
- JSLinux
- Codeonweb
- 리눅스 설치해서 bash 사용

### 파일 시스템 관련 명령어
```
- root 로 가기 : cd /
- 상대경로
    - . : 현재 디렉토리
    - .. : 현재보다 상위 디렉토리
- 파일 시스템 관련
    - cd
    - ls
    - ls -al
    - ls -1 : 파일명만
    - ls -alh : 사람이 읽기 편한 용량을 표시하는게 h
    - ls -alt : 시간순으로 정렬
    - ls -altr : 역순으로 정렬
    - df(Disk Free) : 마운트된 모든 장치에 대한 현재의 디스크 공간 통계를 출력
    - df -h : 단위를 같이 보여지게 해서 편하다.
```

### 디렉토리와 파일 통계
```
- mkdir
- rmdir : 안에 비어있다면 디렉토리 삭제
- mount : 디스크 장치를 표시하거나 가상 파일 시스템으로 지정한 디렉토리를 연결
- stat : 지정한 파일의 파일 통계를 출력
```

### 파일 명령어
```
- touch : 지정한 이름의 비어있는 파일을 생성하거나 파일이 있는 경우 타임스탬프를 업데이트
- cat(catenate) : 지정한 파일의 내용을 출력
- head : 지정한 파일의 1 라인부터 지정한 라인까지 출력(기본 지정값 10)
- tail : 지정한 파일의 마지막 라인부터 지정한 수만큼의 라인을 출력(기본 지정값 10)
    - tail -f : 로그 확인 명령어 
    - tail -F
- cp : 지정한 파일을 지정한 위치와 이름으로 복사
    - cp -rfp 원본파일패스/이름 복사할파일패스/이름
    - 원본 파일이나 디렉토리가 남아있다.
- mv : 지정한 파일을 지정한 위치와 이름으로 이동
    - 원본 파일이나 디렉토리가 남아있지 않는다.
    - 파일을 옮기는 것보다 이름을 변경할 때 사용한다. 파일이나 디렉토리가 남아있지 않기 때문에, cp 로 먼저 옮기고 나중에 rm 으로 삭제하는 것이 안전하다.
- rename : 지정한 규칙에 따라 여러 개의 파일 이름을 변경
    - rename 변경전파일명 변경후파일명 대상파일
    - 예시) 파일명이 모두 규칙이 test1, test2, test3 처럼 되어 있는데 이를 test01, test02, test03 처럼 바꾸고 싶다면 -> rename test test0 test? 이렇게 해준다.(? 는 문자 하나를 의미한다.)
    - 예시) 위 예시에서 다시 원래대로 바꾸고 싶다면 -> rename test0 test test0?
- rm(remove) : 지정한 파일을 삭제
    - 실수로 삭제한다면 되돌릴 수 없다.
    - 디렉토리 삭제 시 : rm -rf
    - 파일 삭제 시 : rm -f
- less : 상하로 커서 이동이 가능한 파일 보기
    - 예시) less testfile.txt
    - q 를 입력하면 빠져나온다.
- ln(link) : 지정한 파일에 대한 심볼릭 링크나 하드링크를 생성
    - ln 옵션 링크의원본파일패스/이름 링크파일패스/이름
    - ln aaa.txt hardlink.txt
    - 하드링크 파일에서 수정을 하면 원본 파일도 수정된다.
    - 원본 파일을 삭제하면, 하드링크 파일은 그대로 유지된다.

    - ln -s hardlink.txt symboliclink.txt
    - 심볼링 링크는 링크 파일 표시가 된다.
    - 심볼링 링크 입장에서는 하드링크가 원본파일인 상황인데, 하드링크 파일을 삭제하면 파일이 깨졌다고 표시가 된다.

- paste : 지정한 파일들의 행을 읽어 탭으로 구분하여 병합
    - shell script 에서 보통 사용한다.
- dd : 블록 단위로 데이터셋을 정의하여 파일을 쓰고 읽음
    - Dataset Definition
    - dd if=인풋파일이름 of=아웃풋파일이름 bs=바이트(크기) count=블록을복사할횟수
- tar : 지정한 데이터 및 디렉토리를 하나의 파일로 만든다.
    - 압축한다 | create, verbal, zip, file => 이렇게 구성된 명령어가 cvzf : tar -cvzf 타르볼파일명 디렉토리명/파일명
    - 압축 푼다 | extract, verbal, zimp, file => 이렇게 구성된 명령어가 xvzf : tar -xvzf 타르볼파일명
```

### 프로세스 관련 명령어
- 프로세스는 프로그램을 실행하면 메모리에 올라가는 작업 단위를 의미
```
- ps(Process Status) : 시스템에서 실행 중인 프로레스에 대한 정보를 출력
    - ps -ef
    - ps aux
    - ps axfwwwww : 내용이 끊기지 않고 다 나옴. w 개수에 따라 정도가 다른데 3 ~ 5개 정도 쓴다. 그러면 명령어가 모두 나온다.
- pstree(process status tree) : 시스템에서 실행 중인 프로세스에 대한 정보를 트리구조로 출력
- top : 프로세스 목록을 일정 시간마다 새로고침하여 화면에 출력하는 툴, 시스템 전반적인 상황을 모니터링 할 수 있음.
    - 출력되는 항목에 대한 설명(확인하고 싶을 때 추후에 다시 강의 듣기)
    - ctrl + c 혹은 q 눌러서 빠져나올 수 있다.
- nohup(no hangUPs) : 쉡 스크립트 파일을 데몬 형태로 실행, 표준 출력을 지정한 파일로 리다이렉트 => 백그라운드에서 실행
- kill : 지정한 프로세스에 지정한 시그널을 보내 프로세스 종료
    - kill -2 프로세스번호 or kill -INT 프로세스번호
    - kill -15 프로세스번호 or kill -TERM 프로세스번호
    - kill -9 프로세스번호 or kill -KILL 프로세스번호
    - 좀비 프로세스는 INT 나 TERM 으로는 안 죽기 때문에 kill -9 혹은 kill -KILL 로 죽일 수 있다.
```

### 네트워크 관련 명령어
```
- ifconfig(Interface Configuration)
    - 네트워크 인터페이스의 활성/비활성화 및 설정
- ip
    - ip 관련 정보 조회 및 설정
- netstat(Network Statistics)
    - 네트워크 프로토콜의 통계와 연결상태를 출력
    - netstat -nltpu : active internet connections(only servers)
- ss(Socket Statistics)
    - 네트워크 소켓의 통계와 연결상태를 출력
    - ss -nltpu
- iptables : 패킷 필터링 도구로 패킷의 출입을 제한하는 방화벽 구성이나 NAT(Network Address Translation) 구성에 사용
- ufw(Uncomplicated Firewall) : iptables 의 제어를 쉽게 하기 위한 도구
- ping : ICMP 프로토콜의 응답 확인 도구
```




