# AWS(Amazon Web Service) 입문자를 위한 강의
> 인프런 Simon Kim님_AWS(Amazon Web Service) 입문자를 위한 강의를 듣고 정리한 내용입니다.

## IAM
- Identity and Access Management
- 유저를 관리하고 접근 레벨 및 권한에 대한 권리
- 유저 생성 시 접근키, 비밀키가 생긴다. 패스워드는 아니다.
- 매우 세밀한 접근 권한 부여 기능
- 비밀번호를 수시로 변경 가능케 해줌.
- Multi-Factor Authentication(다중 인증) 기능
    - Group
    - User
    - Role
    - Policy
- 정책은 그룹, 역할에 추가시킬 수 있다. 유저마다 다양한 역할 부여가능하다. 
세밀한 접근 권한을 설정해서 정책을 만들 수 있다.
- 하나의 그룹 안에 다수의 유저가 존재 가능하다.
- IAM 은 유니버설하다. -> 지역 설정이 필요 없다.

## EC2
- Elastic Computed Cloud
- 변덕스러운, 예측하기 어려운 디스크 사용량 -> EC2 를 통해 인스턴스 켜고 끌 수 있으며 켰을 때만 사용량 지불
- 다양한 지불 방법
    - On-demand : 시간 단위로 가격이 고정되어 있음.
    - Reserved : 한정된 EC2 용량 사용 가능, 1-3년 동안 시간 별로 할인 적용 받을 수 있음.
    - Spot : 입찰 가격 적용, 가장 큰 할인률을 적용받으며 특히 인스턴스의 시작과 끝기간이 전혀 중요하지 않을 때 매우 유용
- EC2 를 사용하기 위해 EBS 라는 디스크 볼륨을 요구한다.

### On-demand
- 오랜시간 동안 선불을 내지 않고 최소한의 비용을 지불하여 EC2 인스턴스를 사용하고 싶을 때, 특히 앱 프로그램 개발시 최초로 EC2 인스턴스에 deploy 할 때 매우 유용
- 미리 개발 시작 시간, 끝 시간을 알 수 없을 때 유용하다.

### Reserved
- 안정된, 예상 가능한 workload 시 Reserved 사용 권장, 선불로 인한 컴퓨팅 비용 대폭 감소
- 개발 시작 시간, 끝 시간을 알고 있을 때 유용하다.

### Spot
- 단순히 비용 절감 시 유용하다. 인스턴스의 시작/끝 시점에 구애받지 않을 경우 권장한다.

## EBS
- Elastic Block Storage
- 저장 공간이 생성되어지며 EC2 인스턴스에 부착된다.
- 디스크 볼륨 위에 File System 이 생성된다.
- EBS 는 특정 Availability Zone 에 생성된다.
    - Availability Zone : 한 쪽 서버 안 될 경우 AZ 로 회복 가능, disaster recovery

## 볼륨 타입
- SSD
    - General Purpose SSD(GP2) : 최대 19k IOPS 를 지원하며 1GB 당 3IOPS 속도가 나옴.
    - Provisioned IOPS SSD(IO1) : 극도의 I/O률을 요구하는 환경에서 주로 사용됨. 10K 이상의 IOPS 를 지원함.
- HDD
    - Throughput Optimized HDD(ST1) : 빅데이터 Datawarehouse, Log 프로세싱시 주로 사용
    - CDD HDD(SC1) : 파일 서버와 같이 드문 volume 접근 시 주로 사용, 역시 Boot Volume 으로 사용 불가능하나 비용은 매우 저렴함.
    - Magnetic(Sandard) : 디스크 1GB 당 가장 싼 비용을 자랑함. Boot Volume 으로 유일하게 가능함.

## ELB
- Elastic Load Balancers
- 수많은 서버의 흐름을 균형있게 흘려보내는데 중추적인 역할을 함.
- 하나의 서버로 traffic 이 몰리는 병목현상 방지
- traffic 의 흐름을 Unhealthy instance -> healthy instance 로 보내준다.
- Load Balancer Error : 504 Error -> 웹 서버 layer 나 데이터베이스 layer 에서 주로 해결이 가능하다.
- X-Forwarded-For 헤더
    - public IP address 인 152.12.3.225  가 DNS request 를 통해 ELB 에 도달 -> 이는 10.0.0.23 인 private IP address 로 인식한다. -> EC2 로 전달한다. -> EC2 는 private IP address 밖에 볼 수가 없다. -> X-Forwarded-For 을 통해 원래의 public IP address 인 152.12.3.225 를 알 수 있다.

### 종류
- Application Load Balancer
    - OSI 7 Layer 에서 작동됨.
    - HTTP, HTTPS 와 같은 traffic 의 load balancing 에 가장 적합함.
    - 고급 request 라우팅 설정을 통하여 특정 서버로 request 를 보낼 수 있음.
- Network Load Balancer
    - OSI 4 Layer(transport layer) 에서 작동됨.
    - 매우 빠른 속도를 자랑하며 production 환경에서 종종 쓰임.
    - 극도의 performance 가 요구되는 TCP traffic 에서 적합함.
    - 초당 수백만개의 request 를 아주 미세한 delay 로 처리 가능
- Classic Load Balancer 
    - 현재 Legacy 로 간주됨.
    - 따라서 거의 쓰이지 않음.
    - Layer 7 HTTP, HTTPS 라우팅 기능 지원
    - Layer 4 TCP traffic 라우팅 기능 지원