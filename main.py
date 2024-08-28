from flask import Flask,render_template,request,jsonify
from summarizer import summarize_text

app=Flask(__name__)

@app.route("/")
def textSummarizer():
    return render_template('textSummarizer.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text_to_summarize = request.form.get('text_to_summarize')

    if 200 < len(text_to_summarize) < 100000:
        summary =summarize_text(text_to_summarize)
    else:
        summary = "The input text must be between 200 and 100000 characters."

    return render_template('textSummarizer.html', summary=summary)

if __name__==('__main__'):
    app.run(debug=True)
