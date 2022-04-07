import copy
import random

class Hat:
    # takes arguments that specify the number of balls of each color that are in the hat
    def __init__(self, **color_number):
        self.contents = []
        for k, v in color_number.items():     # makes a list of strings of every ball by its color name
            i = v
            while i > 0:
                self.contents.append(k)
                i -= 1

    # remove balls at random from contents and return them as a list of strings
    def draw(self, num_balls):  
        if len(self.contents) < num_balls:
            return self.contents
        balls_drawn = []
        for ball in range(num_balls):
            rand_idx = random.randint(0, len(self.contents)-1)
            new_ball = self.contents[rand_idx]
            balls_drawn.append(new_ball)
            self.contents.remove(new_ball)
        return balls_drawn

# return a probability; draw balls and compare to expected a set number of times
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # convert dictionary input to list to compare with drawn list
    print('Experiment has Begun')
    expected_list = []
    for k, v in expected_balls.items():
        i = v
        while i > 0:
           expected_list.append(k)
           i -=1

    matches = 0
    cycles = 0

    # main loop -- draws, checks if the expected list matches, and keeps count
    for z in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn = new_hat.draw(num_balls_drawn)
        expected_copy = copy.copy(expected_list)

        # compare expected list with drawn list
        for drawn_item in drawn:
            if drawn_item in expected_copy:
                expected_copy.remove(drawn_item)

        if len(expected_copy) < 1:
            matches += 1
            cycles += 1
        else:
            cycles += 1

    probability = matches / num_experiments
    print('cycles', cycles)
    print('num_experiments', num_experiments)
    print('matches', matches)
    return probability
          
      

      
    
