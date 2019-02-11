import json
from flask import Flask, request, Response
from flask import render_template, flash, redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

import sys
sys.path.append('/home/evaclickwithoutfsm/classes')

import hrqclasses
import dbclasses

###############
@app.route('/')
@app.route('/index')
def index():
    sql = dbclasses.SQLighter()

    sql.create_table('answer_01')

    full_name = '/home/evaclickwithoutfsm/data/hrq.json'
    hrq = hrqclasses.HrqDataFromFile(json, full_name)
    hrq_data = hrq.getAll()

    return render_template('index.html', title='Home', hrq_data=hrq_data)


##############
@app.route('/question', methods=['GET', 'POST'])
def question():
    full_name = '/home/evaclickwithoutfsm/data/hrq.json'
    hrq = hrqclasses.HrqDataFromFile(json, full_name)
    hrq_data = hrq.getAll()
    question_code = request.args.get('question_code')
    if 'current_question_code' in request.form :
        question_code = request.form['current_question_code']
        if 'answer_code' not in request.form :
            next_question_code = question_code
            return render_template('question.html', title='Question', hrq_data = hrq_data, question_code = next_question_code, error = 'no answer selected')
        if 'answer_code' in request.form :
            answer_code = request.form['answer_code']
            sql = dbclasses.SQLighter()
            query = "INSERT INTO `answer_01` (`ANSW_QUESTION_CODE`, `ANSW_ANSWER_CODE`) VALUES ('" + question_code + "', '" + answer_code + "')"
            sql.insert(query)

    next_question_code = hrq.getNextQuestionCode(question_code)

    if next_question_code == 'Q_LAST_ONE':

        return redirect("/show_result")

    return render_template('question.html', title='Question', hrq_data = hrq_data, question_code = next_question_code, error = '')

###############
@app.route('/show_result')
def showResult():
    full_name = '/home/evaclickwithoutfsm/data/hrq.json'
    hrq = hrqclasses.HrqDataFromFile(json, full_name)
    hrq_data = hrq.getAll()

    sql = dbclasses.SQLighter()

    question_all = 0
    question_with_correct_answer = 0
    for question_code in hrq_data:
        if question_code != 'Q_00':
            question_all += 1
            row = sql.getByQuestionCode(question_code)
            answer_code = row[2]
            if hrq_data[question_code]['answers'][answer_code]['is_right'] == 'true':
                question_with_correct_answer += 1

    percentage_of_correct_answers = (question_with_correct_answer/question_all)*100

    return render_template('show_result.html', title='Show Result', percentage_of_correct_answers = percentage_of_correct_answers)

###############
@app.route('/test_sql')
def testSql():

    sql = SQLighter();




    return render_template('test_sql.html', title='Test SQL')

##############
if __name__ == "__main__":
    app.run(host='https://evaclickwithoutfsm.pythonanywhere.com/', port=8080, debug=True)



