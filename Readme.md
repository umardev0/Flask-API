# Median Time Calculator

|build status|_

[![Build Status](https://travis-ci.org/umardev0/Flask-API.svg?branch=master)](https://travis-ci.org/umardev0/Flask-API)

This is a REST API built with Flask in Python to calculate median pick up time for a location.

## Installation

Make sure you have Python installed on your system. You can check it by running:

```bash
$python --version
```
Code is tested for both Python-2.7.16 and Python-3.7.3.

Clone the repository and switch working directory.

```bash
$cd path/to/cloned/repository/
```
Make virtual environment for your respective python version and activate it:

```bash
$virtualenv /path/to/venv/
$source /path/to/venv/bin/activate
```
Install the required libraries by running:

```bash
$pip install -r requirements.txt
```

## Usage

Run the api by executing:

```bash
$python api.py
```
Once the API is running, open browser or any REST client like Postman or Restlet and go to API address as displayed in Terminal:

```
127.0.0.1:5000/median_pickup_time?location_id=12&start_time=2019-01-09T11:00:00&end_time=
2019-01-09T12:00:00
```
### Testing
To start the test suite simply run:

```bash
$pytest
```

### Changing source file
You can change the source file by simply replacing **pickup_times.csv** with new file. New file needs to have same name. You can also give url of file by changing following code:

```
# file = 'https://srv-file4.gofile.io/download/j84UTV/pickup_times.csv'
file = 'pickup_times.csv'
```

### Heroku Deployment (Optional)
You can deploy the API to Heroku also. Required libraries and settings have been added in the source code. The deployed API can be tested from following link.

```
https://umardev0-wolt.herokuapp.com/median_pickup_time?location_id=12&start_time=2019-01-09T11:00:00&end_time=2019-01-09T12:00:00
```
