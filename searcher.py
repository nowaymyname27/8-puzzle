#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """
        Constructs a new Searcher object by initializing the attributes.
        """
        self.states = []  # List of untested states
        self.num_tested = 0  # Number of states tested
        self.depth_limit = depth_limit  # Depth limit for search tree
        
    def add_state(self, new_state):
        """
        Adds a new State object to the Searcher's list of untested states.
        """
        self.states += [new_state]  # Add the new state to the list of untested states
    
    def should_add(self, state):
        """
        Determines if a given state should be added to the Searcher's list of untested states.
        """
        # Check if the searcher has a depth limit and if the state is beyond the depth limit
        if self.depth_limit != -1:
            if state.num_moves > self.depth_limit:
                return False

        # Check if the state creates a cycle
        if state.creates_cycle():
            return False

        # If none of the conditions above are met, return True
        return True
    
    def add_states(self, new_states):
        """
        Adds new_states to the list of untested states if they meet the conditions
        specified by the should_add method.
        """
        # Go through each state in the new_states list
        for s in new_states:
            # Check if the state should be added
            if self.should_add(s):
                # Add the state to the list of untested states
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    
    
    def find_solution(self, init_state):
        """
        Searches for a solution starting from the initial state.
        """
        self.add_state(init_state)
    
        while self.states:
            s = self.next_state()
            self.num_tested += 1
    
            if s.is_goal():
                return s
            else:
                successors = s.generate_successors()
                self.add_states(successors)
    
        return None  # failure



    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """
    A class for searcher objects that perform breadth-first search (BFS).
    This class inherits from the Searcher class.
    """
    
    def next_state(self):
        """
        Choose the next state to test from the list of untested states following
        FIFO (first-in first-out) ordering, which leads to breadth-first search.
        This method overrides the next_state method from the Searcher class.
        """
        chosen_state = self.states[0]  # Get the first state in the list
        self.states = self.states[1:]  # Remove the first state from the list
        return chosen_state

class DFSearcher(Searcher):
    """
    A class for searcher objects that perform depth-first search (DFS).
    This class inherits from the Searcher class.
    """

    def next_state(self):
        """
        Choose the next state to test from the list of untested states following
        LIFO (last-in first-out) ordering, which leads to depth-first search.
        This method overrides the next_state method from the Searcher class.
        """
        chosen_state = self.states[-1]  # Get the last state in the list
        self.states = self.states[:-1]  # Remove the last state from the list
        return chosen_state


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ A heuristic function that computes and returns the number of misplaced tiles
    in the Board object associated with the given state.
    """
    return state.board.num_misplaced()

def h2(state):
    '''This function calculates the number of tile swaps needed to reach the goal state.
    '''
    return state.board.manhattan_distance()



class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    

    def __init__(self, heuristic):
        """
        Constructs a new GreedySearcher object.
        """
        super().__init__(-1)  # Call the constructor of the superclass (Searcher) with a depth limit of -1
        self.heuristic = heuristic  # Initialize the heuristic attribute with the provided heuristic function

    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """
        Adds a [priority, state] pair to the list of untested states, where priority
        is determined by calling the priority method.
        """
        priority = self.priority(state)
        self.states += [[priority, state]]
        
    def next_state(self):
        """
        Choose the next state to test from the list of untested states by selecting
        the state with the highest priority.
        This method overrides the next_state method from the Searcher class.
        """
        # Find the state-priority pair with the highest priority using max function
        chosen_state_priority_pair = max(self.states)

        # Get the state with the highest priority
        chosen_state = chosen_state_priority_pair[1]

        # Remove the state from the list
        self.states.remove(chosen_state_priority_pair)

        return chosen_state

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """
    A class for searcher objects that perform A* search. This class inherits
    from the GreedySearcher class.
    """

    def priority(self, state):
        """
        Computes the priority of a given state using the searcher's heuristic
        function and the number of moves made to reach the state.
        """
        heuristic_value = self.heuristic(state)
        num_moves = state.num_moves
        return -1 * (heuristic_value + num_moves)

