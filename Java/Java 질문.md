1. Java 에서 제공하는 List, Set, Map 에 대해 설명해주세요.
```
[순서가 있는 목록 List]
List 인터페이스의 가장 큰 차이점은 배열처럼 "순서"가 있다는 것이다. ArrayList 와 Vector 클래스의 사용법은 거의 동일하고 기능도 거의 비슷한 "확장 가능한 배열"이다. 하지만 ArrayList 는 thread safe 하지 않고, Vector 는 thread safe 하다. 
ArrayList 는 객체를 선언할 때 매개 변수를 넣지 않으면 초기 크기는 10이다. 따라서 10개 이상의 데이터가 들어가면 크기를 늘이는 작업이 ArrayList 내부에서 자동으로 수행된다. 참고로 자바의 모든 객체가 생성되면 그 객체가 위치하는 주소가 내부적으로 할당된다.

[순서가 중요하지 않은 Set]
순서에 상관 없이, 어떤 데이터가 존재하는지를 확인하기 위한 용도로 많이 사용된다. 다시 말해서 중복되는 것을 방지하고, 원하는 값이 포함되어 있는지를 확인하는 것이 주 용도이다. 
- HashSet : 순서가 전혀 필요 없는 데이터를 저장한다. Set 중에 가장 성능이 좋다. 
- TreeSet : 저장된 데이터의 값에 따라서 정렬되는 셋이다. red-black 이라는 트리 타입으로 값이 저장되며, HashSet 보다 약간 성능이 느리다.
- LinkedHashSet : 연결된 목록 타입으로 구현된 해시 테이블에 데이터를 저장한다. 저장된 순서에 따라 값이 정렬된다. 성능이 셋 중에 가장 나쁘다. 

[key-value 형태로 저장되는 Map]
모든 데이터는 키와 값이 존재한다.
키가 없이 값만 저장될 수 없다. 
값 없이 키만 저장할 수도 없다. 
키는 해당 Map 에서 고유해야만 한다. 
값은 Map 에서 중복되어도 전혀 상관 없다.
```

- 불변 객체가 무엇인지 설명하고 대표적인 Java 의 예시를 설명해주세요.
```
불변객체는 재할당은 가능하지만, 한 번 할당하면 내부 데이터를 변경할 수 없는 객체를 의미한다. 즉 객체에 값을 할당하면 내부 데이터를 변경시킬 수 없다는 것이다. 대표적인 예로는 String, Integer, Boolean 등이 있다.
```

- 왜 객체를 불변으로 만들어야 하는지, 어떠한 장점이 있는지 설명해주세요.
```
먼저, 불변객체는 생성 후 그 상태를 바꿀 수 없는 객체를 말한다. 재할당은 가능하지만, 한 번 할당하면 내부 데이터를 변경할 수 없는 객체이다. 대표적인 예로는 String, Integer, Boolean 등이 있다.
장점은
- 객체에 대한 신뢰도가 높아진다. 
- 생성자, 접근 메소드에 대한 방어 복사가 필요 없다.
- 멀티스레드 환경에서 동기화 처리 없이 객체를 공유할 수 있다.

단점은
- 객체가 가지는 값마다 새로운 객체가 필요하다. 따라서 메모리 누수와 새로운 객체를 계속 생성해야하기 때문에 성능 저하를 발생시킬 수 있다.
```

- Immutable Object 만들기
    - final 을 사용하면 setter 를 구현할 수 없으므로 value 를 변경하려면 재할당하는 방법밖에 없다.
    - 하지만 불변 객체라면 그 참조 변수 또한 불변이어야 한다.
```java
public class Test {
    private final int value;

    public Test(final int value) {
        this.value = value;
    }
}
```


```java
public class Test {
    private final Age age;

    public Test(final Age age) {
        this.age = age;
    }

    //getter
}

class Age {
    private final int value;

    public Age(final int value) {
        this.value = value;
    }

    //getter
}
```

```java
public class Test {
    private final List<Animal> animals;

    public Test(final List<Animal> animals) {
        this.animals = new ArrayList<>(animals);
    }

    public List<Animal> getAnimals() {
        return Collections.unmodifiedList(animals);
    }
}
```

- Java 언어를 만든 사람이 누군인지 아시나요?
```
썬 마이크로시스템즈에서 1995년에 개발한 객체 지향 프로그래밍 언어로 창시자는 제임스 고슬링이다. 2010년에 오라클이 썬 마이크로시스템즈를 인수하면서 Java 의 저작권을 고휴하였다. 
```

