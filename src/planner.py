# Planning and solving functionalities
from unified_planning.engines import OneshotPlanner

class PlannerInterface:
    def __init__(self, problem):
        self.problem = problem

    def solve(self, heuristic):
        with OneshotPlanner(name='fmap', params={'heuristic': heuristic}) as planner:
            result = planner.solve(self.problem)
            return result
