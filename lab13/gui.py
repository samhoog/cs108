""" Lab 13.1

This module implements a quiz application with different sorts of questions.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: Sam Hoogewind (sth6)
@date: Fall 2020
"""

from tkinter import Tk, Text, StringVar, Entry, Label, Button, Frame, \
    LEFT, RIGHT, WORD, END
from quiz import Quiz


class App:
    """This class builds the quiz application GUI."""

    def __init__(self, window):
        """Instantiates the GUI widgets"""

        # Build the quiz to be given.
        self.quiz = Quiz()

        # Keep track of the user's performance.
        self.correct_count = 0
        self.question_count = 0

        # Build the question output box and set the first question.
        self.question_text = Text(window, font="arial 16",
                                  width=75, height=4, wrap=WORD)
        self.question_text.insert(1.0, self.quiz.get_current_question())
        self.question_text.pack()

        # Build the answer input box.
        self.answer = StringVar()
        self.answerEntry = Entry(window,  font="arial 16",
                                 textvariable=self.answer)
        self.answerEntry.pack(side=LEFT)
        self.answerEntry.focus_set()
        self.answerEntry.bind("<Return>", self.check_answer)

        # Build the feedback/prompt panel and set the first prompt.
        self.instructions = StringVar()
        self.instructions.set('\u21D0 Enter your answer here')
        instructions_label = Label(window, font="arial 16",
                                   textvariable=self.instructions)
        instructions_label.pack(side=LEFT)

    def check_answer(self, event):
        """Checks the user's answer, gives appropriate feedback, and then
        decides whether to go on with the quiz or print the final score.
        """
        
        # Check the given answer.
        if self.quiz.check_current_answer(self.answer.get()):
            self.instructions.set("Good job!  Next question...")
            self.correct_count += 1
        else:
            self.instructions.set("Sorry, the answer was "
                                  + self.quiz.get_current_answer()
                                  + '.')
        self.question_count += 1
        self.answer.set('')
        
        # Go to the next question if it exists, otherwise print the score.
        self.question_text.delete(1.0, END)
        if self.quiz.has_next():
            self.quiz.next()
            self.question_text.insert(1.0, self.quiz.get_current_question())
        else:  
            self.question_text.insert(
                1.0,
                'Quiz Complete\n' +
                'You got {0} correct out of {1}'.format(self.correct_count,
                                                        self.question_count)
                + '.'
            )
            self.answerEntry.configure(state='disabled')


if __name__ == '__main__':
    root = Tk()
    root.title('World Forum Quiz')
    App(root)
    root.mainloop()
