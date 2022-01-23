# Servlet
- 사용자의 요청을 받아서 응답을 처리해줄 수 있는 자바 객체가 Servlet(예시 - Controller)


# DispatcherServlet
- 제일 먼저 받아서 어떤 처리를 할지 결정

# mvc 구조
- 사용자의 요청을 최전선에서 FrontController 의 역할을 하는 DispatcherServlet 이 받게 된다.
- URI path 를 HandlerMapping 에게 넘기고, 모든 Controller 를 저장하고 있는 HandlerMapping 에서 올바른 Controller 를 리턴한다. 
- Controller 는 내부의 HandlerRequest 를 통해서 요청을 처리한다. 
- 요청을 처리한 뒤 ViewResolver 를 통해 view 파일 이름과 경로를 리턴한다.
- 사용자에게 올바른 화면을 보여준다.