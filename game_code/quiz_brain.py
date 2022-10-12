import html

class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
        self.num_qs = len(questions)

    def still_has_questions(self):
        #print(self.question_number < self.num_qs)
        return self.question_number < self.num_qs

    def next_question(self):
        self.current_q = self.question_list[self.question_number]
        self.question_number += 1
        self.cur_q = html.unescape(self.current_q.text)
        return f"Q{self.question_number}: {self.cur_q} (True/False): "


    def check_answer(self, choice):
        if(choice == self.current_q.answer):
            self.score += 1
            return "Correct!"
        else:
            return "Incorrect!"
            #debug self.question_number = self.num_qs

    def print_score(self):
        print(f"Your score is: {self.score}/{self.question_number}.\n")