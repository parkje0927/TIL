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