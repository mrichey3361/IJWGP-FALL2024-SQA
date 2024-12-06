import time
import datetime
import os
import pandas as pd
import numpy as np
import pytest
from hypothesis import given
from hypothesis.strategies import integers

from FAME_ML.main import giveTimeStamp, getCSVData, getAllPythonFilesinRepo, runFameML

@given(integers(min_value=-999999999, max_value=999999999))
def test_giveTimeStamp(mocked_time):
    original_time = time.time
    time.time = lambda: mocked_time
    try:
        if not isinstance(giveTimeStamp(), str):
             raise AssertionError("giveTimeStamp() did not return a string")
    except Exception as e:
        print(f"Error for time {mocked_time}: {e}")
    finally:
        time.time = original_time

def test_getCSVData():
    try:
        dic_ = {"test_script_1": "data", "test_script_2": "data"}
        dir_repo = "/invalid/path"
        result = getCSVData(dic_, dir_repo)
        if not isinstance(result, str):
            raise AssertionError("getCSVData() did not return a string")
    except Exception as e:
        print(f"Error in test_getCSVData: {e}")

def test_getAllPythonFilesinRepo():
    try:
        result = getAllPythonFilesinRepo("/invalid/path")
        if not isinstance(result, list):
             raise AssertionError("getAllPythonFilesinRepo() did not return a list")
    except Exception as e:
        print(f"Error in test_getAllPythonFilesinRepo: {e}")

def test_runFameML():
    try:
        input_dir = "/invalid/input/dir"
        output_csv = "/invalid/output/file.csv"
        result = runFameML(input_dir, output_csv)
        if not isinstance(result, str):
             raise AssertionError("runFameML() did not return a string")
    except Exception as e:
        print(f"Error in test_runFameML: {e}")

def test_time_time():
    try:
        edge_case_times = [-1, 0, 1, 9999999999, -9999999999, 9_223_372_036_854_775_808]
        for mock_time in edge_case_times:
            original_time = time.time
            time.time = lambda: mock_time
            result = giveTimeStamp()
            time.time = original_time
            if not isinstance(result, str):
                 raise AssertionError(f"giveTimeStamp() did not return a string for time {mock_time}")
    except Exception as e:
        print(f"Error in test_time_time: {e}")

if __name__ == "__main__":
    pytest.main()
