import json
with open('question.txt', 'r') as file:
    a = file.read()
list_qwest = json.loads(a)
score = 0
list_ = []

class Question():
    def __init__(self, text, deef, answer):
        self.text = text
        self.deef = deef
        self.answer = answer
        self.flag = False
        self.answ_player = None
        self.point = self.get_points()

    def is_correct (self):
        self.answ_player = input('Ответ: ')
        if self.answ_player == self.answer:
            self.flag = True
            self.build_positive_feedback()
        else:
            self.flag = False
            self.build_negative_feedback()
    def get_points(self):
        return 10*self.deef

    def build_question(self):
        return f"Вопрос: {self.text}\nСложность {self.deef}/5"

    def build_positive_feedback(self):
        return f"Ответ верный, получено {self.deef} балов"

    def build_negative_feedback(self):
        return f"Ответ неверный, верный ответ {self.answer}"

def create_qwest():
    for qweest in list_qwest:
        list_.append(Question(qweest['q'],qweest['d'], qweest['a']))

create_qwest()
print(list_[0].build_question())
print(list_[0].is_correct())
