# Retrofit
- firebase 기반 push 알림 기능 개발을 위해 설계 중 RestTemplate 대신 Retrofit 을 도입하려고 하여 스터디 진행
- RestTemplate 은 Object 타입을 다 맞춰줘야 하지만, Retrofit 은 이와 다른 장점을 가지고 있다고 하여 더 알아보게 되었다.

## Retrofit 전반적인 내용
- ![baelding 문서](https://www.baeldung.com/retrofit)
- Retrofit 은 요청과 응답 데이터에 있어 타입을 강제한다. (Type-safe 하다.)

## 실습
### import
- gradle 의 경우 MavenCentral 에서 찾아보기
```
<dependency>
    <groupId>com.squareup.retrofit2</groupId>
    <artifactId>retrofit</artifactId>
    <version>2.3.0</version>
</dependency>  
<dependency>  
    <groupId>com.squareup.retrofit2</groupId>
    <artifactId>converter-gson</artifactId>
    <version>2.3.0</version>
</dependency>
```

### Model
- 간단한 예시를 위해 `User` 도메인을 만드려고 한다. 
```java
public class User {
  private String login;
  private Long id;
  private String url;
}
```

- 이후, REST endpoint 로부터 객체를 반환하는 `interface` 를 하나 생성한다. 
```java
public interface UserService {
  
  /**
  * @GET annotations
  * {baseUrl} 에서 {baseUrl}/users 로 request 를 전달
  *
  * @Query
  * `@Query` 가 붙은 값이 null 이면 자동으로 해당 값이 무시된다.
  *
  * @Path
  * path parameter
  */

  @GET("/users")
  public Call<List<User>> getUsers(
    @Query("per_page") int per_page, 
    @Query("page") int page);
  
  @GET("/sers/{username}")
  public Call<User> getUser(@Path("username") String username);
}
```

- 그 다음에는, Retrofit 객체를 하나 생성한다. 
```java
OkHttpClient.Builder httpclient = new OkHttpClient.Builder();
Retrofit retrofit = new Retrofit.Builder()
  .baseUrl("https://api.github.com/")
  .addConverterFactory(GsonConverterFactory.create())
  .client(httpClient.build())
  .build();
```

  - baseUrl : 각 call, converterFactory 에 쓰일 베이스가 될 url
  - converterFactory : 우리가 보내고 받는 데이터를 parsing 하는 것과 관련된 일을 진행
  - GsonConverterFactory : JSON 타입의 데이터를 User 클래스로 매핑
  - OkHttpClient : Android, Java 앱을 위한 HTTp & HTTP/2 클라이언트이다. 서버에 접속하고 데이터를 보내고 정보를 받아오는 것을 관리한다.

- 각 call 에 header 나 interceptor 를 추가할 수 있다. 

### Synchronous API
- 위에서 만든 클래스들을 활용하여 실제 구동하는 코드를 작성
```java
UserService service = retrofit.create(UserService.class);
Call<User> callSync = service.getUser("jh");

try {
  Response<User> response = callSync.execute();
  User user = response.body();
} catch (Exception e) {
  log.error(e);
}
```

- 여기서 `execute` 함수는, 동기적으로 call 을 수행해서 데이터를 전달할 동안 현재의 스레드를 block 처리를 한다. 이후 요청이 성공적으로 수행되면 정보를 Response 의 body 로 얻어올 수 있으며 GsonConverterFactory 덕에 User 클래스로 받아올 수 있다.

### Asynchoronous API
- `non-blocking asynchronous request` 를 보통 사용한다고 하는데 이는 무엇인가?
- 먼저 Async, Sync & Blocking, Non-Blocking 의 차이를 살펴보자
```txt
작업을 요청하는 클라이언트 : A
작업을 수행해서 결과를 return : B

Sync & Async : 작업의 주체성을 누가 갖는가 => A / B
Blocking & Non-Blocking : 로직의 흐름 => 멈춘다. / 안 멈춘다.

Sync-Blocking : A 는 B 가 완료할 때까지 계속 기다린다.
Sync-Non-Blocking : A 가 작업의 주체성을 갖고 있으며, B 가 작업을 완료할 때까지 핑퐁하면서 완료 여부를 체크한다.

Non-Blocking : B 가 A 에게 
Async-Blocking : A 가 넘겨준 콜백 함수를 B 가 실행하고 완료하는 것을 기다린다.
Async-Non-Blocking : A 가 B 에게 콜백 함수를 넘겨주고 A 는 자신의 일을 계속 진행하다가 B 가 작업 완료하면 A 가 넘겨 준 콜백 함수를 수행한다.

```
- `non-blocking asynchronous request` 는 결국 A 는 B 에게 요청만 하고 자신의 일에 집중할 수 있고, B 역시 요청 받은 일을 끝내면 알아서 콜백 함수로 작업을 마무리 지을 수 있으니 더 효율적인 방법이라고 볼 수 있다. 

- 아래 예시를 보자
```java
UserService service = retrofit.create(UserService.class);
Call<User> callAsync = service.getUser("jh");

callAsync.enqueue(new Callback<User>() {

  @Override
  public void onResponse(Call<User> call, Response<User> response) {
    User user = response.body();
  }

  @Override
  pyblic void onFailure(Call<User> call, Throwable throwable) {
    System.out.println(throwable);
  }
})
```

- 이렇게 enqueue 메소드를 활용하면, 성공과 실패를 다루기 위해 Callback<User> 를 활용하게 되는 것이며, 서로 분리된 스레드에서 수행이 될 것이다. 
- 요청이 성공적으로 끝나면, 이전과 똑같이 정보를 Response body 에서 얻어올 수 있다.

### Reusable 한 클래스
- 위 코드를 재사용이 가능하게 만들기 위해 코드를 정리해보자
```java
public class RetrofitGenerator {

  private static final String BASE_URL = "https://api.github.com/";

  private static Retrofit retrofit = new Retrofit.Builder()
    .baseUrl(BASE_URL)
    .addConverterFactory(GsonConverterFactory.create())
    .build();

  private static OkHttpClient.Buider httpClient = new OkHttpClient.Builder();

  public static <S> S createService(Class<S> serviceClass) {
    return retrofit.create(serviceClass);
  }
}
```

- 아래와 같이 호출하여 사용할 수 있다.
```java
UserService service = RetrofitGenerator.createService(UserService.class);
```

### Authentication
- 보안 접근을 위해 authentication 관련 코드를 위에서 생성한 RetrofitGenerator 클래스내 createService(seriviceClass, token) 메소드를 추가해본다. 

```java
public static <S> S createService(Class<S> serviceClass, final String token) {
  if (token != null) {
    httpClient.interceptors().clear();
    httpClient.addInterceptor( chain -> {
      Request original = chain.request();
      Request request = original.newBuilder()
        .header("Authorization", token)
        .build();

        return chain.proceed(request);
    });

    builder.client(httpClient.build());
    retrofit = builder.build();
  }

  return retrofit.create(serviceClass);
```
- interceptors 를 사용하면 OAuth 나 user/password 와 같은 authentication 모두에서 다 사용가능해진다.

### logging
- log 를 확인하고 싶다면 먼저 import 를 해주어야 하며 관련 코드는 baeldung 사이트를 참고하여 작성해보면 될 것 같다.
```
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>logging-interceptor</artifactId>
    <version>3.9.0</version>
</dependency>
```

## 참고한 사이트
- ![baelding 문서](https://www.baeldung.com/retrofit)
- ![Async/Sync/Blocking/Non-Blocking](https://wbluke.tistory.com/49)

## 추후 더 study 할 내용
- Sync/Async 
- Blocking, Non-Blocking