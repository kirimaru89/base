from module.activity.question.consts import QuestionType


class QuestionUtil:
    def check_valid_answers(question_type, answers):
        if not answers:
            return False, "Thiếu câu trả lời"
        number_of_correct_answers = 0
        for answer in answers:
            if answer["correct"]:
                number_of_correct_answers += 1
        if number_of_correct_answers == 0:
            return False, "Thiếu câu trả lời đúng"

        if question_type == QuestionType.SINGLE and number_of_correct_answers > 1:
            return False, "Câu hỏi chỉ có 1 câu trả lời đúng"
        return True, None

    def clean_and_create_answers(question, answers):
        question.answers.all().delete()
        for order, answer in enumerate(answers):
            answer["question"] = question
            answer["correct"] = answer.get("correct", False)
            answer["content"] = answer.get("content", "")
            answer["order"] = order
            question.answers.create(**answer)
