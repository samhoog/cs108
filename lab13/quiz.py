""" Lab 13.1

This module implements and instantiates a quiz of heterogeneous questions.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@date: Spring, 2020 - restored original questions
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""
import random
from questions import ShortAnswer, TrueFalse, FillInTheBlank


class Quiz:
    """This class builds a quiz model with hard-coded, sample questions."""

    def __init__(self):
        """Initializes the quiz object with sample questions in random order"""

        self.questions = [
            ShortAnswer(
                'Who won the English football cup in 1949',
                'Wolverhampton'),
            ShortAnswer(
                'The Hammers is the nickname of what English football team',
                'West Ham United'),
            ShortAnswer(
                'What’s Jerry Lee Lewis’s biggest hit',
                'Great Balls of Fire'),
            TrueFalse(
                'The development of the industrial proletariat is conditioned by the development of the industrial bourgeoisie.',
                True),
            FillInTheBlank(
                'The struggle of class against class is a _______ struggle.',
                'political')
        ]
        random.shuffle(self.questions)
        
        self.problemNum = 0
        
    def get_current_question(self):
        """Returns the text of the current question"""
        return self.questions[self.problemNum].get_question()
    
    def get_current_answer(self):
        """Returns the answer of the current question"""
        return self.questions[self.problemNum].get_answer()
    
    def check_current_answer(self, answer):
        """Returns a boolean indicating the correctness of the given answer"""
        return self.questions[self.problemNum].check_answer(answer)
    
    def has_next(self):
        """Returns a boolean indicating whether there are more questions"""
        return self.problemNum < len(self.questions) - 1
    
    def next(self):
        """Goes on to the next question"""
        if self.problemNum == len(self.questions) - 1:
            raise StopIteration("There are no more problems")
        self.problemNum += 1


if __name__ == '__main__':

    quiz = Quiz()

    # The questions should have correct answers.
    i = 0
    while quiz.has_next():
        assert quiz.check_current_answer(quiz.get_current_answer())
        quiz.next()

    # There should be no more questions and going through them all.
    try:
        quiz.next()
        assert False
    except StopIteration:
        assert True
