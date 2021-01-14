import pytest
import subprocess
import psutil

from swtoolkit.api.com import COM


@pytest.fixture
def init_test_sldworks(teardown_sldworks):
    if "SLDWORKS.exe" in [p.name() for p in psutil.process_iter()]:
        teardown_sldworks


@pytest.fixture
def teardown_sldworks(com_reset):
    subprocess.call("Taskkill /IM SLDWORKS.exe /F")
    com_reset


@pytest.fixture
def com_reset():
    """Resets the COM instance in the COM class.

    COM is a Singleton. When the Solidworks instance the COM object is bound
    to is terminated during the session, the instance will need to be unbound.
    """

    COM.instance = None
