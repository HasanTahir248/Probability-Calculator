import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    
    self.contents = []
    
    for color, count in kwargs.items():
      self.contents.extend([color] * count)

  def draw(self, num_of_balls):
    
    drawn_balls = []
    
    if num_of_balls >= len(self.contents):
      return self.contents
      
    for _ in range (num_of_balls):
      random_index = random.randint(0, len(self.contents) - 1)
      drawn_balls.append(self.contents.pop(random_index))
      
    return drawn_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  successful_exp = 0
  
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    
    match = True
    
    for color, count in expected_balls.items():
      
      if drawn_balls.count(color) < count:
        match = False
        break
        
    if match:
        successful_exp += 1

  probability = successful_exp / num_experiments
  return probability
    

