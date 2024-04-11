from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    result = None  # result 변수 초기화
    if request.method == 'POST':
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        operation = request.form.get('operation')
        if operation == 'add':              # 덧셈
            result = number1 + number2
        elif operation == 'subtract':       # 뺄셈
            result = number1 - number2
        elif operation == 'multiplication':     # 곱셈
            result = number1 * number2
        elif operation == 'devide':     # 곱셈
            if number2 !=0:
                result = number1 * number2
            else :
                result = 'Invalid Error'

    return render_template('first_template.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)