0. 코드 볼때 router에서 시작하는 게 편함
1. 매개변수 db 관련은 항상 맨뒤로  
2. 로그인을 확인하는 current_user 에 login_id 를 다른 파일에 함수로 받을 때 
3. 모든 예외처리는 service에서 함, commit/refresh도 service에서 함
4. service 로직을 API 명세서 + API 명세서 상세설명과 맞게 해야함 -> 필요한 crud 더 있으면 추가로 정의
5. crud 함수 이름은 create, get, update, delete로 시작(기존 함수 이름 규칙 맞춰서 정하기)
6. scheme은 라우터, API 명세서 보고 필요한거 작성