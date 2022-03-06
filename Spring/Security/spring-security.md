# Spring Security
## 동작 원리
```
1) 사용자는 원하는 URL을 입력한다. 
2) 스프링 시큐리티에서는 인증/인가가 필요하다고 판단하고(필터에서 판단) 사용자가 인증하도록 로그인 화면을 보여준다. 
3) 정보가 전달된다면 AuthenticationManager 가 적절한 AuthenticationProvider 를 찾아서 인증을 시도한다.
- AuthenticationProvider 의 실제 동작은 UserDetailsService 를 구현한 객체로 처리한다. 
- 만일 올바른 사용자라고 인증되면 사용자의 정보를 Authentication 타입으로 전달한다. : 인증(Authentication)
- 전달된 객체로 사용자가 적절한 권한이 있는지 확인하는 과정을 거친다. : 인가(Authorization)
```

## Filter, Filter Chain
### 인증
- UsernamePasswordAuthenticationFilter
```
- request 를 이용해서 UsernamePasswordAuthenticationToken 객체를 생성
- 이를 AuthenticationManager 의 authenticate()에 파라미터로 전달
```

- AuthenticationManager
```
- UsernamePasswordAuthenticationToken 를 파라미터로 받아서 실제 사용자에 대해서 검증하는 행위는 AuthenticationManager 를 통해서 이루어진다. 
- 다양한 방식으로 인증처리 방법을 제공해야하며, DB 를 이용할 것인지, 메모리상에 있는 정보를 활용한 것인지 등 다양한 방법을 사용할 수 있다. 
- 이러한 처리를 AuthenticationProvider 로 처리한다. 
```

- AuthenticationProvider
```
- 전달 되는 토큰의 타입을 처리할 수 있는 존재인지를 확인하고 이를 통해서 authenticate()을 수행한다. 
- 내부적으로는 UserDetailsService 를 이용한다. 
```

### 인가
- AuthenticationManager
```
authenticate()이라는 메서드가 있는데 리턴값은 Authentication 이라는 인증 정보이며 이 인증 정보 내에는 Roles 라는 권한에 대한 정보가 있다. 
- 이 정보로 접근 제한을 할 수 있다. 
```