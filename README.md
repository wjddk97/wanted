## wanted 백엔드 프리온보딩 선발 과제
   
### 1. 회원가입[POST]
- 계정, 패스워드 저장
- **endpoint :** ```http://127.0.0.1:8000/users/signup```

<br>

### **request**
```json
{
    "account":"wanted",
    "password":"hiwanted!"
}
```
<br>

### **response**
```json
{
    "message": "SUCCESS"
}
```
- 계정이 이미 존재할 경우
```
{
    "message": "ERROR_ACCOUNT_ALREDAY_EXIST"
}
```


### 2. 로그인[POST]
- 계정, 패스워드 검사 후 토큰 발행
- **endpoint :** ```http://127.0.0.1:8000/users/login```

<br>

###  **request**
```json
{
    "account":"wanted",
    "password":"hiwanted!"
}
```
<br>

### **response**
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.QU4507ChQTemgYcim6gdczC7iei3bmTDSipDKx1pufE"
}
```
- id 및 password 잘못 입력 시

```
{
    "message": "INVALID_USER_ID"
}
```
```
{
    "message": "INVALID_USER_PASSWORD"
}
```
### 3. 글 작성[POST]
- 1. 로그인을 통해 받은 토큰 header에 저장
- 2. 로그인 데코레이터를 통해 유저id를 받음
- 3. 유저id, 제목, 내용 데이터 저장
- **endpoint :** ```http://127.0.0.1:8000/board```

<br>

### **request**
```json
{
    "title":"wanted1",
    "body":"안녕원티드1"
}
```
<br>

### **response**
```json
{
    "message": "CREATE"
}
```
### 4. 글 목록[GET]
- order_by(-created_at) 최신순으로 정렬
- offset&limit 페이지네이션 적용
- **endpoint :** ```http://127.0.0.1:8000/board?offset=0&limit=5```

<br>

###  **response**
```json
{
    "board_list": [
        {
            "id": 17,
            "writer": "wanted",
            "body": "안녕원티드10",
            "created_at": "2021.10.27"
        },
        {
            "id": 16,
            "writer": "wanted",
            "body": "안녕원티드9",
            "created_at": "2021.10.27"
        },
        {
            "id": 15,
            "writer": "wanted",
            "body": "안녕원티드8",
            "created_at": "2021.10.27"
        },
        {
            "id": 14,
            "writer": "wanted",
            "body": "안녕원티드7",
            "created_at": "2021.10.27"
        },
        {
            "id": 13,
            "writer": "wanted",
            "body": "안녕원티드6",
            "created_at": "2021.10.27"
        }
    ]
}
```
### 5. 글 상세페이지[GET]
- board_id에 해당하는 정보 반환 
- **endpoint :** ```http://127.0.0.1:8000/board/<int:board_id>'```

<br>

###  **response**
```json
http://127.0.0.1:8000/board/13
{
    "board_detail": [
        {
            "board_id": 13,
            "writer": "wanted",
            "title": "wanted6",
            "body": "안녕원티드6",
            "created_at": "2021.10.27"
        }
    ]
}
```
- board_id에 해당하는 글이 없을 시
```
http://127.0.0.1:8000/board/10000
{
    "message": "BOARD_DOES_NOT_EXIST"
}
```
### 6. 글 수정[POST]
- 유저 확인
- board_id에 해당하는 글 수정
- **endpoint :** ```http://127.0.0.1:8000/board/<int:board_id>'```

<br>

###  **request**
```json
http://127.0.0.1:8000/board/13
{
    "title":"wanted13",
    "body":"안녕원티드13 수정수정수정수정수정 "
}
```

<br>

###  **response**
```json
{
    "message": "SUCCESS"
}
```
```json
GET|http://127.0.0.1:8000/board/13
{
    "board_detail": [
        {
            "board_id": 13,
            "writer": "wanted",
            "title": "wanted13",
            "body": "안녕원티드13 수정수정수정수정수정 ",
            "created_at": "2021.10.27"
        }
    ]
}
```

### 7. 글 삭제[DELETE]
- 유저 확인
- board_id에 해당하는 글 삭제
- **endpoint :** ```http://127.0.0.1:8000/board/<int:board_id>'```

<br>

### response

```json
{
    "message": "SUCCESS"
}
```

```json
GET|http://127.0.0.1:8000/board/13
{
    "message": "BOARD_DOES_NOT_EXIST"
}
```
