# fib_challenge

Getting started

First you'll need to get Docker for this project which can be found at:https://docs.docker.com/get-docker/ .
Once you have the source code for the project: 

Once you have succesfully installed Docker, build the container image and verify it has been sucessfully built:

```bash
docker image build -t fibonacci_challenge .
docker image ls
```

To run the container: 
```bash
docker run -p 5001:5000 -d fibonacci_challenge
```




