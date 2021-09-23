
# Pytest commands
Code-along with https://calmcode.io/pytest/git.html <br>

*"A test can demonstrate the presence of a bug, but not the absence of it"* - Dijkstra



### Run all tests starting w/ 'test_' in 'tests' folder
`pytest`

### Run specific test
`pytest test_file.py::test_case1`

### Run test verbose and with print statements (-s)
`pytest -s --verbose`

### Check test coverage
**NOTE**: Requires that we have turned it into a package
**NOTE**: Requires `python -m pip install pytest-cov`
`pytest --cov blackjack`

### Export test coverage check to HTML
`pytest --cov blackjack --cov-report html`



