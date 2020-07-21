# Travelers_Board API Server

### 작업할 내용
```bash

 1 CRUD  -  Clear
 2 Pagination 처리  -  Clear
 3 권한처리, 인증처리, 회원가입(약식)  -  Clear
 4 댓글, 게시글 삭제기능(어제말했던 상태필드를 removed 하는 방식으로)  -  Clear
 5 /board/1/posts/  => 1번 게시판의 모든 게시글 조회 api. 이런 api 만들기  -  진행중
 6 Tag 기능  -  Clear
 7 Like 기능
 8 트랜잭션 처리  -  Clear
 9 게시글(post) 목록 조회 api에 다양한 파라미터를 통한 필터가능하도록 하는 구조 만들기
    (ex. /api/posts/ => 게시글전체
    /api/posts/?create_date__gte=2020-07-01&search=aaa  => 2020-07-01 이후에 생성된 게시글 중 aaa로 검색되는 게시글 모두조회)
 10 보안기능(xss방지) post의 contents 에는 자바스크립크 구문이 실행되지 않도록 save 전에 그런구문제거
    혹은 에러리턴 등으로 게시글본문의 js 구문 실행안되도록 해야함)
 11  search 엔진을 통한 full text search
```