# Set up the environment, user types, and objects
from unified_planning.model import UserType, Object

class EnvironmentSetup:
    def __init__(self, problem):
        self.problem = problem

    def add_user_type(self, name):
        return UserType(name)

    def add_object(self, name, user_type):
        obj = Object(name, user_type)
        self.problem.add_object(obj)
        return obj
