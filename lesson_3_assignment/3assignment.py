
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/sample.txt')
def render_static():
    return render_template(list.html)

@app.route('/webpage.html')
def render_static():
    return render_template(webpage.html)


@app.route('/pic.jpeg')
def render_static():
    return render_template(hello.html)



if __name__ == '__main__':
    app.run()