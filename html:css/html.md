# HTML(Hyper Text Markup Language)
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

## Box, Item
### Box
- Item 들의 sectioning 을 도와주고, 사용자의 눈에는 보이지 않음.
- 나중에 css 로 스타일링은 가능하지만 html 에서는 보이지 않음.

### Item
- 실제 사용자의 눈에 보인다.
- Block, Inline

## Block vs Inline
### Block
- 부모 요소의 전체 공간을 차지하여 블록을 만든다.
- 블록 쌓듯이, 좌우 양쪽 다 차지
- ul, ol, div, h1, p

### Inline
- 요소를 구성하는 태그에 할당된 공간만 차지한다.
- img, span, a(`새창에서 열기 -> target = _blank`), button, strong

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

## 예시
```
<body>
  <!-- Box vs Item -->
  <header></header>
  <footer></footer>
  <section></section>
  <div></div>
  <span></span>
  
  <h1></h1>
  <button></button>
  
  <!-- a -->
  <a href="http://google.com" target="_blank">Click</a>
  
  <!-- p, b, span : Inline -->
  <p>This is a sentence. <b>That</b> is ...</p>
  <p>This is a sentence. <span>That</span> is ...</p>
  
  <!-- div : Block -->
  <p>This is a sentence. <div>That</div> is...</p>
  
  <!-- List -->
  <ol type="i" reversed>
    <li>1.</li>
    <li>2.</li>
    <li>3.</li>
  </ol>
  
  <ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
  </ul>
  
  <!-- Input(label, input : Inline) -->
  <label for="input_name">Name : </label>
  <input id="input_name" type="text">
  
  <label for="file">Name : </label>
  <input id="file" type="file">
  
</body>
```
