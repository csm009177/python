from flask import Flask, render_template, request, redirect, url_for
import pymysql

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
    return render_template('main.html')

# 로그인 페이지 라우트
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginForm', methods=['POST'])
def loginForm():
    if request.method == 'POST':
        # 폼에서 전달된 아이디와 비밀번호 가져오기
        username = request.form['username']
        password = request.form['password']
        
        # MariaDB에서 유저 정보 확인
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s AND pw=%s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()
            
        if user:
            # 로그인 성공 시 처리 (예: 세션 설정)
            return redirect(url_for('index'))
        else:
            # 로그인 실패 시 처리
            return "로그인 실패"
    else:
        return redirect(url_for('login'))  # POST 요청이 아닌 경우 로그인 페이지로 리다이렉트

if __name__ == '__main__':
    app.run(debug=True)
