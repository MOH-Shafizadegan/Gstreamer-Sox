# Import Flask library
from flask import Flask, render_template, Response
from flask import redirect, request
import os
import glob

# Create a Flask app
app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:3000'

global record_state

def gen_page():
	if os.path.exists("result.txt"): 
		recording_done = True 
		with open("result.txt", "r") as f:
			output = f.read()
		record_state = "Recording progress finished"
		audio_file = glob.glob("static/*.wav")[0].split("static/")[-1]
		print(audio_file)
	else: 
		recording_done = False
		output = "" 
		audio_file = ""
		record_state = "Recording not started yet."
	#return render_template("index1.html", recording_done=recording_done, output=output,
	#			record_state = record_state, audio_file=audio_file)
	return render_template("index3.html", recording_done=recording_done, output=output,
				record_state = record_state, audio_file=audio_file)
	
# Define a route for the home page
@app.route("/")
def index():
    # Render the index.html template
    return gen_page()

@app.route("/<string:file_name>")
def stream(file_name):
    #video_dir = "./static"
    #print(file_name)
    #return send_from_directory(directory=video_dir, filename=file_name)
    # Generate the video stream from the HLS playlist file
    def generate_video():
        with open("./static/playlist.m3u8", "rb") as f:
            yield f.read()
    # Return the video stream as a response
    return Response(generate_video(), mimetype="application/x-mpegURL")
     	
# Define a route for the audio stream
@app.route("/audio_record", methods=['POST'])
def audio():
    th = request.form['treshold']
    duration = request.form['duration']
    os.system(f'static/record.sh {duration} {th}')
    return redirect("/", code=302)
        
# Run the app
if __name__ == "__main__":
    app.run(debug=True)

