import pandas as pd
import pyodbc
import json

from flask import Flask, render_template, redirect, request, session, url_for

from queries import current_sql, hourly_sql, daily_sql
from database_connector import query_executor
from secrets import psql_dsn

app = Flask(__name__)

@app.route('/')
def _():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/location/<location>')
def route_location(location):
    psql_connector = query_executor(pyodbc.connect(f"DSN={psql_dsn}"))

    current = psql_connector.get_results(current_sql, location, result_format="dict-list")
    hourly_forecast = psql_connector.get_results(hourly_sql, location, result_format="dict-list")
    daily_forecast = psql_connector.get_results(daily_sql, location, result_format="dict-list")

    psql_connector.close_()

    return render_template(
        'location_view.html', 
        current=json.loads(json.dumps(current)), 
        hourly_forecast=json.loads(json.dumps(hourly_forecast)), 
        daily_forecast=json.loads(json.dumps(daily_forecast))
    )

if __name__ == '__main__':
   app.run()
