from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return "Automate Deployment of Python Flask App on AWS AppRunner using GitHub Actions"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)