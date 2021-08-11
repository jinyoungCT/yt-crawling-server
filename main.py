from flask import Flask, render_template
from flask import request
from sandworks_yt_crawling import Comment

app = Flask(__name__)


@app.route('/video', methods=["GET",])
def getComments():
	vid= request.args['vid']
	limit=  request.args['limit']

	comment = Comment(vid, limit)
	response = comment.extract()

	lists = comment.commentList

	#print(data)
	
	if lists == []:
		return render_template("page_not_found.html"), 404
	
	
	return str(lists)


if __name__ == "__main__":
	app.run(host="localhost" , port=8080, debug=True)
