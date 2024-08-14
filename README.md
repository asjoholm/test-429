# test-429

### Description
Simple service to test how your application handles 429 (Too many requests) responses.
This is often overlooked and can cause your application to be rate limited.

Runs on port 5000 and responds with a 429 status code to whatever request is made.

### Usage
1. Install packages
```
pipenv install
```
2. Start the application
```
python app.py
```
3. Configure your application to send requests to http://localhost:5000
