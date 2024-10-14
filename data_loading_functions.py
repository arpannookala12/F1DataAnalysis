import requests
import pandas as pd

race_results_url = 'http://ergast.com/api/f1/current/last/results.json'
response = requests.get(race_results_url)
data = response.json()

def fetch_race_results():
    """Process race results data to format suitable for saving to database."""
    race_results_url = 'http://ergast.com/api/f1/current/last/results.json'
    response = requests.get(race_results_url)
    data = response.json()
    races = data['MRData']['RaceTable']['Races']
    if races:
        race = races[0]
        results = race['Results']
        df = pd.DataFrame({
            'season': race['season'],
            'race_name': race['raceName'],
            'round': race['round'],
            'position': [result['position'] for result in results],
            'driver_id': [result['Driver']['driverId'] for result in results],
            'constructor_id': [result['Constructor']['constructorId'] for result in results],
            'laps': [result['laps'] for result in results],
            'time': [result.get('Time', {}).get('time', 'N/A') for result in results],
            'points': [result['points'] for result in results]
        })
        return df
    return pd.DataFrame()

def fetch_qualifying_results():
    race_results_url = 'http://ergast.com/api/f1/current/last/qualifying.json'
    response = requests.get(race_results_url)
    data = response.json()
    races = data['MRData']['RaceTable']['Races']
    if races:
        qualifyings = races[0]['QualifyingResults']
        df = pd.DataFrame({
            'season': races[0]['season'],
            'race_name': races[0]['raceName'],
            'round': races[0]['round'],
            'position': [qualifying['position'] for qualifying in qualifyings],
            'driver_id': [qualifying['Driver']['driverId'] for qualifying in qualifyings],
            'constructor_id': [qualifying['Constructor']['constructorId'] for qualifying in qualifyings],
            'q1': [qualifying.get('Q1', 'N/A') for qualifying in qualifyings],
            'q2': [qualifying.get('Q2', 'N/A') for qualifying in qualifyings],
            'q3': [qualifying.get('Q3', 'N/A') for qualifying in qualifyings]
        })
        return df
    return pd.DataFrame()

def fetch_pit_stops():
    race_results_url = 'http://ergast.com/api/f1/current/last/pitstops.json'
    response = requests.get(race_results_url)
    data = response.json()
    races = data['MRData']['RaceTable']['Races']
    if races:
        pit_stops = races[0].get('PitStops', [])
        df = pd.DataFrame({
            'season': races[0]['season'],
            'round': races[0]['round'],
            'race_name': races[0]['raceName'],
            'driver_id': [pit['driverId'] for pit in pit_stops],
            'stop': [pit['stop'] for pit in pit_stops],
            'lap': [pit['lap'] for pit in pit_stops],
            'time': [pit['time'] for pit in pit_stops],
            'duration': [pit['duration'] for pit in pit_stops]
        })
        return df
    return pd.DataFrame()

def fetch_constructor_standings():
    race_results_url = 'http://ergast.com/api/f1/current/last/constructorStandings.json'
    response = requests.get(race_results_url)
    data = response.json()
    standings = data['MRData']['StandingsTable']['StandingsLists']
    standings1 = data['MRData']['StandingsTable']['StandingsLists']
    if standings:
        standings = standings[0]['ConstructorStandings']
        df = pd.DataFrame({
            'season': standings1[0]['season'],
            'round': standings1[0]['round'],
            'constructor_id': [standing['Constructor']['constructorId'] for standing in standings],
            'position': [standing['position'] for standing in standings],
            'points': [standing['points'] for standing in standings],
            'wins': [standing['wins'] for standing in standings]
        })
        return df
    return pd.DataFrame()

