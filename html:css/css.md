# css(Cascading Style Sheets)
## 문법
- 태그 선택자 : `p {color: red;}`

## 속성
![css_속성]()
![css_border]()

## padding, margin
- padding : 나 자신의 부피를 감싼다.
	- padding 까지 자신의 영역으로 인식하게 하려면 -> box-sizing:border-box
- margin : 밖으로 밀어낸다.

## position
- relative : 기본
- absolute : 상위의 div 기준
- fixed : 스크롤을 움직여도 고정
- sticky : 스크롤을 내리면 이 속성에 해당한 곳이 걸리고, 다시 올리면 자기 위치를 찾는다.

## display
- 모든 div 는 block 요소
- inline 으로 설정할 경우 그 요소가 차지하는 영역만 해당
- flex
- inline-block : 라인 안에서 영역이 이어지다가, 길어지면 block 요소로 바뀜(줄바꿈)

## 추가
- overflow
	- auto : 내용이 길어지면 자동으로 스크롤이 생김.
	- scroll : 내용의 길이와 상관 없이 스크롤이 항상 생김.

## 선택자
## 기본 선택자
- 전체 선택자 : `*`
	- 많이 쓰는 것을 추천하지 않음.
- ID 선택자 : `#`
- 클래스 선택자 : `.`
- 요소 선택자 : `div`
- 특성 선택자
	```	
	- input[type="text"] {
		border-color: red;
	}
	```


- `<ul>` 안에 8번째 위치한 `<li>`
	- `li:nth-child(8)`
- disabled 가 아닌 상태의 button 에 hover 하면 배경색이 red 가 되게 하기
	- `button:not(:disabled):hover{background-color: red;}`

- 가상 요소 선택자
	- 선택한 요소의 지정된 부분에 스타일을 입힐 수 있다.
	- ::before, ::after, ::placeholder 등