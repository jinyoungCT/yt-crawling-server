from flask import Flask, render_template
from flask import request
from sandworks_yt_crawling import VideoStat

app = Flask(__name__)


@app.route('/video', methods=["GET",])
def getVideo():
	vid= request.args['vid']

	video = VideoStat(vid)
	data = video.extract()
	#print(data)
	
	videoInfo = video.videoInfo
	if videoInfo == None:
		return render_template("page_not_found.html"), 404
	#print(videoInfo)
	
	return videoInfo


if __name__ == "__main__":
	app.run(host="localhost" , port=8080, debug=True)
