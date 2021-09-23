from flask import Flask  # Import Flask to allow us to create our app
from flask import render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def home():
    return 'Welcome'        # Return the string 'Hello World!' as a response

#@app.route('/play', methods = ['GET'])
#def play():
#    return render_template( 'index.html' )

@app.route('/play/<num>/<color>', methods = ['GET'])
def playNumber(num, color):
    bNumber = int(num)
    bColor = str(color)
    return render_template ( 'index.html', numbers = bNumber, color1 = bColor)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


# from flask import Flask
# from flask import render_template

# app = Flask( __name__ )


# @app.route ('/play/<num>/<color>' ,methods=['GET'])
# def boxes(num,color):
#     numberofboxes = int(num)
#     colorofboxes = str(color)
    


#     return render_template ('index.html', number = numberofboxes, color = colorofboxes)


# if __name__ == "__main__":
#     app.run( debug = True )
