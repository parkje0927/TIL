# html
## 태그
- 중첩 구조를 허용
```
<div><p>마크업</p></div>
```
- 콘텐츠가 태그에 포함되어 있는 경우에는 닫는 태그가 없다.
```
<img src="이미지 주소" width="300" height="100">
```
- 영역
	- section
	- div
- img
	- alt : 의미가 있는 경우 설명 적기
- ul : 순서가 없는 리스트
- ol : 순서가 있는 리스트
- label 의 for 는 input 의 id 와 연결된다.
- input type
	- text
	- radio
	- checkbox

## Block vs Inline
### Block
- 부모 요소의 전체 공간을 차지하여 블록을 만든다.
- 블록 쌓듯이, 좌우 양쪽 다 차지
- ul, ol, div, h1, p

### Inline
- 요소를 구성하는 태그에 할당된 공간만 차지한다.
- img, span, a, button, strong

## 시맨틱 마크업
- 검색 엔진 최적화
- 접근성
- 유지보수

## emmet
```
div{content} tab
<div>content</div>
<div>content</div>

div>div tab
<div>
  <div></div>
</div>

div>p^div tab
<div>
  <p></p>
</div>
<div></div>

ul>li*4 tab
<ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul>

div.division tab
<div class="division"></div>

img[alt="이미지 설명"] tab
<img src="" alt="이미지 설명">

div.item$*6 tab
<div class="item1"></div>
<div class="item2"></div>
<div class="item3"></div>
<div class="item4"></div>
<div class="item5"></div>
<div class="item6"></div>
```

## tip
- mdn 활용하기 
- w3c 활용하기