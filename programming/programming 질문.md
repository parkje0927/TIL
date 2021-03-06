- OOP 에 대해 설명해주세요.
```
객체지향프로그래밍, 즉 객체의 관점에서 프로그래밍을 한다는 의미이다. 
먼저 캡슐화란, 하나의 객체에 대해 그 객체가 특정한 목적을 위한 필요한 변수나 메소드를 하나로 묶는 것을 의미한다. 
정보은닉은, getter, setter 등의 메소드를 통해서만 간접적으로 접근이 가능하도록 한다. 
추상화는 목적과 관련이 없는 부분을 제거하여 필요한 부분만을 표현하기 위한 개념을 의미하며, 다형성은 형태가 같은데 다른 기능을 하는 것을 의미한다. (ex : overriding, overloading)
마지막으로 상속은 재사용을 높여서 코드의 중복을 없애고 효율성을 높인다. 
```

- DDD(Domain-Driven-Design)에서 Domain이란 무엇인가요?
```
먼저, DDD 란 도메인 패턴을 중심에 놓고 설계하는 방식을 일컫는다. 일반적으로 많이 사용하는 데이터 중심의 접근법을 탈피해서 순수한 도메인의 모델과 로직에 집중하는 것을 말한다. 여기서 도메인이란, 사용자가 사용하는 모든 것이며 실세계에서 사건이 발생하는 집합이다. 즉, 유사한 업무의 집합으로 어플리케이션을 비즈니스 도메인 별로 나누어 설계하라는 의미이다. 도메인은 사용자에 따라 또는 사용자가 바라보는 관점에 따라 지속적으로 변하므로 문맥에 따라 객체의 역할이 바뀌는 특징이 있다. DDD 의 목적은 소프트웨어의 복잡성을 최소화하는 것에 있다. 
```

- 단위 테스트를 작성할 때 Mock을 하는 이유는 무엇일까요? 기능이 정상 동작 하려면 외부 모듈 또는 객체에 의존해야 하는데 왜 이 의존성을 끊으려고 할까요?
```
Mock 이란, 개발자가 동작을 직접 제어할 수 있는 가짜 객체를 지원하는 테스트 프레임워크이다. 실제 객체를 만들어서 테스트하기에는 시간, 비용이 높거나 객체 서로 간의 의존성이 강해 구현하기 힘들 경우 가짜 객체를 만들어 사용하는 방법이다. 즉, 테스트 작성 환경 구축이 어렵거나 다른 것에 의존적일 경우, 테스트 시간이 오래 걸리는 경우 Mock 을 활용한다.
기능이 정상 동작 하려면 외부 모듈 또는 객체에 의존해야 하지만 단위 테스트는 한 번에 메서드 하나만을 실행해는 보는 것인데도 이 메서드가 다른 네트워크, 데이터베이스 등 제어하기 어려운 것에 의존하고 있다면 테스트 수행이 어려워진다. 따라서 이 의존성을 끊기 위해 Mock 을 활용한다.
```

