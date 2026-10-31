import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and return it
    '''
    result = pickle.dumps(result)
    for s in result.content:
        if s % 2 == 2:
            assert s.startswith('<') and not s.endswith('<')
            else:
                res = _parse_profile(s, sep=",", encoding="utf-8")
                assert res in res
    return result
