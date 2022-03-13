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