from enum import Enum


class Key_State:

    states = Enum("States", "PRESSED RELEASED")

    def __init__(self, state, time_created):
        self._state = state
        self._last_modified = time_created

    def get_state(self):
        return self._state

    def get_last_modified(self):
        return self._last_modified

    def update_state(self, new_state, new_time):
        if new_state != self._state:
            self._state = new_state
            self._last_modified = new_time

    def is_priority(self, other):
        if self.get_state() == Key_State.states.PRESSED and other.get_state() == Key_State.states.RELEASED:
            return True
        elif self.get_state() == Key_State.states.RELEASED and other.get_state() == Key_State.states.PRESSED:
            return False
        elif self.get_state() == Key_State.states.PRESSED and other.get_state() == Key_State.states.PRESSED:
            if self.get_last_modified() > other.get_last_modified():
                return True
            elif self.get_last_modified() < other.get_last_modified():
                return False

    def __str__(self):
        return f"({self._state}, {self._last_modified})"


