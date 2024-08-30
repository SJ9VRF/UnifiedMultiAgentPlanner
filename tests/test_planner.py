# Tests for the planner functionalities
import pytest
from src.planner import PlannerInterface
from src.agents import MultiAgentSetup

# Mock data or functions can be used to simulate the environment for tests.
def test_planner_solves_problem_correctly():
    # Setup a multi-agent problem.
    multi_agent_setup = MultiAgentSetup("test_problem")
    agent1 = multi_agent_setup.add_agent("robot_a")
    agent2 = multi_agent_setup.add_agent("scale_a")

    # Add agents, fluents, actions, etc., to your problem
    # This part depends on how you've structured your problem setup code.
    # For example:
    # multi_agent_setup.problem.add_object(home)
    # multi_agent_setup.problem.add_object(office)
    # Assume that there are some initial values and goals set up here.

    # Initialize the planner
    planner = PlannerInterface(multi_agent_setup.problem)

    # Solve the problem
    result = planner.solve(heuristic='1')  # using DTG heuristic as an example

    # Check if the result status is as expected (i.e., SOLVED_SATISFICING)
    assert result.status == "SOLVED_SATISFICING", "The planner failed to solve the problem satisfactorily."

    # Optionally, check the properties of the resulting plan
    assert len(result.plan.all_sequential_plans()) > 0, "No plans were generated."

def test_planner_handles_no_solution():
    # Setup a different problem configuration where no solution is expected
    multi_agent_setup = MultiAgentSetup("unsolvable_problem")
    agent1 = multi_agent_setup.add_agent("robot_b")
    agent2 = multi_agent_setup.add_agent("scale_b")

    # Add unsolvable configurations

    # Initialize the planner
    planner = PlannerInterface(multi_agent_setup.problem)

    # Attempt to solve the problem
    result = planner.solve(heuristic='1')

    # Check if the result status is correctly identified as UNSOLVABLE
    assert result.status == "UNSOLVABLE", "The planner incorrectly found a solution."

# More tests can be added to check different functionalities and edge cases of the planner.
