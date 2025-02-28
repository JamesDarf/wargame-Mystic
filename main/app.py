from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# 플래그 파일 읽기
with open('flag.txt', 'r') as file:
    FLAG = file.read().strip()


@app.route('/')
def index():
    # 쿠키에 flag 설정
    response = make_response(render_template('index.html'))
    response.set_cookie('flag', FLAG)  # 'flag' 쿠키에 플래그 값 설정

    response.headers['X-Flag3'] = 'ThisIsTheFlag2"Na_nUn_I11I_Am_DRa"'
    return response

@app.route('/get-cookie')
def get_cookie():
    flag = request.cookies.get('flag', 'No Flag Found')
    return f"{flag}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
