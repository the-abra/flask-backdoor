from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Sandbox!"


@app.route('/backdoor')
def backdoor():
    cmd = request.args.get('cmd')
    if cmd:
        # This is the intentional vulnerability
        result = subprocess.check_output(cmd, shell=True)
        return render_template_string(f"Executed: <pre>{result.decode()}</pre>")
    return "No command executed."


if __name__ == '__main__':
    app.run(debug=True, port=467)
