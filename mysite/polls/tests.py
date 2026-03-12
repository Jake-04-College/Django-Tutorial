import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_choice(choiceText, Question):
    return Choice.objects.create(question=Question, choice_text=choiceText)


class QuestionTestCase(TestCase):

    def setUp(self):
        question = create_question("What is your Favourite Colour?", -1)
        create_choice("Red", question)
        create_choice("Blue", question)
        #create_choice("Green", question)

    def test_IsQuestionPublished(self):
        Q = Question.objects.last()
        print(Q)
        self.assertEqual(Q.question_text, "What is your Favourite Colour?")

    def test_AreChoicesCorrect(self):
        question = Question.objects.last()
        choices = Choice.objects.filter(question=question)
        choice_texts = [c.choice_text for c in choices]
        self.assertIn("Red", choice_texts)
        self.assertIn("Blue", choice_texts)
        self.assertNotIn("Green", choice_texts)


class Database