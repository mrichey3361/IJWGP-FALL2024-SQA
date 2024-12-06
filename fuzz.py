from src.main import giveTimeStamp
from src.main import getCSVData
from src.log.op.miner import checkIfParsablePython
from src.main import getAllPythonFilesinRepo
from src.main import runFameML


from hypothesis import given
from hypothesis.strategies import text
from unittest.mock import patch
import pytest
import os

@given(text())
def test_giveTimeStamp(input_string):
    try:
        timestamp = giveTimeStamp()
        assert isinstance(timestamp, str)
        assert len(timestamp) > 0
    except Exception as e:
        pytest.fail(f"Failed to generate timestamp: {e}")

@given(text())
def test_getCSVData(file_path):
    try:
        dic_ = {file_path: "fake value"}
        dir_repo = "fake_repo_path"
        data = getCSVData(file_path, dic_)
        assert isinstance(data, list)
        assert len(data) > 0
    except Exception as e:
        pytest.fail(f"Failed to get CSV data: {e}")

@given(text())
def test_getAllPythonFilesinRepo(path2dir):
    try:
        if not os.path.exists(path2dir):
            os.makedirs(path2dir)
        files = getAllPythonFilesinRepo(path2dir)
        assert isinstance(files, list)
        assert all(isinstance(file, str) for file in files)
        shutil.rmtree(path2dir)

    except Exception as e:
        pytest.fail(f"Failed to get Python files {path2dir}: {e}")

@given(text())
def test_checkIfParsablePython(pyFile):
    try:
        with open(pyFile, "w") as f:
            f.write("print('Hello, World!')")
            f.close()
        checkIfParsablePython(pyFile)
    except Exception as e:
        pytest.fail(f"Failed to check if file is parsable Python: {e}")
    finally:
        if os.path.exists(pyFile):
            os.remove(pyFile)

@pytest.mark.parametrize(
    "inp_dir, csv_fil",
    [("/mock/repo", "/mock/csv_file.csv")]
)
@patch("src.main.runFameML")
def test_runFameML(mock_runFameML, inp_dir, csv_fil):
    mock_runFameML.return_value = None

    try:
        runFameML(
            inp_dir=inp_dir,
            csv_fil=csv_fil,
            threshold=0.5,
            max_files=100,
            max_lines=1000,
            max_functions=50,
            max_imports=20,
            max_loc=500,
            max_cyclo=10,
            max_atfd=5,
            max_nopa=10,
            max_cog=2,
            max_wmc=100,
            max_rfc=20,
            max_lcom=5,
            max_ca=10,
            max_ce=5,
            max_nose=1,
            max_fanout=5,
            max_loc_threshold=100,
            max_cyclo_threshold=5,
            max_atfd_threshold=10,
            max_nopa_threshold=5,
            max_cog_threshold=2,
            max_wmc_threshold=50,
            max_rfc_threshold=10,
            max_lcom_threshold=5,
            max_ca_threshold=5,
            max_ce_threshold=5,
            max_nose_threshold=1,
            max_fanout_threshold=5
        )
        mock_runFameML.assert_called_once_with(
            inp_dir=inp_dir,
            csv_fil=csv_fil,
            threshold=0.5,
            max_files=100,
            max_lines=1000,
            max_functions=50,
            max_imports=20,
            max_loc=500,
            max_cyclo=10,
            max_atfd=5,
            max_nopa=10,
            max_cog=2,
            max_wmc=100,
            max_rfc=20,
            max_lcom=5,
            max_ca=10,
            max_ce=5,
            max_nose=1,
            max_fanout=5,
            max_loc_threshold=100,
            max_cyclo_threshold=5,
            max_atfd_threshold=10,
            max_nopa_threshold=5,
            max_cog_threshold=2,
            max_wmc_threshold=50,
            max_rfc_threshold=10,
            max_lcom_threshold=5,
            max_ca_threshold=5,
            max_ce_threshold=5,
            max_nose_threshold=1,
            max_fanout_threshold=5
        )
    except Exception as e:
        pytest.fail(f"Failed to run FameML: {e}")
