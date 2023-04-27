from typing import Tuple, List, Union
from datetime import datetime


class Message:
    """Message class that represents message objects."""

    def __init__(
        self,
        from_number: str,
        time_arrived: datetime = datetime.now(),
        text_of_msg: str = "",
    ) -> None:
        """Creates a new Message that has not yet viewed."""
        self.has_been_viewed = False
        self._from_number = from_number
        self._time_arrived = time_arrived
        self._text_of_message = text_of_msg

    @property
    def from_number(self):
        return self._from_number

    @property
    def time_arrived(self):
        return self._time_arrived

    @property
    def text_of_msg(self):
        return self._text_of_msg

    def view_message(self) -> None:
        """Updates the status of the message to `viewed`."""
        self.has_been_viewed = True

    def is_unread(self) -> bool:
        """Checks if the message has not yet been viewed."""
        return not self.has_been_viewed

    def get_information_tuple(self) -> Tuple[str, datetime, str]:
        """Create a tuple of the information of the message with all attributes except the viewing status."""
        return self.from_number, self.time_arrived, self.text_of_msg


class SMSsStore:
    """SMSsStore class represents the inbox of a phone that includes the messages with relevant information."""

    def __init__(self) -> None:
        """Creates a new empty SMSsStore."""
        self.messages: List[Message] = []

    def add_new_arrival(
        self, from_number: str, time_arrived: datetime, text_of_msg: str
    ) -> None:
        """Makes new SMS tuple, inserts it after other messages in the store.
        When creating this message, its has_been_viewed status is set False."""
        self.messages.append(Message(from_number, time_arrived, text_of_msg))

    def message_count(self) -> int:
        """Returns the number of sms messages in my_inbox."""
        return len(self.messages)

    def get_unread_indexes(self) -> List[int]:
        """Returns list of indexes of all not-yet-viewed SMS messages."""
        return [i for i in range(self.message_count()) if self.messages[i].is_unread()]

    def get_message(self, i: int) -> Union[Tuple[str, datetime, str], None]:
        """"Returns the contents of the ith message, and updates its state as `viewed`.
        If there is no message at position i, it returns None."""

        # check if the message index is a valid one
        if i < self.message_count():
            self.messages[i].view_message()
            return self.messages[i].get_information_tuple()

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
            if self.messages[ind].from_number() == from_number:
                self.messages[ind].view_message()
                msgs.append(self.messages[ind].text_of_msg())

        return msgs

    def clear(self) -> None:
        """Deletes all messages from inbox."""
        self.messages = []
