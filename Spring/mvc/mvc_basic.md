# Servlet
- 사용자의 요청을 받아서 응답을 처리해줄 수 있는 자바 객체가 Servlet(예시 - Controller)


# DispatcherServlet
- 제일 먼저 받아서 어떤 처리를 할지 결정
- FrontController 의 역할
- `DispatcherServlet -> FrameworkServlet -> HttpServletBean -> HttpServlet`
- 스프링 부트는 `DispatcherServlet` 을 서블릿으로 자동으로 등록하면서 모든 경로에 대해서 매핑

# mvc 구조
- 사용자의 요청을 최전선에서 FrontController 의 역할을 하는 DispatcherServlet 이 받게 된다.
- URI path 를 HandlerMapping 에게 넘기고, 모든 Controller 를 저장하고 있는 HandlerMapping 에서 올바른 Controller 를 리턴한다. 
- Controller 는 내부의 HandlerRequest 를 통해서 요청을 처리한다. 
- 요청을 처리한 뒤 ViewResolver 를 통해 view 파일 이름과 경로를 리턴한다.
- 사용자에게 올바른 화면을 보여준다.

## 인프런 강의(김영한님 강의 참고)
![MVC 구조](https://github.com/parkje0927/TIL/blob/main/Spring/mvc/mvc.png)

- 요청 흐름
	- 서브릿이 호출되면 `HttpServlet` 이 제공하는 `servie()` 가 호출된다.
	- **DispatcherServlet.doDispatch** 가 최종적으로 호출된다.
	- 핸들러 조회 -> 핸들러 어댑터 조회 -> 핸들러 어댑터 실행 -> 핸들러 실행 -> ModelAndView 반환 -> viewResolver 호출 -> View 반환 -> 뷰 렌더링 

- 주요 인터페이스 목록
	- 핸들러 매핑
	- 핸들러 어댑터
	- 뷰 리졸버
	- 뷰
