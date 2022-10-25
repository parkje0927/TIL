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
자바 싱글톤은 클래스로더에 의해 구현되고, 스프링의 싱글톤은 스프링 컨테이너에 의해 구현된다. 즉, 스프링 컨테이너를 통한 싱글톤 패턴은, 클래스 자체에 의해서가 아니라 스프링 컨테이너에 의해 구현된다. 특정 클래스에 @Bean 이 정의되면, 스프링 컨테이너는 그 클래스에 대해 딱 한 개의 인스턴스를 만든다.
자바 싱글톤의 scope는 코드 전체이고, 스프링 싱글톤의 scope 는 해당 컨테이너 내부이다.
자바 싱글톤 패턴은 개발자의 로직에 따라 thread safety 를 보장할수도 있고, 보장하지 않을 수도 있다. 반면 스프링에 의해 구현되는 싱글톤 패턴은 Thread Safety 를 자동으로 보장한다. 

아래와 같이 작성된 경우, SingletonService 객체를 생성하기 위해 new SingletonService() 로 호출시 에러가 뜨게 된다.

public class SingletonService {
	private static final SingletonService instance = new SingletonService();

	public static SingletonService getInstance() {
		return instance;
	}

	private SingletonService() {

	}

	public void test() {
		System.out.prinln("싱글톤 객체 로직 호출");
	}
}

참고 : https://gem1n1.tistory.com/96
```

- Spring 프레임워크는 트래잭션을 어떻게 구현하였는지 설명해주세요.
```
트랜잭션은 스프링 AOP Proxy 를 통해 처리가 된다.
프록시 객체를 통해 기능 수행한 뒤 이상이 없으면 commit 을 하고 이상이 있으면 rollback 을 하게 된다.
Spring 에서는 @Transactional 어노테이션을 명시하게 되면 내부적으로 AOP 를 통해 트랜잭션 처리 코드가 전후로 수행된다.

여기서 AOP 는 관점 지향 프로그래밍으로, 포인트컷을 통해 특정 시점에 어떤 행위를 할 수 있도록 설계하는 방식을 말한다. AOP 는 일반적으로 2가지 방법이 있는데, JDK Dynamic Proxy 방식과 CGLIB 방식이 있다. 

- JDK Dynamic Proxy
트랜잭션 처리를 다이나믹 프록시 객체에 대신 위임하는 방식으로, 다이나믹 프록시 객체는 타깃이 상속하고 있는 인터페이스를 상속 후 추상 추상메소드를 구현하며, 내부적으로 타깃 메소드 호출 전후로 트랜잭션 처리를 수행한다.
이런 프록시 객체를 런타임 시점에 동적으로 만들어주기 때문에 다이나믹 프록시라고 한다.

- CGLIB
바이트 코드 생성 프레임워크를 사용하여 런타임 시점에 프록시 객체를 만드는 방식이다.

스프링 컨테이너는 트랜잭션 범위의 영속성 컨텍스트 전략을 기본으로 한다.
트랜잭션 AOP 가 트랜잭션을 시작할 때 -> 영속성 컨텍스트가 생기고, 메소드가 종료되어 트랜잭션 AOP 가 트랜잭션을 커밋할 경우 -> 영속성 컨텍스트가 flush 되면서 해당 내용이 반영된다. -> 이후 영속성 컨텍스트 역시 종료

참고 : https://hwannny.tistory.com/98
```

- JPA에서 PK는 어떻게 설정하나요?
```

```

- Spring의 DI가 어떻게 동작하는지 설명해주세요.
```

```

- Spring의 3가지 Layer에 대해 설명해주세요
```
presentation layer, service layer, data access layer 3가지 계층과 모든 계층에서 사용되는 도메인 모델 클래스로 구성되어 있다. 각각의 계층은 독립적으로 분리하여 구현하는 것이 가능해야 하는데 presentation layer 는 요청 및 응답을 처리한다. 즉 비즈니스 로직과 최종 UI 를 분리하기 위해서 컨트롤러 기능을 제공한다.
service layer 는 비즈니스 로직 처리와 도메인 모델의 적합성 검증을 한다. data access layer 는 데이터 액세스 로직을 객체화하고 마지막으로 도메인 모델 클래스는 VO 또는 DTO 객체에 해당한다.
```

- Spring과 SpringBoot의 차이에 대해 설명해주세요
```
spring boot starter 가 대부분의 dependency 를 관리해준다.
spring boot 는 xml 설정을 하지 않아도 된다.
spring boot 는 AutoConfiguration 이 있어서 많은 외부 라이브러리, 내장 톰캣 서버등이 실행될 수 있다.
```

- API가 무엇인지 설명해주세요
```
API 는 Application Programming Interface 로 응용 프로그램에서 사용할 수 있도록 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 의미한다.
```

- JPA FetchType에 대해 설명하고 각각 어떤 기준으로 사용하시는지 설명해주세요
```
- FetchType.LAZY 지연로딩
회원과 팀이라는 객체가 있을 때 지연로딩을 사용하게 되면 회원 엔티티를 조회할 때 팀 회원을 같이 조회하는 것이 아니라 실제로 팀 엔티티를 사용할 때 조회해오는 방법을 의미한다. 여기서 사용하는 방버은 프록시 전략이다. 실제 팀 엔티티를 가져오는 것이 아니라 프록시 객체가 들어가 있다가 실제로 사용할 때 이 프록시가 팀 엔티티 관련 데이터를 리천을 해준다.

- FetchType.EAGER 즉시로딩
즉시 연관된 엔티티도 다 조회해온다. 조인을 이용해 하나의 쿼리로 데이터를 가져오기 때문에 만약 특정 상황에서 데이터를 가져오지 못하는 상황이 발생한다면 null 이 될 수 있다.
```

- 프레임워크와 라이브러리의 차이점
```
프레임워크와 라이브러리의 차이점은 제어 흐름의 권한이 어디에 있는가이다.
라이브러리를 사용할 때 사용자는 애플리케이션 코드의 흐름을 직접 제어해야 한다. 
반면 프레임워크는 애플리케이션의 코드가 프레임워크에 의해 사용된다. 제어의 흐름은 프레임워크가 가지고 있고 사용자가 그 안에 필요한 코드를 작성하게 된다. 

라이브러리의 경우 애플리케이션의 흐름을 사용자가 직접 제어해야 하지만 프레임워크의 경우 코드를 연결할 수 있는 위치를 제공하고 사용자가 연결한 코드를 호출하는 제어 흐름 권한을 가지고 있다.
```