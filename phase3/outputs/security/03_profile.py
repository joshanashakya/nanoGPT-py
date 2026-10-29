from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request,  make a response with it and return it
    '''
    mod = Flask()
    ma_key = mod.spen.McaskFor(copy=True)
    ma_key = None
    br_obj = mod.spen.McaskGetModeRephScore(moid=moid)
    br_obj._mix_base = None
