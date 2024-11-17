import tkinter as tk
import datetime
from datetime import timedelta
from matplotlib.pyplot import pause

import player
import news
import graph

delta = timedelta(days=1)

from datetime import date

time_value = date(2020, 1, 1)
pause_value = False

# previous_news = None


def update():

  global delta, time_value, go, news_widget, previous_news, pleb, net, money

  share_text.set(str(pleb.share))
  if not pause_value:
    monthly_update = time_value.month != (time_value + delta).month
    time_value += delta
    time.config(text=time_value)

    net.set(f"${pleb.calculate_networth(go.current_price)}")
    money.set(f"${pleb.cash}")

    if monthly_update:
      news_widget.update()

      # if previous_news is not None:
      go.add_monthly_price(go.current_price + news_widget.previous_impact * 10)
      go.render()

      # previous_news = news_widget.current_impact


#Time Value
def tick():
  update()
  window.after(1000, tick)


window = tk.Tk()
window.title("Stock Game")
window.geometry("550x300")

###
news_widget = news.NewsWidget(window)
pleb = player.Player()


def speed_update(current_value):
  global delta
  if current_value == ">":
    delta = timedelta(days=3)
    return ">>"
  elif current_value == ">>":
    delta = timedelta(days=7)
    return ">>>"
  elif current_value == ">>>":
    delta = timedelta(days=1)
    return ">"


def pause_update(current_value):
  global pause_value
  if current_value == "❚❚":
    pause_value = False

    return "▶"
  else:

    pause_value = True
    return "❚❚"


from PIL import ImageTk, Image

# raw_image = Image.open("Cool stock stuff.webp")
# img = raw_image.resize((400, 275))
# img = ImageTk.PhotoImage(img)
# panel = tk.Label(window, image=img)
# panel.grid(row=3, column=1)
go = graph.GraphWidget(root=window)
go.render()

buy_and_sell_frame = tk.Frame(window)
buy_and_sell_frame.grid(row=8, column=9)

buy = tk.Button(buy_and_sell_frame,
                text="Buy",
                command=lambda: pleb.buy(go.current_price))
buy.grid(row=0, column=0)

sell = tk.Button(buy_and_sell_frame,
                 text="Sell",
                 command=lambda: pleb.sell(go.current_price))

sell.grid(row=0, column=1)

stockgame = tk.Label(text="Stock Game", font=("Arial", 25))
stockgame.grid(row=0, column=1)

# networth = tk.Label(text="NetWorth", font=("Arial", 7))
# networth.grid(row=1, column=0)

net = tk.StringVar()
netmoney = tk.Label(textvariable=net, font=("Arial", 15))
netmoney.grid(row=1, column=0)
net.set(f"${pleb.calculate_networth(go.current_price)}")

level = tk.Label(font=("Arial", 16), text="Level")
level.grid(row=0, column=9)

time = tk.Label(font=("Arial", 16), text=time_value)
time.grid(row=1, column=9)

#money
money = tk.StringVar()
money_label = tk.Label(textvariable=money, font=("Arial", 15))
money_label.grid(row=0, column=0)
money.set(f"${pleb.cash}")

#speed value
fast = tk.StringVar(value=">")
fast_forward = tk.Button(textvariable=fast,
                         width=5,
                         height=1,
                         command=lambda: fast.set(speed_update(fast.get())),
                         font=("Arial", 15))
fast_forward.grid(row=9, column=9)

news_title = tk.Label(text="NEWS", font=("Arial", 15))
news_title.grid(row=8, column=1)

stocks_frame = tk.Frame(window)
stocks_frame.grid(row=3, column=9)

#pause value
pause_text = tk.StringVar(value="▶")
pause = tk.Button(
    textvariable=pause_text,
    command=lambda: pause_text.set(pause_update(pause_text.get())))
pause.grid(row=9, column=0)

share_text = tk.StringVar(value="0")
share = tk.Label(textvariable=share_text, font=("Arial", 17))
share.grid(row=7, column=9)

# olves = tk.Button(stocks_frame, text="Olves")
# olves.grid(row=0, column=0)

# acer = tk.Button(stocks_frame, text="Acer")
# acer.grid(row=1, column=0)

# coding_dinds = tk.Button(stocks_frame, text="coding_dinds")
# coding_dinds.grid(row=2, column=0)

# mousey = tk.Button(stocks_frame, text="Mousey")
# mousey.grid(row=3, column=0)

# red_bricks = tk.Button(stocks_frame, text="red_bricks")
# red_bricks.grid(row=4, column=0)

tick()
tk.mainloop()
