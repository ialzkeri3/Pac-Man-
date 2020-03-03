# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import searchAgents


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):

    # problem = (searchAgents.PositionSearchProblem) problem
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack


    visitedNodes = []  
    stack = Stack() 
    stack.push((problem.getStartState(), []))

    while (not stack.isEmpty()):
        head = stack.pop()
        actions = head[1]
        state = head[0]
        if (state in visitedNodes):
            continue
        if (state not in visitedNodes):    
            if problem.isGoalState(state):
                return actions
            visitedNodes.append(state)
            for child in problem.getSuccessors(state):
                tempActions = actions[:]
                tempActions.append(child[1])
                stack.push((child[0], tempActions))
    return None


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    visitedNodes = []
    queue = util.Queue()
    queue.push((problem.getStartState(), []))

    while (not queue.isEmpty()):
        head = queue.pop()
        actions = head[1]
        state = head[0]

        if (state not in visitedNodes):

            if problem.isGoalState(state):
                return actions

            visitedNodes.append(state)

            for child in problem.getSuccessors(state):
                tempActions = actions[:]
                tempActions.append(child[1])
                queue.push((child[0], tempActions))

    return None


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    # problem = (searchAgents.PositionSearchProblem) problem

    visited = []
    PQueue = util.PriorityQueue()
    PQueue.push((problem.getStartState(), []), 0)

    while (not PQueue.isEmpty()):
        head = PQueue.pop()
        actions = head[1]
        state = head[0]
        cost = problem.getCostOfActions(actions)

        if (state not in visited):

            if problem.isGoalState(state):
                return actions

            visited.append(state)

            for node in problem.getSuccessors(state):
                tempActions = actions[:]
                tempActions.append(node[1])
                tempCost = problem.getCostOfActions(tempActions)
                PQueue.push((node[0], tempActions), tempCost)

    return None


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):

    visited = []
    PQueue = util.PriorityQueue()
    PQueue.push((problem.getStartState(), []),
                heuristic(problem.getStartState(), problem))

    while (not PQueue.isEmpty()):
        head = PQueue.pop()
        actions = head[1]
        state = head[0]

        if (state not in visited):

            if problem.isGoalState(state):
                return actions

            visited.append(state)

            for node in problem.getSuccessors(state):
                tempActions = actions[:]
                tempActions.append(node[1])
                tempCost = problem.getCostOfActions(
                    tempActions)+heuristic(node[0], problem)
                PQueue.push((node[0], tempActions), tempCost)

    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
