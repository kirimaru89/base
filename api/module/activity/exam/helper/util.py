from module.activity.exam_question.models import ExamQuestion
from module.activity.exam_answer.models import ExamAnswer
from module.activity.exam_result.models import ExamResult


class ExamUtil:
    @staticmethod
    def clone_exam_questions(exam):
        contest = exam.contest
        questions = contest.questions.all()
        for question in questions:
            exam_question = ExamQuestion.objects.create(
                exam=exam,
                type=question.type,
                content=question.content,
            )
            answers = question.answers.all()
            for answer in answers:
                ExamAnswer.objects.create(
                    exam_question=exam_question,
                    content=answer.content,
                    correct=answer.correct,
                )

    @staticmethod
    def calculate_exam_item_result(exam_question_id, exam_answer_ids):
        correct_answers = set(
            ExamAnswer.objects.filter(
                exam_question_id=exam_question_id, correct=True
            ).values_list("id", flat=True)
        )
        return set(exam_answer_ids) == correct_answers

    @staticmethod
    def calculate_exam_score(exam):
        return ExamResult.objects.filter(exam_question__exam=exam, correct=True).count()
