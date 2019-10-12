from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Handler(Resource):
    def post(self):
        # Parse request
        json = request.get_json(force=True)
        app = json["app"]
        id = json["id"]
        data = json["data"]

        print json

        return "Message received, cheers", 200

api.add_resource(Handler, "/receive")

app.run(debug=False)