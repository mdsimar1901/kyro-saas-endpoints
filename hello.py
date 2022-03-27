import flask
from flask import request,jsonify

completeddetails = [
    {
        "id":1,
        "projectname":"PP2600 - Project name",
        "schedule":"Baseline Schedule",
        "type":"Line Design Engineering",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"100.00%"
    },
    {
        "id":2,
        "projectname":"TD1330 - Project name",
        "schedule":"TxDOT Permits Acquired",
        "type":"Line Design Engineering",
        "duration":"06/01/2020 - 06/01/2020",
        "percentage":"100.00%"
    },
    {
        "id":3,
        "projectname":"PP2600 - Project name",
        "schedule":"Easements, Permits, Licenses etc. Acquired",
        "type":"Line Design Engineering",
        "duration":"6/11/2020 - 06/11/2020",
        "percentage":"100.00%"
    },
    {
        "id":4,
        "projectname":"PP1200 - Project name",
        "schedule":"Baseline Schedule",
        "type":"Line Design Engineering",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"100.00%"
    },
    {
        "id":3,
        "projectname":"PP2600 - Project name",
        "schedule":"Easements, Permits, Licenses etc. Acquired",
        "type":"Line Design Engineering",
        "duration":"6/11/2020 - 06/11/2020",
        "percentage":"100.00%"
    }
]

progres = [
    {
        "id":1,
        "projectname":"TD1160 - Project name",
        "schedule":"Baseline Schedule",
        "type":"Line Design Engineering",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"47.00%",
        "predictedduration":"86 days"
    },
    {
        "id":2,
        "projectname":"TD1330 - Project name",
        "schedule":"TxDOT Permits Acquired",
        "type":"Line Design Engineering",
        "duration":"06/01/2020 - 06/01/2020",
        "percentage":"25.00%",
        "predictedduration":"122 days"
    },
    {
        "id":3,
        "projectname":"PP2600 - Project name",
        "schedule":"Easements, Permits, Licenses etc. Acquired",
        "type":"Line Design Engineering",
        "duration":"6/11/2020 - 06/11/2020",
        "percentage":"70.00%",
        "predictedduration":"34 days"
    },
    {
        "id":4,
        "projectname":"PP1200 - Project name",
        "schedule":"Baseline Schedule",
        "type":"Line Design Engineering",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"0.00%",
        "predictedduration":"142 days"
    },
    {
        "id":5,
        "projectname":"TD1160 - Project name",
        "schedule":"File aCCN Documents",
        "type":"CCN Activities",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"0.00%",
        "predictedduration":"142 days"
    },
    {
        "id":3,
        "projectname":"PP2600 - Project name",
        "schedule":"Easements, Permits, Licenses etc. Acquired",
        "type":"Line Design Engineering",
        "duration":"6/11/2020 - 06/11/2020",
        "percentage":"0.00%",
        "predictedduration":"224 days"
    }
]

todo = [
    {
        "id":1,
        "projectname":"TD1160 - Project name",
        "schedule":"Baseline Schedule",
        "type":"Line Design Engineering",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"0.00%",
        "predictedduration":"142 days"
    },
    {
        "id":2,
        "projectname":"TD1330 - Project name",
        "schedule":"TxDOT Permits Acquired",
        "type":"Line Design Engineering",
        "duration":"06/01/2020 - 06/01/2020",
        "percentage":"00.00%",
        "predictedduration":"167 days"
    },
    {
        "id":3,
        "projectname":"PP2600 - Project name",
        "schedule":"Easements, Permits, Licenses etc. Acquired",
        "type":"Line Design Engineering",
        "duration":"6/11/2020 - 06/11/2020",
        "percentage":"0.00%",
        "predictedduration":"224 days"
    },
    {
        "id":4,
        "projectname":"PP1200 - Project name",
        "schedule":"Baseline Schedule",
        "type":"Line Design Engineering",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"0.00%",
        "predictedduration":"142 days"
    },
    {
        "id":5,
        "projectname":"TD1160 - Project name",
        "schedule":"File aCCN Documents",
        "type":"CCN Activities",
        "duration":"08/10/2022 - 08/10/2022",
        "percentage":"0.00%",
        "predictedduration":"142 days"
    },
    {
        "id":7,
        "projectname":"PP2600 - Project name",
        "schedule":"Easements, Permits, Licenses etc. Acquired",
        "type":"Line Design Engineering",
        "duration":"6/11/2020 - 06/11/2020",
        "percentage":"0.00%",
        "predictedduration":"224 days"
    }
]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Home</h1>"

@app.route('/completeddetails',methods=['GET'])
def cdetails():
    return jsonify(completeddetails)

@app.route('/progress', methods=['GET'])
def progress():
    return jsonify(progres)

@app.route('/tododetails', methods=['GET'])
def tododet():
    return jsonify(todo)





app.run()