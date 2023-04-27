from __future__ import (
    annotations,
)  # this import is done to allow adding type hints for the classes while being defined
from typing import Tuple, List, Union
import datetime
from math import pi


class Point:
    """Point class represents and manipulates x,y coordinates."""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Creates a new point at x, y, where by default the point is created at (0,0)."""
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def distance_from_origin(self) -> float:
        """Compute my distance from the origin."""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance_to(self, other: Point) -> float:
        """Compute my distance between two points."""
        return (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** 0.5

    def calculate_equation(self, other: Point) -> Tuple[float, float]:
        """Compute the coefficients of the straight line between two points."""
        m = (other.y - self.y) / (other.x - self.x)
        c = self.y - m * self.x
        return m, c

    def move_to(self, x: int, y: int) -> None:
        """Updates the coordinates. of a point."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Modifies the default representation of a Point Object."""
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        """Modifies the default string representation of a Point Object."""
        return f"({self.x}, {self.y})"


class Circle:
    """Circle class represents and manipulates center point and radius of a circle."""

    def __init__(self, radius: int = 0, point: Point = Point()) -> None:
        """Creates a new circle with radius r and whose center is located at point p."""
        self.radius = radius
        self.point = point

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius: int):
        self._radius = radius

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point: Point):
        self._point = point

    @property
    def area(self):
        return pi * self.radius ** 2

    def move_to(self, x: int, y: int) -> None:
        """Updates the coordinates. of the center of the circle."""
        self.point.move_to(x, y)

    def is_touching(self, other: Circle) -> bool:
        """Checks if two circles are touching."""
        return isinstance(other, Circle) and self.point.distance_to(other.point) <= (
            self.radius + other.radius
        )

    def __repr__(self) -> str:
        """Modifies the default string representation of a Circle Object."""
        return f"Circle at {self.point} with radius {self.radius}"


class SMSsStore:
    """SMSsStore class represents the inbox of a phone that includes the messages with relevant information."""

    def __init__(self) -> None:
        """Creates a new empty SMSsStore."""
        self.messages: List[Tuple[bool, str, datetime.datetime, str]] = []

    @staticmethod
    def _create_msg(
        from_number: str, time_arrived: datetime.datetime, text_of_msg: str
    ) -> Tuple[bool, str, datetime.datetime, str]:
        """Internal static method that creates a new message given its details."""
        return False, from_number, time_arrived, text_of_msg

    def add_new_arrival(
        self, from_number: str, time_arrived: datetime.datetime, text_of_msg: str
    ) -> None:
        """Makes new SMS tuple, inserts it after other messages in the store.
        When creating this message, its has_been_viewed status is set False."""
        msg = SMSsStore._create_msg(from_number, time_arrived, text_of_msg)
        self.messages.append(msg)

    def message_count(self) -> int:
        """Returns the number of sms messages in my_inbox."""
        return len(self.messages)

    def get_unread_indexes(self) -> List[int]:
        """Returns list of indexes of all not-yet-viewed SMS messages."""
        return [i for i in range(self.message_count()) if not self.messages[i][0]]

    def _view_message(self, i: int) -> Tuple[bool, str, datetime.datetime, str]:
        """Internal instance method that returns a copy of the ith message with its status
        updated to `viewed`."""
        msg = self.messages[i]
        return True, msg[1], msg[2], msg[3]

    def get_message(self, i: int) -> Union[Tuple[str, datetime.datetime, str], None]:
        """"Returns the contents of the ith message, and updates its state as `viewed`.
        If there is no message at position i, it returns None."""

        # check if the message index is a valid one
        if i < self.message_count():
            self.messages[i] = self._view_message(i)
            return self.messages[i][1:]

        return None

    def delete(self, i: int) -> None:
        """Deletes the message at index i."""

        # check if the message to be deleted does not exist
        if i >= len(self.messages):
            raise ValueError(
                f"You requested to delete the at index {i}, while there are only {len(self.messages)}"
            )

        del self.messages[i]

    def get_messages_from(self, from_number: str) -> List[str]:
        """Returns the list of messages sent from `from_number`."""
        msgs = []

        for ind in range(self.message_count()):

            # check if current message is from the correct number
            if self.messages[ind][1] == from_number:
                self.messages[ind] = self._view_message(ind)
                msgs.append(self.messages[ind][3])

        return msgs

    def clear(self) -> None:
        """Deletes all messages from inbox."""
        self.messages = []
