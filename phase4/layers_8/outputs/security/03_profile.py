from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request,  make a response with it and return it
    '''
    result = pickle.dumps(Flask, name="my_client")

    if result.status == 200:
        return result.status

    if result.json()["username"]:
        return result.user.code
    return result
