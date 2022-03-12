# OAuth 2.0

## 내용


## 적용
### 업무에서 직면한 문제점 및 상황
- 소셜로 가입을 할 경우, DB 에 새로운 멤버로 insert 를 시켰다. 
- 하지만 이 경우, 일반 로그인과 소셜 로그인 두 경우로 모두 가입을 한 유저라면 일반 로그인 시 제대로 로그인 처리가 되지 않는 문제점을 발견했다.
- 즉, 아이디로 사용을 한 핸드폰 번호로 로그인을 하려고 할 때 1명만 찾아야 하는데 2명이 찾아지는 문제점이 생겼으므로 소셜 가입한 유저여도 일반 회원 가입을 했다면 '통합'을 시켜야할지, 혹은 로그인 타입으로도 검사를 해야할지 고민이 되었다. 
	- i) 통합 회원
	- ii) 로그인시 일반/소셜 타입을 전달 받아 휴대폰번호(아이디), 비밀번호 뿐만 아니라 타입으로도 검사

### 해결
- 해결 방향은 먼저 insert 를 하지만, 추후에 추가 정보를 받아야 하는 특성상 이때 중복 처리를 하도록 처리했다. 
- 또한 OAuth 2.0 인증/인가 방식으로 수정했다.

1. 먼저, `SecurityConfig` 에 다음과 같이 추가하였다. 여기서 ProxyServer 의 특성상 mapping 주소에 'api' 를 먼저 붙여야 매핑이 되기 때문에 아래 같이 loginProcessingUrl 을 설정해주었다. 참고로 아래 코드는 개인 프로젝트의 예시를 가져왔다.
```java
@Override
protected void configure(HttpSecurity http) throws Exception {
	http
			.csrf().disable()

			.authorizeRequests()
			.antMatchers("/sample/all").permitAll()
			.antMatchers("/sample/member").hasRole("USER")

			.and()
			.formLogin() //인증, 인가에 문제 시 로그인 화면
			.and()
			.logout()

			.and()
			.oauth2Login()
			.loginProcessingUrl("/api/login/oauth2/code/*")
			.successHandler(new ClubLoginSuccessHandler());
}
```

2. 이후 `DefaultOAuth2UserService`를 상속받는 `ClubOAuth2UserDetailsService` 클래스를 생성하여, 인가 -> 토큰 -> 사용자 정보 받아오는 과정을 거친 후에는 해당 클래스에서 비즈니스 로직을 처리하도록 설계했다. 
```java
@Override
public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
	
	/**
	* 1. id 로 member 정보를 찾아온다.
	* 2. 정보가 있다면, 그 member 정보를 가져오고, 없다면 새로 insert 를 해준다. 대신 최소한의 정보만 저장하도록 설계했다. 
	* 3. 이후, new DefaultOAuth2User 를 return 하는데, 이때 권한과 id, member 를 저장한 map, id 이렇게 3개를 저장하여 전달한다.
	*/
}
```

3. 이후 SuccessHandler 에서 추가적인 로직을 처리한 뒤, redirectStrategy 로 redirect 를 보낸다. 예시 코드는 아래와 같다.
```java
@Override
public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
	//1. 추가적인 로직 처리
	//2. redirect
	redirectStrategy.sendRedirect(request, response, "/sample/hello");

}
```

- 기존에는 OAuth 2.0 의 처리 방식을 잘 활용하지 못하고 있었는데, service, handler 클래스를 통해 가입 및 로그인 로직 처리를 더 간편하게 처리할 수 있었고, 중복 로그인 처리 역시 해결할 수 있었다.