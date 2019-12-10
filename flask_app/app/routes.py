from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# In this example there are two decorators, which associate the URLs / and /index to this function. 
# This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser as a response.