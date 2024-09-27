import json
with open('question.txt', 'r', encoding='utf-8') as file:
    a = file.read()
list_qwest = json.loads(a)
score = 0
list_ = []
a = 10
class Question():
    def __init__(self, text, deef, answer):
        self.text = text
        self.deef = deef
        self.answer = answer
        self.flag = False
        self.answ_player = None
        self.point = self.get_points()

    def is_correct(self):

        if self.answ_player == self.answer:
            return True

        else:
            return False


    def get_points(self):
        return self.deef*10

    def build_question(self):
        return f"Вопрос: {self.text}\nСложность {self.deef}/5"

    def build_positive_feedback(self):
        return f"Ответ верный, получено {self.deef} балов"

    def build_negative_feedback(self):
        return f"Ответ неверный, верный ответ {self.answer}"

    def __repr__(self):
        return f'{self.text}'

def create_qwest():
    for qweest in list_qwest:
        list_.append(Question(qweest['q'],qweest['d'], qweest['a']))

def get_report():
    global end_score, score
    create_qwest()
    for quest in list_:
        # report += f'{quest.build_question()}\n'
        print(quest.build_question())
        quest.answ_player = input('Ответ: ')
        if quest.is_correct():
            print(quest.build_positive_feedback())
            score+=quest.point
        else:
            print(quest.build_negative_feedback())

get_report()
print(f'SCORE:{score}')