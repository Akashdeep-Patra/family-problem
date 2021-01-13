import sys
import utils

if __name__=="__main__":
    q=utils.get_initial_tree()
    with open(sys.argv[1], 'r') as file:
        for line in file:
            utils.formatted_output(utils.factory(queen=q,command_line_args=line.split()))
    