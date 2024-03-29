- 링크드리스트(LinkedList)와 어레이리스트(ArrayList) 중 검색 속도가 빠른 자료구조는 어떤 것이고, 그렇게 생각하는 이유는 무엇인가요?
```
검색속도는 ArrayList 가 더 빠르다. 
어레이리스트는 인덱스를 통해 무작위로 접근이 가능하므로 add(), get() 의 시간복잡도가 O(1) 이다. 하지만 어레이리스트는 초기 사이즈가 10이며 용량이 꽉 차게 되면 더 큰 용량의 배열에 옮기는 과정이 존재한다.(이때 늘려주는 용량은 new Capacity = oldCapacity + (oldCapacity >> 1) 이다. 즉, oldCapacity + (oldCapacity / 2) 만큼 늘어난다.) 따라서 조회가 빈번할 때만 어레이리스트가 적합하다.

반면 링크드리스트는 순차적으로 접근을 해야해서 검색속도가 느리다. get() 의 시간복잡도가 O(n) 이며 반면 add(), remove() 에서는 O(1) 이다. 중간에 추가하고자 할 때, 추가하고자 하는 노드로 가서 가리키고 있는 주소만 추가해주면 되며 삭제하는 것도 마찬가지의 과정이다. 각 요소의 연결만 변경해주면 되지 때문에 처리속도가 빠르다.

즉, 순차적으로 추가, 삭제하는 경우에는 어레이리스트가 빠르지만, 중간 데이터를 추가 삭제하는 경우에는 링크드리스트가 더 빠르다.
```

- 스택(Stack), 큐(Queue), 트리(Tree), 힙(Heap) 자료구조, TreeMap 자료구조에 대해 설명해주세요
```
- TreeMap 자료구조
key 순서가 오름차순으로 유지된다. 그 이유는 내부에 레드-블랙 트리로 저장이 되는데 이진 탐색 트리의 경우 한쪽으로 치우치면 O(N) 의 속도를 가질 수 있기 때문에 이를 보완하기 위해 등장한 자료구조라고 볼 수 있다.
레드-블랙 트리는 넣고 뺄 때 O(logN) 을 유지한다. 레드와 블랙으로 노드를 칠하고 부모노드보다 작은 값을 가지는 노드는 왼쪽으로, 큰 값은 오른쪽으로 배치하여 균형을 맞추는 자료구조이다. 
```

- 레드블랙 트리(Red-Black Tree)에 대해 설명해주세요
```
레드블랙 트리는 이진탐색트리의 일종으로 자가 균형 이진 탐색 트리이다.
모든 노드는 빨간색 혹은 검은색이고, 루트 노드가 검은색이며 모든 external node 들은 검정이다. 빨강 노드의 자식은 검정이고 빨간색 노드가 연속으로 나올 수 없다. 모든 리프노드에서 Black Depth 는 같다.
```

- 해시 테이블(Hash Table)과 시간 복잡도에 대해 설명해주세요
```
해시 테이블은 효율적인 탐색을 위한 자료구조로 key-value 쌍의 데이터를 입력받는다. 해시 함수 h 에 key 값을 이력으로 넣어 얻은 해시값 h(k)를 위치로 지정하여 key-value 데이터 쌍을 저장한다. 키 k 값을 갖는 원소가 위치 h(k) 에 hash 된다. 또는 h(k) 는 키 k 의 해시값이다 라고 표현한다. 키는 무조건 존재해야하고 중복되는 키가 있어서는 안된다.

시간복잡도는 저장, 삭제, 검색 모두 O(1) 이지만 collision 으로 인하여 최악의 경우 O(n) 이 될 수 있다.
```

- 스택(Stack), 큐(Queue)을 직접 구현하고자 할 때, 어떻게 구현할 것인지 설명해주세요
- 링크드리스트(LinkedList)와 어레이리스트(ArrayList)의 차이에 대해 설명해주세요
- 버블소트, 힙소트, 머지소트, 퀵소트, 삽입소트와 각각의 시간 복잡도에 대해 설명해주세요
- 우선순위 큐(Priority Queue)와 시간복잡도에 대해 설명해주세요
- AVL 트리(Adelson-Velsky and Landis Tree)에 대해 설명해주세요
- Elastic Search의 인덱스 구조와 RDBMS의 인덱스 구조의 차이에 대해 설명해주세요
- Redis에 대해서 간단히 설명해주세요