from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션에 사용될 비밀키 설정

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
    # 세션에서 username 키가 있는지 확인하여 로그인 상태 확인
    # 세션에 username 키가 있다면 로그인 상태로 간주하여 True 반환, 없으면 False 반환
    logged_in = 'username' in session
    return render_template('main.html', logged_in=logged_in)

# 로그인 페이지 라우트
@app.route('/login')
def login():
    return render_template('login.html')

# 로그아웃 기능
@app.route('/logout')
def logout():
    # 세션에서 username 키 삭제 (로그아웃)
    session.pop('username', None)
    return redirect(url_for('index'))  # 메인 페이지로 리다이렉트

# 로그인 폼 제출 처리
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
            # 로그인 성공 시 세션에 사용자 정보 저장
            session['username'] = username
            return redirect(url_for('index'))  # 메인 페이지로 리다이렉트
        else:
            # 로그인 실패 시 처리
            return "로그인 실패"
    else:
        return redirect(url_for('login'))  # POST 요청이 아닌 경우 로그인 페이지로 리다이렉트

if __name__ == '__main__':
    app.run(debug=True)
