
from flask import Flask, jsonify, request
from pybaseball import statcast, playerid_lookup, batting_stats_range, pitching_stats_range
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'vULTIMA is online ðŸ”¥'})

@app.route('/statcast')
def get_statcast():
    start = request.args.get('start', default="2024-08-01")
    end = request.args.get('end', default="2024-08-02")
    data = statcast(start_dt=start, end_dt=end)
    return data.head(20).to_json(orient='records')

@app.route('/playerid/<firstname>/<lastname>')
def get_playerid(firstname, lastname):
    ids = playerid_lookup(lastname, firstname)
    return ids.to_json(orient='records')

@app.route('/batting-stats')
def get_batting_stats():
    start = request.args.get('start', default="2024-04-01")
    end = request.args.get('end', default="2024-08-01")
    stats = batting_stats_range(start, end)
    return stats.head(20).to_json(orient='records')

@app.route('/pitching-stats')
def get_pitching_stats():
    start = request.args.get('start', default="2024-04-01")
    end = request.args.get('end', default="2024-08-01")
    stats = pitching_stats_range(start, end)
    return stats.head(20).to_json(orient='records')

if __name__ == '__main__':
    app.run()
