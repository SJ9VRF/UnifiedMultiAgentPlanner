# Defines Agent and MultiAgentProblem classes
from unified_planning.model import Agent, MultiAgentProblem

class MultiAgentSetup:
    def __init__(self, name):
        self.problem = MultiAgentProblem(name)

    def add_agent(self, agent_name):
        agent = Agent(agent_name, self.problem)
        self.problem.add_agent(agent)
        return agent
