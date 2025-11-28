# This will be the festive message generator!
from datetime import date
import holidays # you will need to pip install holidays if you haven't already
import time
import zmq


#structures to hold holidays
HOLIDAY = {
  	"Christmas Day": "Merry Christmas!",
  	"Thanksgiving Day": "Happy Thanksgiving!",
  	"Veterans Day": "Happy Veterans Day!",
  	"Juneteenth National Independence Day": "Happy Juneteenth Independence Day!",
  	"Independence Day": "Happy Independence Day!",
  	"Labor Day": "Happy Labor Day!",
  	"Martin Luther King Jr. Day": "Happy Martin Luther King Jr. Day!",
  	"New Year's Day": "Happy New Year!",
}



def get_message(holiday_type):
	today = date.today()
	# today = ('2025-11-27')
	h = holidays.US()
	message = None
	# if our current day is a holiday, return a message
	if today in h:
		today_holiday = h.get(today)
		print(today_holiday)
		message = HOLIDAY[today_holiday]
	
	return str(message)

def main():
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind('tcp://*:7777')
	print('Microservice is connected and running on port 7777')

	# very similar to Logan's random quotes
	try:
		while True:
			# should be a type of holiday(?)
			message = socket.recv_string()
            
			try:
				response = get_message(message)
			except ValueError:
				# TBA what the correct ask is
				response = 'Error. Send correct ask'
            
            # send the response back to client
			time.sleep(3)
			socket.send_string(response)

	except KeyboardInterrupt:
		print("Shutting down microservice...")
	finally:
        # ensure proper cleanup of zmq context
		context.destroy()

if __name__ == "__main__":
    main()

