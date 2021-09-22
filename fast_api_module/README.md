
# FastAPI commands
Code-along @ https://calmcode.io/fastapi/hello-world.html <br>

### Install FastAPI and Uvicorn
`pip install fastapi uvicorn`

### Start server at local host
`uvicorn app:app --reload` then navigate to `http://127.0.0.1:8000` in browser

### Check docs for app
`http://127.0.0.1:8000/docs`

### Use "boom" to check effect of asynchronous calls
Run `pip install boom` first <br>
`boom http://127.0.0.1:8000/sleep_slow -c 200 -n 200`
`boom http://127.0.0.1:8000/sleep_fast -c 200 -n 200`

### Run pytests 
`pytest fast_api_module/test_app.py --verbose`