import subprocess
import psutil

import pytest

from swtoolkit import SolidWorks


def test_start():
    """Checks if SolidWorks is in the process list before and after
    execution of start().
    """

    if "SLDWORKS.exe" in [p.name() for p in psutil.process_iter()]:
        subprocess.call("Taskkill /IM SLDWORKS.exe /F")
    SolidWorks.start()
    assert "SLDWORKS.exe" in [p.name() for p in psutil.process_iter()]


def test_kill():
    """Checks if SolidWorks is not in the process list before and after
    execution of kill().
    """

    if "SLDWORKS.exe" not in [p.name() for p in psutil.process_iter()]:
        SolidWorks.start()
    SolidWorks.kill()
    assert "SLDWORKS.exe" not in [p.name() for p in psutil.process_iter()]


def test_pid():
    """Check if PID returned by SolidWorks matches PID in process list"""
    assert SolidWorks().pid in [
        p.pid for p in psutil.process_iter() if p.name() == "SLDWORKS.exe"
    ]
