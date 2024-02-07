""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """
import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """

    return render_template('index.html')


@app.route("/error")
def error():
    """Эта функция запуская и отвечает за процесс возврата результата test_error.html."""
    return render_template('index.html')


@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./New_Dyplom_Alina/script/allure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/runapi")
def run_api():
    os.chdir('C:/Users/PC/PycharmProjects/New_Dyploma_Alinascript/script')
    cmd = ["api.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True,
                          shell=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/runui")
def run_ui():
    """ Эта функция запуская и отвечает за тесты страницы /example. """

    cmd = ["C:/Users/PC/PycharmProjects/New_Dyploma_Alinascript/script/ui.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True,
                          shell=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)

