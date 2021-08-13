from flask import Flask,render_template, request
from flaskwebgui import FlaskUI
import pathlib
from engine.Scraping import Scraping

scrape = Scraping()

print(str(pathlib.Path(__file__).parent.parent.absolute()) + '\index.html')
app = Flask(__name__ , template_folder='GUI\\frontend', static_folder='GUI\\static')
ui = FlaskUI(app, width= 695)

@app.route('/')
def function():
    return render_template('index.html')


@app.route('/scraping')
def scraping():
    args = request.args
    arg1 = request.args.get("location")
    arg2 = request.args.get("type")
    arg1 = int(arg1)
    arg2 = int(arg2)
    info = scrape.FindPage(arg1, arg2)
    scrape.createExcel(info)
    return ("nothing")

ui.run()

if __name__ == '__main__':
    app.run( host='127.0.0.1',debug = True)

