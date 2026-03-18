import os
import re

def test_script_exists():
    assert os.path.exists('/home/user/list_ci_sandboxes.py'), "list_ci_sandboxes.py was not created"

def test_code_uses_correct_methods():
    with open('/home/user/list_ci_sandboxes.py', 'r') as f:
        code = f.read()
        
    assert "Sandbox.list" in code, "Code does not use Sandbox.list"
    assert "query" in code, "Code does not use the query parameter for filtering"
    assert "has_next" in code, "Code does not check paginator.has_next"
    assert "next_items" in code, "Code does not call paginator.next_items"
    assert "metadata" in code, "Code does not use metadata filtering"
    assert "ci" in code, "Code does not filter by 'ci' environment"
    assert "kill" in code, "Code does not kill the created sandboxes"

def test_output_file():
    assert os.path.exists('/home/user/ci_sandboxes.txt'), "ci_sandboxes.txt was not created"
    with open('/home/user/ci_sandboxes.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    assert len(lines) >= 3, f"Expected at least 3 sandbox IDs in ci_sandboxes.txt, found {len(lines)}"
    
    # Check if they look like sandbox IDs
    for sid in lines:
        assert re.match(r'^[a-zA-Z0-9_-]+$', sid), f"Invalid sandbox ID format: {sid}"
