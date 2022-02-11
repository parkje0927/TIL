# Retrofit
- firebase 기반 push 알림 기능 개발을 위해 설계 중 RestTemplate 대신 Retrofit 을 도입하려고 하여 스터디 진행
- RestTemplate 은 Object 타입을 다 맞춰줘야 하지만, Retrofit 은 이와 다른 장점을 가지고 있다고 하여 더 알아보게 됨.

## Retrofit 전반적인 내용
- ![baelding 문서](https://www.baeldung.com/retrofit)
- Retrofit 은 요청과 응답 데이터에 있어 타입을 강제한다. (Type-safe 하다.)

- API 예시
```
public interface UserService {

    @GET("/users")
    public Call<List<User>> getUsers(
      @Query("per_page") int per_page, 
      @Query("page") int page);

    @GET("/users/{username}")
    public Call<User> getUser(@Path("username") String username);
}
```

- `https://api.github.com/users` 로 request 를 전달한다는 의미
- `@Query` 가 붙은 값이 null 이면 자동으로 해당 값이 무시된다. 
- `@Path` 는 path parameter

- Synchronous / Asynchoronous API
