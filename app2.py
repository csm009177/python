from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
# '@' ~에서 라는 뜻을 가지고 있는 atSign은 '데코레이터'라는 문법으로 
# 객체지향 언어에서 매우 자주 기용하며, node.js의 Nest.js도 데코레이터를 사용한다. 
# 이 뷰 함수가 GET 요청과 POST 요청을 모두 처리할 수 있음을 나타냅니다. 
# 즉, 루트 경로로 오는 GET 요청과 POST 요청을 모두 처리할 수 있는 다중 메서드 뷰를 설정합니다.
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

if __name__ == '__main__':
    app.run(debug=True)
