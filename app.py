# import library
from flask import Flask, render_template

# create instance
app = Flask(__name__)

# defind router
@app.route("/")
def main():
  return "Welcome!"

# run
if __name__ == "__main__":
  app.run()
