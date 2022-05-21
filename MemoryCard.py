#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QFormLayout, QGroupBox, QButtonGroup
import sys
from random import shuffle
#создание элементов интерфейса

app = QApplication(sys.argv)
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.setGeometry(400, 200, 400, 200)
main_win.cur_question = -1
main_win.all_right = 0
finish = ''
#class
class Question():
    def __init__(
        self, question, right, wrong1, wrong2, wrong3
    ):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#question
question = QLabel(main_win)
answer = QPushButton(main_win)
answer.setText('Ответить')
#results
group_box_k = QGroupBox('Результат теста')
true = QLabel(main_win)
vv_line = QVBoxLayout(main_win)
vv_line.addWidget(true)
group_box_k.setLayout(vv_line)
group_box_k.hide()
#GroupBox
group_box = QGroupBox('Варианты ответов')
#answers
radio_group = QButtonGroup()

btn_answer_1 = QRadioButton(main_win)
btn_answer_2 = QRadioButton(main_win)
btn_answer_3 = QRadioButton(main_win)
btn_answer_4 = QRadioButton(main_win)

radio_group.addButton(btn_answer_1)
radio_group.addButton(btn_answer_2)
radio_group.addButton(btn_answer_3)
radio_group.addButton(btn_answer_4)
#привязка элементов к вертикальной линии
v_line = QVBoxLayout(main_win)
v2_line = QVBoxLayout(main_win)
h_line = QHBoxLayout(main_win)
hh_line = QHBoxLayout(main_win)
hhh_line = QHBoxLayout(main_win)

v2_line.addWidget(question, alignment = Qt.AlignCenter)
h_line.addWidget(btn_answer_1, alignment = Qt.AlignVCenter)
h_line.addWidget(btn_answer_2, alignment = Qt.AlignVCenter)
hh_line.addWidget(btn_answer_3, alignment = Qt.AlignVCenter)
hh_line.addWidget(btn_answer_4, alignment = Qt.AlignVCenter)

v_line.addLayout(h_line)
v_line.addLayout(hh_line)
v_line.addLayout(hhh_line)
#group_box
group_box.setLayout(v_line)
v2_line.addWidget(group_box)
v2_line.addWidget(group_box_k)

v2_line.addWidget(answer, alignment = Qt.AlignCenter)

main_win.setLayout(v2_line)
# обработка событий
q1 = Question('question-1', '+', '-', '-', '-')
q2 = Question('question-2', '+', '-', '-', '-')
q3 = Question('question-3', '+', '-', '-', '-')
q4 = Question('question-4', '+', '-', '-', '-')
q5 = Question('question-5', '+', '-', '-', '-')
q6 = Question('question-6', '+', '-', '-', '-')

answers = [
    btn_answer_1, btn_answer_2, btn_answer_3, btn_answer_4
]

all_questions = [
    q1, q2, q3, q4, q5, q6
]

def next_question(answers, all_questions):
    shuffle(answers)

    main_win.cur_question += 1
    if main_win.cur_question != 6:
        answers[0].setText(all_questions[main_win.cur_question].right)
        answers[1].setText(all_questions[main_win.cur_question].wrong1)
        answers[2].setText(all_questions[main_win.cur_question].wrong2)
        answers[3].setText(all_questions[main_win.cur_question].wrong3)
        question.setText(all_questions[main_win.cur_question].question)

def check_answer(answers):
    if answers[0].isChecked():      
        main_win.all_right += 1          
        true.setText('Правильно!')
    else:
        true.setText('Неравильно!')
def show_result():
    check_answer(answers)

    radio_group.setExclusive(False)
    btn_answer_1.setChecked(False)
    btn_answer_2.setChecked(False)
    btn_answer_3.setChecked(False)
    btn_answer_4.setChecked(False)
    radio_group.setExclusive(True)

    group_box.hide()
    group_box_k.show()
    if main_win.cur_question == 5:
        answer.setText('Завершить')
    else:
        answer.setText('Следующий вопрос')
def show_question():
    group_box_k.hide()
    group_box.show()
    answer.setText('Ответить')
def start_test():
    if 'Ответить' == answer.text():
        show_result()

    elif 'Следующий вопрос' == answer.text():
        show_question()
        next_question(answers, all_questions)

    elif 'Завершить' == answer.text():
        finish = ('Правильно: ' + str(main_win.all_right) + ' / Неправильно: ' + str(6 - main_win.all_right))
        true.setText(finish)
        question.setText('Поздравляем! Вы прошли тест.')
        answer.setText('OK')
    elif 'OK' == answer.text():
        app.quit()









#test
next_question(answers, all_questions)
answer.clicked.connect(start_test)

#запуск приложения
main_win.show()
sys.exit(app.exec_())