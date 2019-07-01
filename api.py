from flask import Flask, jsonify, request
from dateutil.parser import parse
import pandas as pd

app = Flask(__name__)

#File cached as Pandas DataFrame
file = 'https://srv-file4.gofile.io/download/j84UTV/pickup_times.csv'
# file = 'pickup_times.csv'
df = pd.read_csv(file)
print('+++++++++')
print(df.columns)
df.columns = ['location_id', 'timestamp', 'pickup_time']
print(df.columns)
print('+++++++++')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp')
df = df.tz_localize(None)

@app.route('/median_pickup_time', methods=['GET'])
def median_pickup_time():
    location_id = request.args.get("location_id", 0, type=int)
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")

    #Check if all arguments are available and in correct format
    if (not location_id) or (not start_time) or (not end_time) or (not is_datetime(start_time)) or (not is_datetime(end_time)):
        data = {
            'message'  : 'Please send appropriate request'
        }
        response = jsonify(data)
        response.status_code = 400
        return response

    else:
        median = calculate_median(location_id, start_time, end_time)
        data = {
            'median'  : median
        }
        response = jsonify(data)
        response.status_code = 200
        return response

def calculate_median(location_id, start_time, end_time):
    mydf = df.loc[df['location_id'] == location_id]
    mydf = mydf[start_time:end_time]
    #Check if given parameters return any results
    if mydf.empty:
        return 0
    else:
        return mydf['pickup_time'].median()

#Checks if given string could be parsed as datetime
def is_datetime(datetimestr):
    try:
        parse(datetimestr)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    app.run()
