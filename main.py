from flask import Flask
from flask import request
from sandworks_yt_crawling import VideoStat

app = Flask(__name__)


@app.route('/video', methods=["GET",])
def getVideo():
	vid="T7h8O7dpJIg"
	video = VideoStat(vid)
	data = video.extract()
	#print(data)
	
	videoInfo = video.videoInfo
	#print(videoInfo)
	
	return videoInfo


if __name__ == "__main__":
	app.run(host="localhost" , port=8080, debug=True)
