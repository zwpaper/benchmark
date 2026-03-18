As a platform engineer setting up sandboxed CI/CD, you need to manage and query multiple sandboxes efficiently. 

Write and execute a Python script `/home/user/list_ci_sandboxes.py` that performs the following steps:

1. Creates 3 sandboxes with metadata `{'env': 'ci', 'tier': 'runner'}` and 2 sandboxes with metadata `{'env': 'dev', 'tier': 'runner'}`.
2. Uses the `Sandbox.list()` method to filter and retrieve ONLY the sandboxes where `env` is `ci` and the state is either `running` or `paused`. You MUST use the `query` parameter for filtering.
3. Uses a pagination loop (checking `paginator.has_next` and calling `paginator.next_items()`) to collect all matching sandboxes. Even if they fit on one page, you must implement the loop to ensure robust pagination.
4. Writes the `sandbox_id` of all matching sandboxes to `/home/user/ci_sandboxes.txt`, one per line.
5. Finally, kills all 5 sandboxes you created to clean up resources.

Your script will be tested by running it and verifying that `/home/user/ci_sandboxes.txt` contains exactly the 3 sandbox IDs that match the `ci` environment.