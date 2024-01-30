""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

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
    bash_path = "C:/Program Files/Git/bin/bash.exe"

    script_path = "C:/Users/PC/PycharmProjects/New_Dyploma_Alina/script/api.sh"

    cmd = [bash_path, script_path]

    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            universal_newlines=True) as result:
        out, err = result.communicate()
    return render_template('index.html', text=out, error=err)



@app.route("/runui")
def run_ui():
    """ Эта функция запуская и отвечает за тесты страницы /example. """

    cmd = ["./New_Dyploma_Alina/script/ui.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True,
                          shell=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)

