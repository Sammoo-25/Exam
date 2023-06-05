import json


class Quiz:
    def __init__(self, questions_file):
        self.questions = self.load_questions(questions_file)
        self.user_answers = {}
        self.info = {}

    def load_questions(self, file):
        with open(file) as f:
            data = json.load(f)
        return data

    def run_quiz(self):
        name = input(self.questions["student_name"])
        surname = input(self.questions["student_surname"])
        for question_num, question_data in self.questions["exam_content"].items():
            print(f"Question {question_num}: {question_data['question']}")
            print("Options:")
            print(f"a) {question_data['a']}")
            print(f"b) {question_data['b']}")
            print(f"c) {question_data['c']}")
            print(f"d) {question_data['d']}")
            user_answer = input("Answer (a, b, c, d): ")
            while user_answer not in ('a', 'b', 'c', 'd'):
                user_answer = input("Invalid input. Please choose a valid option (a, b, c, d): ")
            print(f"You selected: {user_answer}\n")

            question_key = f"{question_num}. {question_data['question']}"
            self.info['Name: '] = name
            self.info['Surname '] = surname
            self.user_answers['Info'] = self.info
            self.user_answers[question_key] = user_answer
        self.save_answers()

    def save_answers(self):
        with open('answers.json', "w") as f:
            json.dump(self.user_answers, f, indent=4)


if __name__ == '__main__':
    quiz = Quiz("d95dfce6-e656-4b22-b6c8-9ad7fbc76f1f_student.json")
    quiz.run_quiz()
