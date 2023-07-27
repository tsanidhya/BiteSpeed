
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



To run the app: run the command "docker compose up --build" in the terminal inside the root directory.
The identify endpoint is hosted on localhost : 5000
PostgreSQL database is hosted on localhost : 5432

**note : both services are hosted inside docker

db_name = postgres,
Username = postgres,
password = postgres

Link : localhost:5000/contact/identify
HTTP Method : POST



