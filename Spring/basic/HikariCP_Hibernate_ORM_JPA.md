
# HikariCP
- 스프링 부트가 기본적으로 이용하는 Connection Pool 이 HikariCP 라이브러리를 이용한다.
- 여기서 HikariCP 란, 
```
미리 정해놓은 만큼의 connetion 은 Pool 에 담아 놓고 요청이 들어오면 Thread 가 connection 을 요청하고, Hikari 는 Pool 내에 있는 connection 을 연결해주는 역할을 한다.
```

- 하나의 쿼리가 실행되는 과정은 다음과 같다. 

```Java
Connection connection  = null;
PreparedStatement preparedStatement = null;

try {
	connection = hikariDataSource.getConnection();
	preparedStatement = connection.preparedStatement(sql);
	preparedStatement.executeQuery();
} catch(Throwable e) {
	throw new RuntimeException(e);
} finally {
	if (preparedStatement != null) {
		preparedStatement.close();
	} 
	if (connection != null) {
		connection.close(); //-> 여기서 Connection Pool 에 반납
	}
}
```

- 그렇다면, Connection 을 연결하는 과정은 아래와 같다.
![HikariCP_flowchart](https://github.com/parkje0927/TIL/blob/main/Spring/basic/HikariCP_flowchart.jpg)

- 이후 `Connection.close()` 를 하면 `Connection.close() -> concurrentBag.requite()` 이 실행되며 HikariPool 에 반납된다.

### 참고한 사이트
- https://techblog.woowahan.com/2664/

---

# Hibernate
- 자바 언어를 위한 객체 관계 매핑 프레임워크
- 객체 지향 도메인 모델을 관계형 데이터베이스로 매핑하기 위한 프레임워크
- JPA 의 구현체 중 하나

---

# ORM
- '객체지향 패러다임'을 '관계형 패러다임'으로 매핑해주는 개념


JPA
- Java 언어를 통해서 데이터베이스와 같은 영속 계층을 처리하고자 하는 스펙






