from flask import Flask, render_template #allows render index.html

#HTTP verb is "GET" here

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html', name = "Roy")

if __name__ == "__main__":
  app.run(debug=True)