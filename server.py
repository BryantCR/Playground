from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/play/<num>/<color>', methods = ['GET'])
def playNumber(num, color):
    bNumber = int(num)
    bColor = str(color)
    return render_template ( 'index.html', numbers = bNumber, color1 = bColor)

if __name__=="__main__":   
    app.run(debug=True)
