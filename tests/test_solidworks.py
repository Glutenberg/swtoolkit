import subprocess

import win32gui
import win32process
import pytest
import psutil


from swtoolkit import SolidWorks
from swtoolkit.api.com import COM


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

    handles = []
    win32gui.EnumWindows(callback, handles)

    handle_list = [
        handle for handle in handles if bool(win32gui.GetWindowText(handle))
    ]

    # Removes the error message box that SolidWorks triggers on Startup from
    # the list of handles used to determine if solidworks is visible
    MESSAGE_BOX_CLASS = 32770
    patch_handle = win32gui.FindWindow(
        MESSAGE_BOX_CLASS, "Microsoft Visual Basic for Applications"
    )

    if patch_handle in handle_list:
        handle_list.remove(patch_handle)

    return bool(handle_list)


def test_start(init_test_sldworks):
    """Checks if SolidWorks is in the process list before and after
    execution of start().
    """
    init_test_sldworks
    SolidWorks.start()
    assert "SLDWORKS.exe" in [p.name() for p in psutil.process_iter()]


def test_kill(init_test_sldworks):
    """Checks if SolidWorks is not in the process list before and after
    execution of kill().
    """

    if "SLDWORKS.exe" not in [p.name() for p in psutil.process_iter()]:
        SolidWorks.start()
    SolidWorks.kill()
    assert "SLDWORKS.exe" not in [p.name() for p in psutil.process_iter()]


def test_pid(init_test_sldworks):
    """Check if PID returned by SolidWorks matches PID in process list"""

    init_test_sldworks
    SolidWorks.start()
    assert SolidWorks().pid in [
        p.pid for p in psutil.process_iter() if p.name() == "SLDWORKS.exe"
    ]


def test_visible_get(init_test_sldworks):
    init_test_sldworks
    assert SolidWorks().visible is False


def test_visible_set(init_test_sldworks):
    init_test_sldworks
    SolidWorks().visible = True
    assert SolidWorks().visible is True


def test_open():
    pass


def test_shutdown():
    pass


def test_get_model():
    pass


def test_get_models():
    pass
