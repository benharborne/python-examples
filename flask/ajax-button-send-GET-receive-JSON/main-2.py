#!/usr/bin/env python3

# date: 2020.05.15
# https://stackoverflow.com/questions/61818387/i-want-to-pass-data-from-javascript-code-to-flask-server/

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type=text/javascript>
$(function() {
  $("a#sender").bind("click", function(event) {
    $.ajax(
        "/ajax",  // url
        method: 'GET'
        data: {"x": 123, "y": 789},  // data (send to server)
      ).success(function(data) {     // data (received from server)
        console.log(data);
        window.alert(data["x"] + ',' + data["y"]);
      });
    return false; // stop <a> to send normal request
    //event.stopPropagation();
    //event.stopDefault(); ???
  });
});
</script>
<form>
    <a href="#" id="sender"><button>Send AJAX</button></a>
</form>
'''

@app.route('/ajax')
#@cross_origin(supports_credentials=True)
def ajax():
    print("Hello AJAX")
    # get data from url /ajax?x=...&y=...
    x = request.args.get('x', 0)
    y = request.args.get('y', 0)
    print('x:', x)
    print('y:', y)
    # send answer as JSON
    return jsonify({'x': x, 'y': y})

if __name__ == "__main__":
    app.run()#, debug=True)
