from flask import *
from functools import reduce

app = Flask(__name__)

@app.route('/sum', methods=["GET"])
def sum():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        return make_response(f"<p>The result of {a}+{b} is: {a+b}<p>")
    except:
        r = make_response("<p>Invalid inputs<p>")
        r.status_code = 403
        return make_response("<p>Invalid inputs<p>")

@app.route('/average', methods=["GET"])
def average():
    try:
        average = (reduce(lambda x, y: int(x) + int(y), request.args.values())) / len(request.args)
        return make_response(f"<p>The result of the average of {request.args.values()} is: {average}<p>")
    except:
        r = make_response("<p>Invalid inputs<p>")
        r.status_code = 403
        return make_response("<p>Invalid inputs<p>")
# התמונה בתוך DATA

## Main ##
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)