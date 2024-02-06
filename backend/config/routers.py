from rest_framework.routers import DefaultRouter

from quizzes.viewsets import QuizViewSet, QuestionViewSet, AnswerViewSet
from users.viewsets import CustomUserViewSets

router = DefaultRouter()

router.register(r"quizzes", QuizViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"answers", AnswerViewSet)
router.register(r"users", CustomUserViewSets)

urlpatterns = router.urls
