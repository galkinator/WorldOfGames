from flask import Flask
import os
from Utils import SCORES_FILE_NAME


app = Flask('gil')

HTML_TEMPLATE = """  
<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{SCORE}</div></h1>
</body>
</html>
"""

ERROR_TEMPLATE = """  
<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1><div id="score" style="color:red">{ERROR}</div></h1>
</body>
</html>
"""

@app.route("/score")
def score_server():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                score = file.read().strip()
                return HTML_TEMPLATE.replace("{SCORE}", score)
        else:
            return ERROR_TEMPLATE.replace("{ERROR}", "File not found")
    except Exception as e:
        return ERROR_TEMPLATE.replace("{ERROR}", str(e))

app.run(host="0.0.0.0", port=5001, debug=True)


