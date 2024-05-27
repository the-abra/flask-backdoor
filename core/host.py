from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app on a specific port
    port = 467  # You can change this to any port you prefer
    app.run(host='127.0.0.1', port=port)
