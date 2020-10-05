# fib_challenge

Getting started

Repository Structure:
   - /fib_challenge
        - /__init__.py contains the flask application, contains the GET calculate_fibonacci route for the challenge
   - /tests
       - /__init__.py
       - /test_fib.py - contains the unittests for the calculate Fibonacci route
   - .travis.yml : THE CI/CD yaml file for Travis CI
   - Dockerfile : Contains the file that builds the image for the flask application
   - requirements.txt : contains the dependencies for the application
   - start_app.py : to run the application, even though you can use flask run, flask run CLI command is not recommended 
      for production. For the docker containers, you will use this file.
         
 Run this Application using Docker Containers 
 -----
First you'll need to get Docker for this project which can be found at:https://docs.docker.com/get-docker/ .
Once you have the source code for the project: 

Once you have successfully installed Docker, build the container image and verify it has been sucessfully built:

```bash
docker image build -t fibonacci_challenge .
docker image ls
```

To run the container: 
```bash
docker run -p 5001:5000 -d fibonacci_challenge
```
Once your image has ran succesfully, if using curl, you can hit the service using:
(Note in the example below 4 was used, but any integer should successfully generate a positive response)
```bash
 curl http://127.0.0.1:5001/calculate_fibonacci?num=4
```
Run Application without using containers
----
You will need to make sure you have Python 3.7.0+ installed which can be found here: https://www.python.org/downloads/
You do not need to worry about installing Pip as it is already provided with the version. 

```bash
pip install virtualenv
```

Create a virtualenv in which we can install the dependencies and install the dependencies
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Run the application:
```bash
export FLASK_APP=fib_challenge.py
flask run
```
Once your image has ran succesfully, if using curl, you can hit the service using:
(Note in the example below 4 was used, but any integer should successfully generate a positive response)
```bash
 curl http://127.0.0.1:5000/calculate_fibonacci?num=4
```

Run tests
----
To run tests locally using containers:
```bash
python -m unittest tests/test_fib.py
```
To run tests without using containers:
```bash
export FLASK_APP=fib_challenge/__init__.py
python -m unittest tests/test_fib.py
```







