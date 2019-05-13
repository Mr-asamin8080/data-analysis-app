import csv
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)

@app.route("/")
def get_form():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def register():
    es = Elasticsearch('elasticsearch:9200')
    index = request.form['index']
    csv_file = request.form['csv_data']
    cf = csv.DictReader(csv_file)
    for row in cf:
        es.index(index=index, doc_type="1", body=row)
    return render_template('index.html')

@app.route("/search")
def root():
    return redirect("http://localhost:5601")

@app.route("/data")
def get_search_form():
    return render_template('search.html')

@app.route("/data", methods=["POST"])
def get_data():
    es = Elasticsearch('elasticsearch:9200')
    index = request.form['index']
    data = es.search(index=index, body={'query': {'match_all': {}}})
    return data
    # return render_template('search.html', records=temp, colnames=columnNames)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