- 빌더 패턴에 대해 설명하고 빌더 패턴이 어떻게 구현되는지 설명해주세요.
```
빌더 패턴이란 복합 객체의 생성 과정과 표현 방법을 분리하여 동일한 생성 절차에서 서로 다른 표현 결과를 만들 수 있게 하는 패턴이다.
빌더 패턴의 장점은 다음과 같다.
1) 필요한 데이터만 설정할 수 있다. 
생성자나 수정자를 통해서 데이터를 설정하게 될 경우, 만약 어떤 필드가 필요 없는 상황이라면 이 필드에 더미값을 넣어서 생성하거나 이 필드가 없는 생성자를 또 하나 만들어야 한다. 하지만 빌더를 통해서 생성하게 되면 필요한 데이터만 가지고 설정을 할 수 있다. 

2) 유연성을 확보할 수 있다. 
객체에 새로운 필드가 추가될 경우, 기존 생성자에는 해당 필드를 모두 넣어서 수정해줘야하지만 빌더 패턴을 이용하게 되면 기존 코드를 수정할 필요가 없다. 1)번과 같은 이유로 수정하지 않고 유연하게 값을 설정할 수 있다. 

3) 가독성을 높일 수 있다.
생성자의 경우 어떤 필드에 값을 설정하는지 한 눈에 확인하기가 어렵지만, 빌더는 어떤 필드에 값을 설정하는지 한 번에 확인할 수 있다.

4) 변경 가능성을 최소화할 수 있다. 
setter 는 불필요하게 변경 가능성을 열어두는 것이다. 값을 어디서 할당하는지를 찾는 것이 어려우므로 유지보수하기가 어렵지만, 만약 값 할당 시점을 객체 생성 시점으로 제한한다면 유지보수가 더 편리해진다.

하지만, 만약 라이브러리를 통해 객체를 생성을 하거나 객체의 필드가 2개 이하라면 빌더 패턴을 구현할 필요가 없다.

빌더 패턴 구현 방법은 아래와 같다. 
먼저 public static 클래스로 생성한다. 그리고 생성자는 public 으로 하며, 필수값에 대해서는 생성자를 통해, 선택값들에 대해서는 메소드를 통해 구현한다.
선택값들에 대해서는 각각의 속성마다 메소드로 제공하며 반환은 빌더 객체 자신이다.

public class Test {
	
	public static class TestBuilder {
		private String required1;
		private String required2;

		private String optional1;
		private String optional2;

		public TestBuilder(String required1, String required2) {
			this.required1 = required1;
			this.required2 = required2;
		}

		public TestBuilder setOptional1(String optional1) {
			this.optional1 = optional1;
			return this;
		}

		public TestBuilder setOptional2(String optional2) {
			this.optional2 = optional2;
			return this;
		}

		public Test build() {
			return new Test(this);
		}
	}
}
```

- 메모리 구조에 대해 설명해주세요.
```
프로그램이 운영체제로부터 할당 받는 대표적인 메모리 공간은, '코드 영역, 데이터 영역, 스택 영역, 힙 영역' 이렇게 총 4개로 구성된다.

- 코드 영역
실행할 프로그램의 코드가 저장되는 영역으로 텍스트 영역이라고도 불린다.
CPU 는 코드 영역에 저장된 명령어를 하나씩 가져가서 처리한다.
가장 낮은 주소에 위치한다.
(상수, 함수가 저장된다.)

- 데이터 영역
프로그램의 전역 변수와 정적 변수가 저장되는 영역이며 프로그램의 시작과 함께 할당되며 프로그램 종료시 소멸된다.
(전역변수, 정적변수가 저장된다.)

- 힙 영역 FIFO
사용자가 직접 관리할 수 있는 그리고 해야만 하는 메모리 영역이다.
사용자에 의해 메모리 공간이 동적으로 할당되고 해제되며, 낮은 주소에서 높은 주소 방향으로 할당된다.
(동적할당이 되는 변수들이 저장된다.)

- 스택 영역 LIFO
함수의 호출과 관계되는 지역 변수와 매개변수가 저장되는 영역이다.
스택 영역은 함수의 호출과 함께 할당되며, 함수의 호출이 완료되면 소멸된다. 
높은 주소에서 낮은 주소의 방향으로 할당된다.
(지역변수가 저장된다.)

참고 : http://www.tcpschool.com/c/c_memory_structure
```

- DDD(Domain-Driven-Design)에서 얘기하는 3가지 계층과 각각의 역할에 대해 설명해 주세요.
```
DDD는 해당 도메인과 일치하도록 소프트웨어를 모델링하는 소프트웨어 설계 접근 방식이다. DDD 에서 이야기하는 3가지 계층은, 도메인 모델 계층, 애플리케이션 계층, 인프라 계층이 있다. 
먼저 도메인 모델 계층은 비즈니스 소프트웨어의 핵심으로 비즈니스 상황을 반영한 상태가 여기서 제어되고 사용된다. 비즈니스 개념/상황 정보/규칙을 나타내는 작업을 담당하는 역할을 한다. 
애플리케이션 계층은 소프트웨어가 수행할 작업을 정의하고 도메인 개체가 문제를 해결하도록 지시하는 역할을 한다. 
마지막으로 인프라 계층은 최초에 도메인 엔티티에 있던 데이터가 데이터베이스나 기타 영구 저장소에 유지되는 방식이다.
```

- 싱글톤 패턴에 대해 설명하고 언제 사용할 수 있는지 예를 들어주세요.
```
```