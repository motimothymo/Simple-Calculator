# Simple Calculator
## Get Started
Build Docker first
```
docker-compose build
```
Then, run Docker containers
```
docker-compose up
```
Run the application on your web browser with URL below
```
127.0.0.1:5000
```
The default application will be redirected to
```
127.0.0.1:5000/api/prime/3
```
So, to access the application use the URL below
  ### Prime n<sup>th</sup>
    /api/prime/<int: n>
  ### Prime-Palindrome n<sup>th</sup>
    /api/prime/palindrome/<int: n>
