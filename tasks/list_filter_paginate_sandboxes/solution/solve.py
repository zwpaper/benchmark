import os
from e2b_code_interpreter import Sandbox

# Create sandboxes
ci_sandboxes = []
for _ in range(3):
    sbx = Sandbox(metadata={'env': 'ci', 'tier': 'runner'})
    ci_sandboxes.append(sbx)

dev_sandboxes = []
for _ in range(2):
    sbx = Sandbox(metadata={'env': 'dev', 'tier': 'runner'})
    dev_sandboxes.append(sbx)

# List, filter, and paginate
paginator = Sandbox.list(
    query={
        "metadata": {"env": "ci"},
        "state": ["running", "paused"]
    },
    limit=2 # Force pagination to test the loop
)

matching_ids = []
while True:
    items = paginator.next_items()
    for item in items:
        matching_ids.append(item.sandbox_id)
    if not paginator.has_next:
        break

# Write to file
with open('/home/user/ci_sandboxes.txt', 'w') as f:
    for sid in matching_ids:
        f.write(f"{sid}\n")

# Kill all created sandboxes
for sbx in ci_sandboxes + dev_sandboxes:
    sbx.kill()
