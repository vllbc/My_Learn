from flask import Flask,jsonify,abort,request
app = Flask(__name__)
books = [
    {
        'id': 1,
        'title': u'论语',
        'auther': u'孔子',
        'price': 18
    },
    {
        'id': 2,
        'title': u'道德经',
        'auther': u'老子',
        'price': 15
    }
]
@app.route("/api/v1/books",method=['GET'])
def get_tasks():
    return jsonify({'books':books})




app.run()
