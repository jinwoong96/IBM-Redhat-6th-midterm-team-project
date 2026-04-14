0. 코드 볼때 router에서 시작하는 게 편함
1. 매개변수 db 관련은 항상 맨뒤로  
2. 로그인을 확인하는 current_user 에 user_id 를 다른 파일에 함수로 받을 때 
매개변수 선언을 user_id로 하는게 고정. 단 user_id를 따로 받아야할때는 current_user_id 로 받음
3. 모든 예외처리는 service에서 함


user_id <<< 다 str 로 바꿔야함