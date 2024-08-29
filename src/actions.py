# Defines actions and their effects
from unified_planning.model import Fluent, InstantaneousAction, UserType, Object

class ActionSetup:
    def __init__(self, problem):
        self.problem = problem

    def create_fluent(self, name, user_type=None):
        fluent = Fluent(name, user_type=user_type)
        return fluent

    def create_action(self, name, preconditions, effects):
        action = InstantaneousAction(name)
        for precondition in preconditions:
            action.add_precondition(precondition)
        for effect, status in effects.items():
            action.add_effect(effect, status)
        return action
