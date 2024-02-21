from flask import Flask, render_template, request, redirect, url_for
import pymysql # pip install pymysql

app = Flask(__name__)

# MariaDB 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='0177',
    database='unhw',
    cursorclass=pymysql.cursors.DictCursor
)

# 메인 페이지 라우트
@app.route('/')
def index():
    if request.method == 'POST':
        # POST 요청일 때, 토글 상태를 확인하고 출력합니다.
        toggle_state = request.form.get('toggle')
        if toggle_state:
            return "토글이 켜졌습니다."
        else:
            return "토글이 꺼졌습니다."
    else:
        # GET 요청일 때, index.html을 렌더링합니다.
        return render_template('index.html')

# 로그인 페이지 라우트
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 폼에서 전달된 아이디와 비밀번호 가져오기
        username = request.form['username']
        password = request.form['password']
        
        # MariaDB에서 유저 정보 확인
        with connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE id=%s AND pw=%s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

        if user:
            # 로그인 성공 시 처리 (예: 세션 설정)
            return "로그인 성공"
        else:
            # 로그인 실패 시 처리
            return "로그인 실패"
    else:
        # GET 요청일 때는 로그인 폼 보여주기
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
