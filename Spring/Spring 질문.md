- JPA 영속성 컨텍스트의 이점(5가지)을 설명해주세요.
```
1. 1차 캐시
우선 1차 캐시에서 식별자 값(@Id)로 엔티티를 찾고, 찾는 엔티티가 있으면 데이터베이스를 조회하지 않고 메모리에 있는 1차 캐시에서 조회를 하기에 성능상 이점이 있다. 또한 만약 1차 캐시에 없으면 엔티티 매니저는 데이터베이스를 조회해서 엔티티를 생성하고 그 엔티티를 1차 캐시에 저장한 후에 영속 상태의 엔티티를 반환한다.

2. 동일성 보장
영속성 컨텍스트(1차 캐시)에서 관리되는 엔티티를 가져왔을 경우 동일성을 보장한다.

3. 트랜잭션을 지원하는 쓰기 지연
트랜잭션 커밋 전까지 SQL 을 쓰기 지연 SQL 저장소에 보관한다. 그리고 커밋하는 순간 영속성 컨텍스트 내 쓰기 지연 SQL 저장소에 보관된 SQL 을 보낸다.

4. 변경 감지(Dirty Checking)
영속성 컨텍스트에서 관리하는 엔티티에 변경이 일어났을 경우 이를 감지하기 때문에 em.update(엔티티) 이런 코드가 필요 없다. 엔티티 변경이 일어난 후, flush()가 발생하면 엔티티와 스냅샷을 비교하고 -> UPDATE SQL 을 생성하여 쓰기 지연 저장소에 저장한 뒤 -> 쌓여있는 쓰기 지연 SQL 저장소의 SQL 을 DB 에 반영한다. 

5. 지연로딩
엔티티에서 해당 엔티티를 불러올 때 SQL 을 날려 해당 데이터를 가져온다.
```

- Spring Filter 와 Interceptor 의 차이에 대해 설명하고, 사용 예시를 설명해주세요.
```
요청이 들어오면 Filter -> Interceptor -> AOP -> Interceptor -> Filter 순으로 거치게 된다. 
1. 서버를 실행시켜 서블릿이 올라오는 동안에 init 이 실행되고, 그 후 doFilter 가 실행된다.
2. 컨트롤러에 들어가기 전 preHandler 가 실행된다.
3. 컨트롤러에서 나와 postHanlder, after Completion, doFilter 순으로 진행이 된다.
4. 서블릿 종료 시 destroy 가 실행된다.

Filter
요청과 응답을 거른 뒤 정제하는 역할을 한다. 서블릿 필터는 DispatcherServlet 이전에 실행이 되는데 필터가 동작하도록 지정된 자원의 앞단에서 요청 내용을 변경하거나 여러가지 체크를 수행할 수 있다.
스프링 컨텍스트 외부에 존재하여 스프링과 무관한 자원에 대해 동작한다. 

- 예시
    - 공통된 보안 및 인증/인가 관련 작업
    - 모든 요청에 대한 로깅 또는 감사
    - 이미지/데이터 압축 및 문자열 인코딩
    - Spring 과 분리되어야 하는 기능

Interceptor
요청에 대한 작업 전/후로 가로챈다는 의미이다. 
스프링의 DispatcherServlet 이 컨트롤러를 호출하기 전/후로 끼어들기 때문에 스프링 컨텍스트 내부에서 Controller 에 관한 요청과 응답에 대해 처리한다. 

- 예시
    - 세부적인 보안 및 인증/인가 공통 작업
    - API 호출에 대한 로깅 또는 감사
    - Controller 로 넘겨주는 정보(데이터)의 가공
```

- 빈 주입 방법들과 가장 좋은 방법이 무엇인지, 왜 그것이 가장 좋은지 설명해주세요.
```
1. 생성자 주입
생성자 호출 시점에 1회 호출이 보장되어 주입받은 객체가 변하지 않거나 반드시 객체의 주입이 필요한 경우 강제하기 위해 사용할 수 있다. 

@Service
public class UserService {
    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}

2. setter 주입
주입받는 객체가 변경될 가능성이 있는 경우 사용한다.

@Service
public class UserService {
    private UserRepository repository;

    @Autowired
    public void setUserRepository(UserRepository repository) {
        this.repository = repository;
    }
}

3. 필드 주입
필드에 바로 의존 관계를 주입하는 방법이다. 하지만 외부에서 변경이 불가능하다는 단점이 있어서 테스트 코드에서 이에 대한 제약이 존재한다.

@Service
public class UserService {

    @Autowired
    private UserRepository repository;
}

생성자 주입을 권장하고 있는데 이유는 다음과 같다.
- 생성자 주입을 통해 변경 가능성을 배제하고 불변성을 보장할 수 있다.
- 컴파일 시점에 객체를 주입받아 테스트 코드를 작성할 수 있으며, 주입하는 객체가 누락된 경우 오류를 발견할 수 있다.
- 생성자 주입을 사용하면 필드 객체에 final 키워드를 사용할 수 있으며, @RequiredArgsContructor 를 같이 활용하여 생성자 주입을 할 수 있다.
- 애플리케이션 구동 시점에 순환 참조 에러를 방지할 수 있다.
```

- Spring 컨테이너를 통한 싱글톤 패턴과 Java 를 이용해 구현하는 싱글톤 패턴의 차이에 대해 설명해주세요.
```

```
