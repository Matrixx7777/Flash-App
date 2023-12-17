from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/credentials')
def credentials():
    author_info = {
        'name': 'Dawid Kocik',
        'email': 'kocik.dawid@wp.pl'
    }
    return render_template('credentials.html', author=author_info)

@app.route('/oMnie')
def oMnie():
    return render_template('oMnie.html')

@app.route('/tabela')
def tabela():
    return render_template('tabela.html')

if __name__ == '__main__':
    app.run(debug=True)
