import pytest
import subprocess
import psutil

from swtoolkit.api.com import COM


@pytest.fixture(autouse=True)
def setup_sldworks():
    pass


@pytest.fixture
def teardown_sldworks(com_reset):
    yield
    if "SLDWORKS.exe" in [p.name() for p in psutil.process_iter()]:
        subprocess.call("Taskkill /IM SLDWORKS.exe /F")
    com_reset


@pytest.fixture
def com_reset():
    """Resets the COM instance in the COM class.

    COM is a Singleton. When the Solidworks instance the COM object is bound
    to is terminated during the session, the instance will need to be unbound.
    """

    COM.instance = None


# def pytest_sessionfinish(session, exitstatus):
#     COM.instance = None
#     if "SLDWORKS.exe" in [p.name() for p in psutil.process_iter()]:
#         subprocess.call("Taskkill /IM SLDWORKS.exe /F")
