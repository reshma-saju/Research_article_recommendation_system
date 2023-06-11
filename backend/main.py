from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

# @app.route('/hello/<title>')
# def hello(user):
#    return render_template('hello.html', name = user)

@app.route('/recommendation',methods = ['POST', 'GET'])
def reco():
    title = request.form['inp_title']
    abst = request.form['inp_abstract']
    if request.method == 'POST':
      return render_template('hello.html', name = title)
    else:
      return redirect(url_for('success',name = title))




if __name__ == '__main__':
    app.run()
