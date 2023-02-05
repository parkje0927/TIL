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
1) private
private 이 붙은 변수, 메소드는 해당 클래스에서만 접근이 가능하다.
2) default
접근 제어자를 별도로 설정하지 않으면 접근 제어자가 없는 변수, 메소드는 default 접근 제어자가 되어 해당 패키지 내에서만 접근이 가능하다.
3) protected
protected 가 붙은 변수, 메소드는 동일 패키지의 클래스 또는 해당 클래스를 상속받은 다른 패키지의 클래스에서만 접근 가능하다.
4) public
어떤 클래스에서라도 접근이 가능하다.
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

- try-with-resources에 대해 설명해주세요
```
이전에는 try-catch-finally 로 처리를 했는데 JDK7부터 추가된 개념이다.
try 에 자원 객체를 전달하고 try 코드 블록이 끝나면 finally 블록 없이도 자동으로 자원을 종료해주는 기능이다. 
사용 방법은 try(...) 안에 객체 선언 및 할당을 해주면 try 문을 벗어나면 try(...) 안에서 선언된 객체의 close() 메소드들을 호출한다. 그래서 finally 에 close() 를 명시적으로 호출해줄 필요 없이 자동으로 종료가 되는 것이다.
여기서 close() 를 호출해주는 객체는 AutoCloseable 을 구현한 객체만 호출이 되므로 내가 만든 클래스가 자원해제되길 원한다면 해당 인터페이스를 implements 해야 한다.
```

- 추상클래스에 있는 protected 메소드를 오버라이딩하여 구현하려고 한다. 각각 private, protected, public으로 구현할 때 이 중 불가능한 것은 무엇이고 왜 그렇게 생각했는지 설명해주세요
```
private 이다. 
먼저 public 의 경우에는 어떤 클래스라도 접근 가능하며 protected 의 경우에는 상속 관계에 있을 때 상속 받은 클래스에서 사용가능한 접근 제어자이다. 하지만 private 은 해당 클래스에서만 접근 가능하기 때문에 불가능하다.
```

- Java에서 제공하는 원시 타입들에 무엇이 있고, 각각 몇 바이트를 차지하나요?
```
- 논리형 boolean : 1byte
- 문자형 char : 2byte
- 정수형 byte : 1byte
- 정수형 short : 2byte
- 정수형 int : 4byte
- 정수형 long : 8byte
- 실수형 float : 4byte
- 실수형 double : 8byte
```

- 스택 2개로 큐를 구현해보세요
```
Stack1, Stack2 가 있고 Queue 를 구현한다고 했을 때, 예시로 1, 2, 3, 4 숫자를 Stack1 에 넣는다고 가정한다. 만약 Stack 구조에 넣고 pop 을 한다면 1, 2, 3, 4 로 넣은 데이터가 4, 3, 2, 1 순서로 조회가 될 것이다.
이때 Stack1 에 넣은 데이터를 하나씩 빼오면서 Stack2 에 넣는다. 그 이후에 Stack2 에서 데이터를 조회해오면 Queue 에 데이터를 넣고 조회해오는 것과 동일한 결과를 얻을 수 있다.
```

- 스트링 문자열을 거꾸로 만들어 반환하는 코드를 구현해보세요
```java
String str = "HELLO";

String reverseStr = "";
for (int i = str.length() - 1; i >= 0; i--) {
    reverseStr += str.charAt(i);
}

System.out.println(reverseStr);
```

```java
String str = "HELLO";

StringBuffer sb = new StringBuffer(str);
String reverseStr = sb.reverse().toString();

System.out.println(reverseStr);
```

- Java의 해시 맵(Hash Map)과 해시 테이블(Hash Table)의 차이에 대해 설명해주세요
```
두 자료구조 모두 map 자료구조라는 점에서는 동일하지만 HashMap 은 동기화를 지원하지 않아서 단일스레드에서 사용하기 좋은 자료구조라는 장점이 있다. 반면 HashTable 은 동기화를 지원하며 thread-safe 하다.
```

- JVM, JRE, JDK에 대해 설명해주세요
```
JVM 은 자바 가상 머신을 의미한다. 어느 기기/운영체제에서나 실행될 수 있게 만들어주고 메모리를 효율적으로 관리를 해서 최적화를 해준다.
JRE 는 자바 런타임 환경을 의미한다. 자바 클래스 라이브러리, JVM, 자바 클래스 로더를 포함하고 있다. 
JDK 는 우리가 일반적으로 설치하는 자바 파일을 의미한다. JDK 를 설치하면 JRE, JVM 이 자동으로 다 설치된다. JDK 에는 자바 컴파일러를 포함하고 있다. .java 파일을 만들어서 실행하면 .class 라는 파일이 자동으로 생성된다.
```

- Java의 동작 과정과 Java의 장점과 단점에 대해 설명해주세요
```
```

- Java8이 이전 버전과 다른 점(추가된 기능)에 대해 설명해주세요
```
Java8 에 추가된 기능으로는 람다 표현식, Functional 인터페이스, Stream, Optional 등이 있다.
람다 표현식은 화살표 함수를 통해서 표현을 만들 수 있고, 익명 클래스로 전환이 가능하다. 
Optional 은 null 처리를 보다 간편하게 하기 위해서 만들어졌다. 
Stream 은 순차적으로 데이터를 처리하며 뭔가 연속된 정보를 처리하는데 사용한다. 예를 들어 컬렉션을 처리하면서 for 문을 수행하게 하거나 조건으로 거를 때 사용할 수 있다.
```

- 컬렉션 관련 메소드 알고있는 것들 설명해주세요
```
max() : 가장 큰 요소 반환
min() : 가장 작은 요소 반환
sort() : 오름차순 정렬
binarySearch() : 해당 값의 인덱스 반환
copy() : 새로운 컬렉션으로 복사해서 반환
reverse() : 순서 역으로 변경
emptyList() : 불변의 List 반환
```

- Static 키워드에 대해 설명해주세요
```
경우에 따라서 각 인스턴스들이 공통적으로 같은 값이 유지되어야 하는 경우 static 을 붙인다. 멤버 변수에 static 을 붙이게 되면 클래스가 메모리에 올라갈 때 그 변수가 자동적으로 생성되기 때문에 static 이 붙은 멤버 변수는 인스턴스를 생성하지 않아도 사용할 수 있다. 그리고 static 이 붙은 메소드는 인스턴스 생성 없이 호출가능한 반면 인스턴스 변수는 생성해야만 존재할 수 있어서 static 이 붙은 메서드에서는 인스턴스 변수의 사용을 허용하지 않는다.
그러므로 메소드에서 인스턴스 변수를 사용하지 않는 메소드에 대해서 static 을 붙일 것을 고려해야한다.
```

- Java의 Optional API에 대해 설명해주세요
```
T 타입의 객체를 포장해주는 래퍼 클래스이다. 따라서 Optional 인스턴스는 모든 타입의 참조 변수를 저장할 수 있다. 즉 Null 또는 값을 감싸서 NPE 로부터 부담을 줄이기 위해 Wrapper 클래스라고 볼 수 있다.
```

