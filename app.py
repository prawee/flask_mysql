# import library
from flask import Flask, render_template, request

# create instance
app = Flask(__name__)

# defind router
@app.route("/")
def main():
  # return "Welcome!"
  return render_template('index.html')

@app.route("/signup")
def singup():
  return render_template('signup.html')

@app.route("/saveSignup", methods=['POST'])
def saveSignup():
  _name = request.form['name']
  _username = request.form['username']
  _password = request.form['password']
  print(_name, _username, _password)

# run
if __name__ == "__main__":
  app.run()
