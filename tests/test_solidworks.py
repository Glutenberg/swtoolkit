import subprocess

import win32con
import win32gui
import win32process
import pytest
import psutil

from swtoolkit import SolidWorks


@pytest.fixture
def init_sldworks():
    if [p.name() for p in psutil.process_iter()].count("SLDWORKS.exe"):
        subprocess.call("Taskkill /IM SLDWORKS.exe /F")
    return SolidWorks()


@pytest.fixture
def visibility_state():
    """Gets the visibility state of SLDWORKS.exe via 3rd party package

    Returns True if window is visible; False if not. This function assumes that
    if the solidworks process is in the process list but does not return a
    win32 window handle based on the callback() logic then it must be
    invisible.
    """

    target_pid = [
        p.pid for p in psutil.process_iter() if p.name() == "SLDWORKS.exe"
    ]

    def callback(handle, handles):
        if win32gui.IsWindowEnabled(handle) and win32gui.IsWindowVisible(
            handle
        ):
            _, pid = win32process.GetWindowThreadProcessId(handle)
            if pid in target_pid:
                handles.append(handle)
        return True

    # Removes the error message box that SolidWorks triggers on Startup from
    # the list of handles used to determine if solidworks is visible
    MESSAGE_BOX_CLASS = 32770
    patch_handle = win32gui.FindWindow(
        MESSAGE_BOX_CLASS, "Microsoft Visual Basic for Applications"
    )

    handles = []
    win32gui.EnumWindows(callback, handles)
    return bool(
        [
            handle for handle in handles if bool(win32gui.GetWindowText(handle))
        ].remove(patch_handle)
    )


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


def test_pid(init_sldworks):
    """Check if PID returned by SolidWorks matches PID in process list"""
    sldworks = init_sldworks
    assert sldworks.pid in [
        p.pid for p in psutil.process_iter() if p.name() == "SLDWORKS.exe"
    ]


# @pytest.mark.xfail
def test_visible_get(init_sldworks, visibility_state):
    sldworks = init_sldworks
    assert sldworks.visible == visibility_state


def test_visible_set():
    pass


def test_frame_state_get():
    pass


def test_frame_state_set():
    pass


def test_open():
    pass


def test_shutdown():
    pass


def test_get_model():
    pass


def test_get_models():
    pass
