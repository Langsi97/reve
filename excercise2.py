import math


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"({self.__x}, {self.__y})"

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


class Circle:
    def __init__(self, radius, center_point):
        self.__radius = radius
        self.__center_point = center_point

    def __repr__(self):
        return f"Circle({self.__radius}, {self.__center_point})"

    def __str__(self):
        return (
            f"Circle with radius {self.__radius} and center point {self.__center_point}"
        )

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    @property
    def center_point(self):
        return self.__center_point

    @center_point.setter
    def center_point(self, value):
        self.__center_point = value

    @property
    def area(self):
        return math.pi * self.__radius**2

    def move_to(self, x, y):
        self.__center_point.move_to(x, y)

    def is_touching(self, other_circle):
        distance_between_centers = math.sqrt(
            (self.__center_point.x - other_circle.center_point.x) ** 2
            + (self.__center_point.y - other_circle.center_point.y) ** 2
        )
        return distance_between_centers <= self.__radius + other_circle.radius


"-----------------------------------------------"
# Create a Point object
p = Point(2, 3)

# Create a Circle object with radius 5 and center at point p
c1 = Circle(5, p)

# Create another Circle object with radius 3 and center at point (0, 0)
c2 = Circle(3, Point())

# Print the circles
print(c1)  # Circle with radius 5 and center point (2, 3)
print(c2)  # Circle with radius 3 and center point (0, 0)

# Move the first circle to a new location at point (1, 1)
c1.move_to(1, 1)

# Check if the two circles are touching
print(c1.is_touching(c2))  # False

# Change the radius of the second circle
c2.radius = 4

# Check if the two circles are touching again
print(c1.is_touching(c2))  # True

# Print the area of the first circle
print(c1.area)  # 78.53981633974483
"-----------------------------------------------"


from datetime import datetime


class SMSsStore:
    def __init__(self):
        self.messages = []

    def __repr__(self):
        return f"SMSsStore({self.messages})"

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.messages.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        return [i for i, message in enumerate(self.messages) if not message[0]]

    def get_message(self, i):
        if i < len(self.messages):
            message = self.messages[i]
            self.messages[i] = (True,) + message[1:]
            return message[1:]
        return None

    def delete(self, i):
        if i < len(self.messages):
            del self.messages[i]
        else:
            raise ValueError(
                f"You requested to delete the message at index {i},while there are only {len(self.messages)} messages"
            )

    def get_messages_from(self, number):
        messages = []
        for i, message in enumerate(self.messages):
            if message[1] == number:
                messages.append(message[3])
                self.messages[i] = (True,) + message[1:]
        return messages

    def clear(self):
        self.messages = []
