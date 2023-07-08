# Import Flask library
from flask import Flask, render_template, Response
from flask import redirect, request
import os
import glob

start_recording = False

# Create a Flask app
app = Flask(__name__)

def gen_page(start_recording):
	#return render_template("index2.html", start_recording=start_recording)
	return render_template("index4.html", start_recording=start_recording)	
	
# Define a route for the home page
@app.route("/")
def index():
    # Render the index.html template
    return gen_page(False)

@app.route('/stream', methods=['POST'])
def stream():
    os.system('./stream/build/bin/main')
    return gen_page(True)    
        
# Run the app
if __name__ == "__main__":
    app.run(debug=True)

