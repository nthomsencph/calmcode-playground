
# Bandit commands
Keep python safe!
Code-along @ https://calmcode.io/bandit/introduction.html <br>

## Install bandit
`pip install bandit`

## Run bandit on single file
`bandit bad.py` will output the following 

    [main]  INFO    profile include tests: None
    [main]  INFO    profile exclude tests: None
    [main]  INFO    cli include tests: None
    [main]  INFO    cli exclude tests: None
    [main]  INFO    running on Python 3.8.11
    [node_visitor]  INFO    Unable to find qualified name for module: bad.py
    Run started:2021-09-23 09:20:56.188575

    Test results:
        >> Issue: [B102:exec_used] Use of exec detected.
        Severity: Medium   Confidence: High
        Location: bad.py:5
        More Info: https://bandit.readthedocs.io/en/latest/plugins/b102_exec_used.html
    4
    5       exec(cmd)

    --------------------------------------------------

    Code scanned:
            Total lines of code: 3
            Total lines skipped (#nosec): 0

    Run metrics:
            Total issues (by severity):
                    Undefined: 0.0
                    Low: 0.0
                    Medium: 1.0
                    High: 0.0
            Total issues (by confidence):
                    Undefined: 0.0
                    Low: 0.0
                    Medium: 0.0
                    High: 1.0
    Files skipped (0):

Essentially, it is telling us that `exec` is being used and that it estimated a `Medium` insecurity severity with `High` confidence. Specifically, this is triggered by `bad.py:5`

## Run bandit on all python files in module
the `-r` command means that the scan is run recursively.
     
    bandit -r <module>

## shield a line from bandit
Simply add a `#nosec` comment.

    ...
    with urllib.requests.urlopen(path) as resp: #nosec
        ...


## Add bandit as pre-commit hook
Create `.pre-commit-config.yaml` file/insert the statements below

    -   repo: https://github.com/Lucas-C/pre-commit-hooks-bandit
        rev: v1.0.5
        hooks:
        -   id: python-bandit-vulnerability-check
            args: [--skip, "B101", --recursive, clumper]

