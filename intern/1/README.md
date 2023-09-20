# Intern Backend Developer Test Task

You have been tasked with writing a phone number validation service. Before proceeding with the implementation, we collected the requirements for the task.

At first, the platform on which your application will be deployed had a couple of requirements:
- the service must listen to port 7777 on the local host (127.0.0.1:7777)
- the `GET/ping` interface must respond with the status code 200 when the application is ready to process requests;
 - The HTTP interface `GET /shutdown` should immediately terminate the execution of the service (the status code is not important in this case).


Then we formulated the specification for the functional part of the service in the OpenAPI format: swagger: "2.0"
```yaml
paths:  
  /validatePhoneNumber:  
    get:  
      description: "API for validating phone numbers"  
      produces:  
      - "application/json"  
      parameters:  
      - name: "phone_number"  
        in: "query"  
        description: "Phone number"  
        required: true  
        type: "string"  
      responses:  
        "200":  
          description: "Successful operation"  
          schema:  
            oneOf:  
              - $$ref: "#/components/schemas/Success"  
              - $$ref: "#/components/schemas/Error"  
        "400":  
          description: "Invalid request"  
        "404":  
          description: "Not found"  
components:  
  schemas:  
    Success:  
      type: object  
      description: "This response is returned if a valid phone number is transmitted"  
      properties:  
        status:  
          type: "boolean"  
          description: "Validation result"  
        normalized:  
          type: "string"  
          description: "Normalized value of the form +7-###-###-####, where # is a digit"  
          example: "+7-912-123-4567"  
    Error:  
      type: object  
      description: "This response is returned if an invalid phone number is transmitted"  
      properties:  
        status:  
          type: "boolean"  
          description: "Validation result" A case-sensitive path is specified in the specification. The service must process the query parameters that are declared in the specification, the other parameters must be ignored.
```


Also:
 - Requests are encoded in the `HTTP/1.0` version.
 - In response to a request with an invalid `path`, we return the code 404.
 - In response to a request with incorrect `query` parameters, we return the code 400.
 - In other cases, we return code 200 with a detailed answer inside.


Phone numbers can have the following formats:
 - `+7 code ### ####`
 - `+7 (code) ### ####`
 - `+7code#######/code>`
 - `8(code)###-####`
 - `8code#######`

> Here `#` ~ digit, `code` ~ operator code from the list `[982, 986, 912, 934]`