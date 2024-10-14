import pytest
import pandas as pd

# Assuming the functions to fetch data are named fetch_race_results, fetch_qualifying_results, etc.

from data_loading_functions import fetch_race_results, fetch_qualifying_results, fetch_pit_stops, fetch_constructor_standings

def test_race_results():
    df = fetch_race_results()
    assert not df.isnull().values.any(), "Dataframe contains NaN values"
    assert len(df) > 1, "Dataframe has too few rows"

def test_qualifying_results():
    df1 = fetch_qualifying_results()
    assert not df1.isnull().values.any(), "Dataframe contains NaN values"
    assert len(df1) > 1, "Dataframe has too few rows"

def test_pit_stops():
    df2 = fetch_pit_stops()
    assert not df2.isnull().values.any(), "Dataframe contains NaN values"
    assert len(df2) > 0, "Dataframe has no rows"

def test_constructor_standings():
    df3 = fetch_constructor_standings()
    assert not df3.isnull().values.any(), "Dataframe contains NaN values"
    assert len(df3) > 1, "Dataframe has too few rows"

