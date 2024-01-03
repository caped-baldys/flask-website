import pandas as pd
# from wtforms.form import Form
# from flask.ext.wtf import Form, TextField, BooleanField, FileField, file_required, RadioField
# from flask.ext.wtf import Required


questions = pd.read_csv('questions.csv', encoding="cp1252")

que = questions['Column2']
n = len(que)
print(n)
optionA = questions['A']
optionB = questions['B']
optionC = questions['C']
optionD = questions['D']
optionE = questions['E']

# class Question():
#     """
#     a record for each question for the quizes
#     """
#     __tablename__ = "questions"

#     question = questions['Column2']
#     choice1 = questions['A']
#     choice2 = questions['B']
#     choice3 = questions['C']
#     choice4 = questions['D']


# class QuizForm(Form):
#     q1 = RadioField(validators=[InputRequired()])
#     q2 = RadioField(validators=[InputRequired()])
#     q3 = RadioField(validators=[InputRequired()])
#     q4 = RadioField(validators=[InputRequired()])
#     q5 = RadioField(validators=[InputRequired()])
#     q6 = RadioField(validators=[InputRequired()])
#     q7 = RadioField(validators=[InputRequired()])
#     q8 = RadioField(validators=[InputRequired()])
#     q9 = RadioField(validators=[InputRequired()])
#     q10 = RadioField(validators=[InputRequired()])


# form = QuizForm(request.form)
# for i in range(0, 10):
#     form.i.choices = [
#         ("1", questions[i].A),
#         ("2", questions[i].B),
#         ("3", questions[i].C),
#         ("4", questions[i].D)
#     ]
