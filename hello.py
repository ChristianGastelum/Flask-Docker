from flask import Flask
#imports flask from package flask
app = Flask(__name__)

#create instance of the Flask object using our module name as parameter,
#Flask use this to resolve resources, and in complex cases one can use
#other than __name__ here.


@app.route('/', methods=['GET'])

def index():
    return "Hello World Docker!"

#When the user visits our application the return value of this will be what is sent
#in response to a user requests our landing page.

if __name__ == '__main__':
    # if our application is run directly
    #app.run(port=5000, debug=True) #kicks off development server on our localmachine
    app.run(debug=True, host='0.0.0.0')