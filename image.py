from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
from werkzeug.datastructures import FileStorage

app = Flask (__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('image', type=FileStorage, location='files')

class Image(Resource):
	def get(self):
		return {"message":"Plese sent 'image' (POST method) to me."}
	def post(self):
		args = parser.parse_args()
		image = args['image']
		image_name = image.filename
		image.save(image_name)
		return {"code":200,"desc":"Upload Success"}

api.add_resource(Image,'/image')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)

