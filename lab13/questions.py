""" Lab 13.1

This module implements a model of a variety of quiz question types.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

class Question:
  
    def __init__(self, question):
        self.text = question

class FillInTheBlank(Question):
    """This class implements a Fill in the Blank question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a fill in the blank question object."""
        Question.__init__(self, question)
        self.answer = answer

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '\nFill in the blank.'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return self.answer.lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return self.answer


class TrueFalse(Question):
    """This class implements a True or False question with a string answer."""
    
    def __init__(self, question, answer):
        """Initializes a true or false question object."""
        Question.__init__(self, question)
        self.answer = answer
        if isinstance(answer, bool) == False:
            raise ValueError("Answer provided is not True or False")

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '\nIs this statement True or False?'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return str(self.answer).lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return str(self.answer)


class ShortAnswer(Question):
    """This class implements a short-answer question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a short-answer question object."""
        Question.__init__(self, question)
        self.answer = answer

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '?'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return self.answer.lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return self.answer


if __name__ == "__main__":

    q = ShortAnswer('question', 'answer')
    assert q.get_question() == 'question?'
    assert q.get_answer() == 'answer'
    assert not (q.check_answer('blob'))
    assert q.check_answer('answer')

    # Add these tests to verify that your new sub-classes operate properly.
    q = FillInTheBlank('question', 'answer')
    assert q.get_question() == 'question\nFill in the blank.'
    assert q.get_answer() == 'answer'
    assert not (q.check_answer('blob'))
    assert q.check_answer('answer')

    q = TrueFalse('question', True)
    assert q.get_question() == 'question\nIs this statement True or False?'
    assert q.get_answer() == 'True'
    assert not (q.check_answer('maybe'))
    assert q.check_answer('True')
    try:
        TrueFalse('question', 'non-boolean answer')
        assert False
    except ValueError:
        assert True