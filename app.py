# import library
from flask import Flask, render_template

# create instance
app = Flask(__name__)

# defind router
@app.route("/")
def main():
  # return "Welcome!"
  return render_template('index.html')

# run
if __name__ == "__main__":
  app.run()
