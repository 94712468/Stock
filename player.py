class Player:
  def __init__(self):
    self.cash = 2000
    self.share = 0

  def calculate_networth(self, current_value):
    return self.cash + self.share*current_value
  
  
  def buy(self, current_value):
    if self.cash >= current_value:
      self.share = self.share + 1
      self.cash = self.cash - current_value

  
  def sell(self, current_value):
    if self.share >=1:
      self.share = self.share - 1
      self.cash = self.cash + current_value

    
  
