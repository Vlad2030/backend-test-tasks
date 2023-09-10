# Junior Backend Developer Test Task

You need to develop a asynchronous REST API for managing pets (dogs and cats).

You should use:
- Your prefer programming language
- Backend framework
- Your prefer Database
- Database ORM
- Docker-compose

The result of the task should be uploaded to a public Git repository.

## API
You need to implement the following endpoints:

#### POST /pets/
Create a pet 

##### *request body*
```json
{
  // to be designed 
}
```

##### *response body*
```json
{
  "id": 1,
  "name": "boy",
  "age": 7,
  "type": "dog",
  "created_at": "2021-05-18T19:10:17"
}
```

#### GET /pets/
Get a list of pets 

##### query parameters :
  `limit: integer (optional, default=20)`

##### *response body*
```json
{
  "count": 2,
  "items": [
    {
      "id": 1,
      "name": "boy",
      "age": 7,
      "type": "dog",
      "created_at": "2021-05-18T19:10:17"
    },
    {
      "id": 2,
      "name": "girl",
      "age": 3,
      "type": "cat",
      "created_at": "2021-04-11T22:39:58"
    }
  ]
}
```

#### DELETE /pets/
Delete pets

##### *request body*
```json
{
  "ids": [
    1,
    2,
    3
  ]
}
```

##### *response body*
```json
{
  "deleted": 2,
  "errors": [
    {
      "id": 1,
      "error": "Pet with the matching ID was not found."
    }
  ]
}
```

## Deployment Automation
You need to containerize the application you've developed.

Write a `Dockerfile` that:
- Downloads a base image from DockerHub
- Copies the application inside the image
- Installs necessary packages and dependencies (DB, requirements.txt, etc.)
- Configures all required components for the application to run
- Launches the application on port 3000

And write a `docker-compose.yaml` which runs your backend service and a PostgreSQL database

## Final Outcome
On a PC with Docker installed, it should be possible to clone the repository with the application's source code.

After executing the `docker-compose up -d` command, the application should respond to API calls at `127.0.0.1:3000`.