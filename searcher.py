#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Sayed AlGharbi
# email: AlGharbi@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Sadiq Alhumood
# partner's email: sadiq@bu.edu
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
        """constructs a new Searcher object"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """takes a single State object called new_state and adds it
        to the Searcher‘s list of untested states"""
        self.states += [new_state]
        
    def should_add(self, state):
        """ takes a State object called state and returns True if the called
        Searcher should add state to its list of untested states, and False 
        otherwise. """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle():
            return False
        
        return True
    
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time """
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s           
                
    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified
        initial state init_state and ends when the goal state is found or when
        the Searcher runs out of untested states."""
        self.add_state(init_state)
        while self.states != []:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() is True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None


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
    """ A class called for searcher objects that perform breadth-first
    search (BFS) instead of random search"""
    
    def next_state(self):
        """returns the state that has been in the list the longest"""
        lc = [[x.num_moves, x] for x in self.states] 
        x = min(lc)
        self.states.remove(x[1])
        return x[1]
        
class DFSearcher(Searcher):
    """"returns the state that has been in the list the shortest"""
    def next_state(self):
        lc = [[x.num_moves, x] for x in self.states] 
        x = max(lc)
        self.states.remove(x[1])
        return x[1]

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    """returns an estimate of how many additional moves are needed to
    get from state to the goal state"""
    return state.board.num_misplaced()

def h2(state):
    return state.board.num_misplaced_1()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    
    def __init__(self, heuristic):
        """ constructs a new GreedySearcher object"""
        super().__init__(-1)
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """adds a sublist that is a [priority, state] pair, where priority
        is the priority of state that is determined by calling the priority 
        method"""
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """chooses one of the states with the highest priority."""
        x = max(self.states)
        self.states.remove(x)
        return x[1]

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
    """ A class for objects that perform an informed greedy AStar
        search on an Eight Puzzle.
    """
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
    
    
    

    
    


