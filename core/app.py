import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        command = request.form['command']
        result = run_command(command)
        return render_template('index.html', result=result, command=command)
    else:
        return render_template('index.html')


@app.route('/message',methods=['POST'])
def message():
    message = request.form.get('message')
    messageContent = request.form.get('messageContent')

    messageFinal = f'{message} {messageContent}'
    run_command(messageFinal)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True,port=467)
