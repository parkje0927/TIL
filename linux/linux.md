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

### 명령어
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
