from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def destroy():
    session['count'] = 0
    return redirect('/')

@app.route('/plus2', methods=['POST'])
def plus2():
  session['count'] += 1
  return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset():
  session['count'] = 0
  return redirect('/')


 


if __name__ == "__main__":
    app.run(debug=True)
