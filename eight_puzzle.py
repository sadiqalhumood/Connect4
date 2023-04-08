#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Sayed AlGharbi
# email: AlGharbi@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Sadiq Alhumood
# partner's email: sadiq@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):
    total_m = 0
    states_t = 0
    puzzles_solved = 0
    file = open(filename, 'r')
    for line in file:
        line = line[:-1]
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return
        
        soln = None 
        try:
            soln = searcher.find_solution(init_state)
            if soln == None:
                print(line + ': no solution')
            elif soln != None:
                print(line + ': ' + str(soln.num_moves) + ' moves, ' + str(searcher.num_tested) + ' states tested')
                puzzles_solved += 1
                total_m += soln.num_moves
                states_t += searcher.num_tested
        except KeyboardInterrupt:
            print(line + ': search terminated, no solution', end='\n')  
    file.close()
    if puzzles_solved == 0:
        print('\nsolved ' + str(puzzles_solved) + ' puzzles')
    else:
        print('\nsolved ' + str(puzzles_solved) + ' puzzles')
        print('averages: ' + str(total_m/puzzles_solved) +" moves, " + str(states_t/puzzles_solved) + ' states tested')
        
    
        
    
   
   

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    