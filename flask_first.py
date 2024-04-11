from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])         #  메인 페이지
def main():
    if request.method == 'POST':            # 사용자가 post 방식으로 접속 했을 때
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        print(number1, number1)
    else:
        return render_template('first_template.html')

if __name__ =='__main__':
    app.run(debug=True)

