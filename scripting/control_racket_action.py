from tkinter import LEFT, RIGHT
from constants import *
from game.scripting.action import Action

class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, collection, script, callback):
        racket = collection.get_first_entity(RACKET_GROUP)
        if self._keyboard_service.is_key_down(LEFT):
            racket.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT):
            racket.swing_right()
        else:
            racket.stop_moving()
    