- JVM 구조에 대해 설명해주세요.
```
자바 가상 머신으로 자바 바이트 코드를 실행할 수 있는 주체이다. 즉 자바 코드를 컴파일해서 얻은 바이트 코드를 해당 운영체제가 이해할 수 있는 기계어로 바꿔 실행시켜주는 역할을 한다. 
JVM 의 구성을 살펴보면 크게 4가지(Class Loader, Execution Engine, Garbage Collector, Runtime Data Area)로 나뉜다.

Class Loader
자바 소스를 자바 컴파일러가 컴파일하면 클래스 파일(바이트 코드)이 생성된다. 이렇게 생성된 클래스 파일들을 엮어서 JVM 이 운영체제로부터 할당 받은 메모리 영역인 Runtime Data Area 로 적재하는 역할을 Class Loader 가 한다.

Execution Engine
Class Loader 에 의해 메모리에 적재된 클래스들을 기계어로 변경해 명령어 단위로 실행하는 역할을 한다.

Garbage Collector
Heap 메모리 영역에 생성된 객체들 중에 참조되지 않는 객체들을 탐색 후 제거하는 역할을 한다.

Runtime Data Area
JVM 의 메모리 영역으로 자바 애플리케이션을 실행할 때 사용되는 데이터들을 적재하는 영역이다. 이 영역은 크게 Method Area, Heap Area, Stack Area, PC Register, Native Method Stack 으로 나눌 수 있다.
```


- Java 의 String 과 StringBuilder 의 차이에 대해 설명하고 언제 StringBuilder 를 사용하면 좋을지 얘기해주세요.
```
String 과 StringBuffer/StringBuilder 클래스의 가장 큰 차이점은 String 은 불변의 속성을 갖는다.

만약, 
String str = "hello";
str += "world";

라는 코드가 있다면, 기존에 "hello" 값이 들어가있던 String 클래스의 참조변수 str 이 "hello world" 라는 값을 가지고 있는 새로운 메모리 영역을 가리키게 변경되고 처음 "hello"로 값이 할당되어 있던 메모리 영역은 GC 에 의해 사라진다.
변하지 않는 문자열을 자주 읽어들이는 경우 String 을 사용하면 좋으나 추가, 수정, 삭제 연산이 빈번하게 발생하는 경우에는 heap 메모리에 임시 가비지가 많이 생성되어 힙메모리 부족으로 이어질 수 있다.

반면, StringBuffer/StringBuilder 는 동일 객체 내에서 문자열 변경이 가능하여 문자열 추가, 수정, 삭제가 빈번할 경우 String 보다 이 클래스들을 활용해야 한다. 
또한 이 둘의 차이는, StringBuffer 는 동기화를 지원해 멀티쓰레드 환경에서 안전하지만, StringBuilder 는 동기화를 지원하지 않지만 단일 쓰레드에서는 StringBuffer 보다 뛰어나다.
```

- 접근제어자의 종류와 특성에 대해 설명해주세요.
```
```

- Java의 StringBuffer와 StringBuilder의 차이에 대해 설명해주세요
```
둘 다 가변성을 가지는 클래스이다.
StringBuffer 는 동기화를 지원하여 멀티 스레드 환경에서 안전하다.
StringBuilder 는 동기화를 지원하지 않아서 멀티 스레드 환경에서는 적합하지 않지만 동기화를 고려하지 않는 만큼 단일 스레드에서는 성능이 뛰어나다.
```

- 템플릿 메소드 패턴이란 무엇인가요?
```
어떤 작업을 처리하는 일부분을 서브 클래스로 캡슐화해 전체 일을 수행하는 구조는 바꾸지 않으면서 특정 단계에서 수행하는 내역을 바꾸는 패턴
전체적으로 동일하면서 부분적으로는 다른 구문으로 구성된 메소드의 코드 중복을 최소화할때 유용
```

- final 키워드에 대해 설명해주세요
```
final 을 붙이면 시간이 지나도 처음 정의된 상태가 변하지 않는 것을 보장한다.
final variable, arguments : 값이 변경되지 않도록 만든다.
final class : 클래스를 상속하지 못하도록 만든다.
fianl method : 메소드가 오버라이드되지 못하도록 만든다.
```