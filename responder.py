# coding=utf-8
from flask import Flask, request
from flask_restful import Api, Resource

from simwood_service import send_text
from message_broker import get_final_confirmation

from BookingState import BookingState

app = Flask(__name__)
api = Api(app)

bookings_in_progress = dict()


class Handler(Resource):
    def post(self):
        json = request.get_json(force=True)

        self.handleResponse(json["data"]["originator"], json["data"]["message"])

        return "Message received, cheers", 200

    def handleResponse(self, originator, response):
        if originator not in bookings_in_progress:
            bookings_in_progress[originator] = BookingState(originator, response)

        booking = bookings_in_progress[originator]
        booking.putResponse(response)

        # Send out new question
        new_message = booking.getNextMessage()
        if new_message is not None:
            print "Sending {} to {}".format(new_message, originator)
            send_text(originator, new_message)
        else:
            send_text(originator, get_final_confirmation())
            booking.flushBooking()
            del bookings_in_progress[originator]


api.add_resource(Handler, "/receive")
app.run(host='0.0.0.0', debug=False, port=80)