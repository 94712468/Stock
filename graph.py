# import matplotlib.pyplot as plt
# y = [10000, 15000, 20000, 25000]
# plt.plot(y)
# plt.show()

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np



plt.ion()

class GraphWidget:

  def __init__(self, root):
    # per month
    self.price_history = [1000 for _ in range(12)]

    self.fig = Figure(figsize=(4, 3), dpi=100)
    self.graph = self.fig.add_subplot(111)
    self.line, = self.graph.plot(self.price_history)
    self.graph.set_ylim([700, 1300])

    self.canvas = FigureCanvasTkAgg(self.fig, master=root)
    self.canvas.draw()
    self.canvas.get_tk_widget().grid(row=3, column=1)

  @property
  def current_price(self):
    return self.price_history[-1]

  def render(self):
    self.line.set_ydata(self.price_history[-12:])
    self.fig.canvas.draw()
    self.fig.canvas.flush_events()

  def add_monthly_price(self, current_price):
    self.price_history.append(current_price)
