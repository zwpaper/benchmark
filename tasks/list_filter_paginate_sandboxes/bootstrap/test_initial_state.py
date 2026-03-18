import os

def test_initial_state():
    assert not os.path.exists('/home/user/list_ci_sandboxes.py'), "list_ci_sandboxes.py should not exist initially"
    assert not os.path.exists('/home/user/ci_sandboxes.txt'), "ci_sandboxes.txt should not exist initially"
