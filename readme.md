
Project Description : The project aims to develop a robust and efficient Contact Management Service using Flask, a Python micro web framework. The service will provide API endpoints to handle POST requests for fetching and updating data from a PostgreSQL database. Additionally, the entire application is containerized using Docker for seamless deployment and scalability.

requirements.txt consists of all the dependencies for this project.

Request format: the request body should be in a JSON format as given below 

{
"email" : "xyz@gmail.com",
"phoneNumber" : "12233"
}

response format: 	
		{
			"contact":{
				"primaryContatctId": 11,
				"emails": ["george@hillvalley.edu","biffsucks@hillvalley.edu"]
				"phoneNumbers": ["919191","717171"]
				"secondaryContactIds": [27]
		}
	}



To run the app on Docker locally: run the command "docker compose up --build" in the terminal inside the root directory.
The identify endpoint is hosted on localhost : 5000
PostgreSQL database is hosted on localhost : 5432

*note : both services are hosted inside docker

URL : localhost:5000/contact/identify
HTTP Method : POST

Alternatively the app in deployed on render.com

URL : https://bitespeed-app.onrender.com/contact/identify
HTTP method : POST

DB_configs are maintained in config/static_configs.py

*Switch to DB_URI which is commented out(line 2) for hitting local postgres service if using docker compose.

note - this app was developed on a Intel machine and docker compose might differently on apple silicon chips.

*** 
As mentioned on Render.com web services documentation:
Web Services on the free instance type are automatically spun down after 15 minutes of inactivity. When a new request for a free service comes in, Render spins it up again so it can process the request.
This will cause a delay in the response of the first request after a period of inactivity while the instance spins up.
***





