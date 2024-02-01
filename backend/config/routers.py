from rest_framework.routers import DefaultRouter


from quiz.viewsets import QuizViewSet, QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)

urlpatterns = router.urls