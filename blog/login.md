# blog 에 정리 전 기록하는 공간
## 로그인
### 세션 방식
```
Spring Session
Redis
Session 동작 방식, SessionResolver
```

### MSA 환경에서 토큰 방식
![gateway](/blog/image/login_1.png)
- client 에서 직접적으로 auth, user 와 통신하는 일은 없으며, gateway 를 통해서 통신
- 이때, route 설정을 통해 token 검증이 필요한 요청을 설정할 수 있는데, gateway 에서 토큰의 유효성과 만료 여부를 확인하도록 구성했음.
    - 다른 micro 서비스는 검증이 완료된 요청에 대한 비즈니스 로직을 수행하도록 하고, gateway 가 검증을 하는 역할을 해줌으로써 역할과 책임을 분리
- 또한, 토큰 검증이 정상적으로 처리된 경우에는 필요한 데이터를 header 에 담아서 전달하여 요청을 처리하는 서비스에서 해당 데이터를 handler 에서 처리하도록 구현함.
    - `ThreadLocal` 이용

- 기본적으로 gateway 의 경우 lb 를 구현할 경우 round robin 방식으로 구성되어 있는데, 이때 특정 요청이 수행될 때 만약 lb 로 구성된 인스턴스 중 한 곳에서 5XX server error 가 반환될 경우 다른 인스턴스로 요청이 이어질 수 있도록 RetryFilter 를 구현함.
- 추가적으로, 특정 ip 만 요청이 갈 수 있도록 제한하거나 특정 url 로 오는 요청을 block 시키는 요청을 filter 로 구현할 수 있음.

### 소셜 로그인
OAuth2 라이브러리를 활용해서 서버에서 주도적으로 로그인을 처리하려고 함.
이유는, redirectUrl 을 프론트 주소로 설정하게 되면 이후 OAuth2 의 흐름을 이어가기 위해 직접 3rd-party 에 API 요청을 보내야하는데 그런 로직을 직접 구성하기보다 OAuth2, Spring security 의 의존성을 그대로 활용해보고 싶었기 때문

하지만 결론적으로 보았을 때, 생각보다 더 커스터마이즈한 설정들이 필요하게 되었고 운영 환경에서 고려해야할 포인트들도 생겨 조금 후회되는 지점으로 남기도 했음.

```
OAuth2 의 간단한 흐름
OAuth2, OIDC 방법, 이 2가지를 같이 활용해야하는 상황

SecurityConfig 설정
- clientRegistrationRepository
- authorizationEndpoint
    - authorizationRequestRepository : cookie 에 OAuth2Request 저장 필요
    - authorizationRequestResolver : parameter 로 넘어오는 데이터들을 successHandler 까지 유지해가기 위한 CustomResolver
- userInfoEndpoint
    - userService : OAuth2User load
    - oidcUserService : OidcUser load => microsoft 의 경우 spring-cloud-starter-active-directory 라이브러리가 필요한데 이 경우 OidcUser load
- successHandler
- failureHandler

microsoft 의 경우 개인 계정인지 특정 조직(학교/회사)에 소속된 계정인지에 따라 로그인 과정이 조금 다르다.
개인 계정의 경우에는 요청 과정에서 token 값이 넘어오는데 기존 OAuth2 흐름에서는 보통 code, state 라는 값으로 넘어오지만 개인 계정은 jwt 토큰 이 넘어오기 때문에 이를 decoding 을 하게 된다.
또한 tokenUri, jwkSetUri 를 common 으로 설정해서 열어줘야 하고, decoding 을 할 때는 이 앱의 tenant id 값으로 디코딩을 해줘야해서 이 설정 부분에서 가장 어려웠음.
```