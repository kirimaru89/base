from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from service.request_service import RequestService


from service.framework.drf_class.custom_permission import CustomPermission
from service.date_service import DateService
from module.activity.exam.models import Exam
from module.activity.exam_result.models import ExamResult
from module.activity.exam.helper.util import ExamUtil
from module.activity.contest.helper.sr import ContestSr
from ..helper.sr import ExamSr


class SubmitView(GenericViewSet):
    _name = "exam"
    serializer_class = ExamSr
    permission_classes = (CustomPermission,)

    @transaction.atomic
    @action(methods=["put"], detail=True)
    def submit(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        if exam.submitted_at:
            return RequestService.res({"detail": "Bài thi này đã được nộp"})
        contest = exam.contest
        results = request.data
        for result in results:
            question = result.get("question")
            answers = result.get("answers")
            ExamResult.objects.create(
                exam_question_id=question,
                exam_answer_ids=answers,
                correct=ExamUtil.calculate_exam_item_result(question, answers),
            )
        exam.score = ExamUtil.calculate_exam_score(exam)
        exam.submitted_at = DateService.now()
        exam.save()
        result = {
            "id": pk,
            "contest": ContestSr(contest).data,
            "exam": ExamSr(exam, context=dict(show_correct_answers=True)).data,
            "result": {
                "started_at": exam.started_at,
                "submitted_at": exam.submitted_at,
                "number_of_questions": exam.exam_questions.count(),
                "number_of_correct_answers": exam.score,
            },
        }
        member = exam.member
        Exam.objects.filter(member=member, contest=contest).exclude(pk=pk).delete()
        return RequestService.res(result)

    @action(methods=["get"], detail=True)
    def retrieve(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        contest = exam.contest
        result = {
            "id": pk,
            "contest": ContestSr(contest).data,
            "exam": ExamSr(exam, context=dict(show_correct_answers=True)).data,
            "result": {
                "started_at": exam.started_at,
                "submitted_at": exam.submitted_at,
                "number_of_questions": exam.exam_questions.count(),
                "number_of_correct_answers": exam.score,
            },
        }
        return RequestService.res(result)
