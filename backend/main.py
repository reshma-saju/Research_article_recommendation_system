from flask import Flask, redirect, url_for, request, render_template
from models.abstracttopaper import getRecommendation
from models.titlestopaper import title_getRecommendation
from models.abstract_summary import getSummary
from models.topic_modelling import getTopics

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"



@app.route('/recommendation', methods=['POST', 'GET'])
def reco():
    if request.method == 'POST':
        title = request.form['inp_title']
        abst = request.form['inp_abstract']
        result_abs=getRecommendation(abst)
        result_titl=title_getRecommendation(title)
        # return 'welcome %s' % title
        return render_template('rec_result.html', title_result=result_titl, abs_result=result_abs) 
    else:
        return "Method not allowed. Please use the POST method to access this route."


@app.route('/summary', methods=['POST', 'GET'])
def summ():
    if request.method == 'POST':
        input_text = request.form['inp_text']
        result_summ=getSummary(input_text)
        # return 'welcome %s' % title
        return render_template('summ_result.html', summary=result_summ) 
    else:
        return "Method not allowed. Please use the POST method to access this route."


@app.route('/topic_modelling', methods=['POST', 'GET'])
def topic():
    if request.method == 'POST':
        input_text = request.form['inp_text']
        hdp_topics, lda_topics = getTopics(input_text)
        # return 'welcome %s' % title
        return render_template('topic_result.html', hdp_result=hdp_topics, lda_result=lda_topics) 
    else:
        return "Method not allowed. Please use the POST method to access this route."

if __name__ == '__main__':
    app.run(debug=True)
