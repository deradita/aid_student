from flask import Flask, request, render_template, flash, redirect, url_for, session, Response, render_template_string
from obj_ques import ObjectiveTest
from subj_ques import SubjectiveTest

app = Flask(__name__)

#app.secret_key= 'aica2'

# import nltk
# nltk.download("all")
# exit()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/test_generate', methods=["POST"])
def test_generate():
	if request.method == "POST":
		inputText = request.form["itext"]
		testType = request.form["test_type"]
		noOfQues = request.form["noq"]
		if testType == "objective":
			objective_generator = ObjectiveTest(inputText,noOfQues)
			question_list, answer_list = objective_generator.generate_test()
			testgenerate = zip(question_list, answer_list)
			return render_template('ques_gen.html', cresults = testgenerate)
		elif testType == "subjective":
			subjective_generator = SubjectiveTest(inputText,noOfQues)
			question_list, answer_list = subjective_generator.generate_test()
			testgenerate = zip(question_list, answer_list)
			return render_template('ques_gen.html', cresults = testgenerate)
		else:
			flash('Error Ocuured!')
			return redirect(url_for('/'))

@app.route('/summary_generate',  methods=["POST"])
def summary_generate():
	if request.method == "POST":
		inputText = request.form["itext"]
		summary_generator = SummaryText(inputText)
		summary_text=summary_generator.generate_summary()
		summarygenerate=zip(summary_text)
		return render_template('summ_gen.html', cresults=summarygenerate)
	
	else:
			flash('Error Ocurred!')
			return redirect(url_for('/'))

	
		





if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 5001, debug=True)