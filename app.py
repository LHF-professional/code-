from flask import Flask, render_template, jsonify, request
import time
from random import randrange

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.form.get('firstInput')
        b = request.form.get('secondInput')
        return jsonify({'message': 'Success', 'a': a, 'b': b})
    return render_template('index.html')


@app.route('/button_1/')
def button_1():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'One'})


@app.route('/button_2/')
def button_2():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Two'})


@app.route('/button_3/')
def button_3():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Three'})


@app.route('/button_4/')
def button_4():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Four', 'status': 400}), 400


@app.route('/button_5/')
def button_5():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Five'})


@app.route('/button_6/')
def button_6():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Six'})


@app.route('/button_7/')
def button_7():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Seven'})


@app.route('/button_8/')
def button_8():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Eight'})


@app.route('/button_9/')
def button_9():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Nine'})


@app.route('/button_10/')
def button_10():
    time.sleep(randrange(1, 2))
    return jsonify({'message': 'Ten'})


if __name__ == '__main__':
    app.run()
