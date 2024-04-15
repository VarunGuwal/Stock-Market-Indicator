import requests
from bs4 import BeautifulSoup
import locale
from customtkinter import *

url="https://finance.yahoo.com/most-active"

fetch=requests.get(url)

#print(fetch.text)

soup=BeautifulSoup(fetch.content,"html.parser")

#comp=["Amazon.com, Inc.", "Advanced Micro Devices, Inc.", "Intel Corporation", "NVIDIA Corporation", "Apple Inc."]
prices={}
change={}
change_per={}
volume={}
market_cap={}
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

p=soup.find('fin-streamer',{'data-symbol': 'AMZN', 'data-field': 'regularMarketPrice'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
prices.update({"AMZN":q})

p=soup.find('fin-streamer',{'data-symbol': 'AMD', 'data-field': 'regularMarketPrice'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
prices.update({"AMD":q})


p=soup.find('fin-streamer',{'data-symbol': 'INTC', 'data-field': 'regularMarketPrice'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
prices.update({"INTC":q})


p=soup.find('fin-streamer',{'data-symbol': 'NVDA', 'data-field': 'regularMarketPrice'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
prices.update({"NVDA":q})


p=soup.find('fin-streamer',{'data-symbol': 'AAPL', 'data-field': 'regularMarketPrice'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
prices.update({"AAPL":q})


p=soup.find('fin-streamer',{'data-symbol': 'AMZN', 'data-field': 'regularMarketChange'})
p=p['value']
change.update({"AMZN":p})


p=soup.find('fin-streamer',{'data-symbol': 'AMD', 'data-field': 'regularMarketChange'})
p=p['value']
change.update({"AMD":p})


p=soup.find('fin-streamer',{'data-symbol': 'INTC', 'data-field': 'regularMarketChange'})
p=p['value']
change.update({"INTC":p})


p=soup.find('fin-streamer',{'data-symbol': 'NVDA', 'data-field': 'regularMarketChange'})
p=p['value']
change.update({"NVDA":p})


p=soup.find('fin-streamer',{'data-symbol': 'AAPL', 'data-field': 'regularMarketChange'})
p=p['value']
change.update({"AAPL":p})


p=soup.find('fin-streamer',{'data-symbol': 'AMZN', 'data-field': 'regularMarketChangePercent'})
p=float(p['value'])*0.01
q="{:.2%}".format(p)
change_per.update({"AMZN":q})


p=soup.find('fin-streamer',{'data-symbol': 'AMD', 'data-field': 'regularMarketChangePercent'})
p=float(p['value'])*0.01
q="{:.2%}".format(p)
change_per.update({"AMD":q})


p=soup.find('fin-streamer',{'data-symbol': 'INTC', 'data-field': 'regularMarketChangePercent'})
p=float(p['value'])*0.01
q="{:.2%}".format(p)
change_per.update({"INTC":q})


p=soup.find('fin-streamer',{'data-symbol': 'NVDA', 'data-field': 'regularMarketChangePercent'})
p=float(p['value'])*0.01
q="{:.2%}".format(p)
change_per.update({"NVDA":q})


p=soup.find('fin-streamer',{'data-symbol': 'AAPL', 'data-field': 'regularMarketChangePercent'})
p=float(p['value'])*0.01
q="{:.2%}".format(p)
change_per.update({"AAPL":q})


p=soup.find('fin-streamer',{'data-symbol': 'AMZN', 'data-field': 'regularMarketVolume'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
volume.update({"AMZN":q})


p=soup.find('fin-streamer',{'data-symbol': 'AMD', 'data-field': 'regularMarketVolume'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
volume.update({"AMD":q})


p=soup.find('fin-streamer',{'data-symbol': 'INTC', 'data-field': 'regularMarketVolume'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
volume.update({"INTC":q})


p=soup.find('fin-streamer',{'data-symbol': 'NVDA', 'data-field': 'regularMarketVolume'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
volume.update({"NVDA":q})


p=soup.find('fin-streamer',{'data-symbol': 'AAPL', 'data-field': 'regularMarketVolume'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
volume.update({"AAPL":q})


p=soup.find('fin-streamer',{'data-symbol': 'AMZN', 'data-field': 'marketCap'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
market_cap.update({"AMZN":q})


p=soup.find('fin-streamer',{'data-symbol': 'AMD', 'data-field': 'marketCap'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
market_cap.update({"AMD":q})


p=soup.find('fin-streamer',{'data-symbol': 'INTC', 'data-field': 'marketCap'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
market_cap.update({"INTC":q})


p=soup.find('fin-streamer',{'data-symbol': 'NVDA', 'data-field': 'marketCap'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
market_cap.update({"NVDA":q})

p=soup.find('fin-streamer',{'data-symbol': 'AAPL', 'data-field': 'marketCap'})
amount=float(p['value'])
q=locale.currency(amount, grouping=True)
market_cap.update({"AAPL":q})

'''
print("Prices-")
print(prices)
print("Change-")
print(change)
print("Change %-")
print(change_per)
print("Volume")
print(volume)
print("Market Cap")
print(market_cap)
'''

stock=CTk()
stock.title("Stock Market Information")

mainlabel=CTkLabel(stock, text="Stock Market Data", font=('',30))
mainlabel.grid(row=0, column=0)

tabview=CTkTabview(master=stock)
tabview.grid()

tabview.add("Home")
tabview.add("Amazon.com")
tabview.add("AMD Inc.")
tabview.add("Intel Corp.")
tabview.add("NVIDIA Corp.")
tabview.add("Apple Inc.")
tabview.set("Home")

general="This program will be displaying the stock market information of 5 companies:\n1. Amazon.com    2. AMD Inc.  3. Intel Corp.  4. NVIDIA Corp.    5. Apple Inc."

generalinfo=CTkLabel(master=tabview.tab("Home"), text=general)
generalinfo.grid(row=0, column=0)

AMZN_market_price_label=CTkLabel(master=tabview.tab("Amazon.com"), text="Share Market Price: ", anchor=W)
AMZN_market_price_label.grid(row=0, column=0)

AMZN_market_price_value=CTkLabel(master=tabview.tab("Amazon.com"), text=prices["AMZN"])
AMZN_market_price_value.grid(row=0, column=1)

AMZN_market_change_label=CTkLabel(master=tabview.tab("Amazon.com"), text="Change: ", anchor=W)
AMZN_market_change_label.grid(row=1, column=0)

AMZN_market_change_value=CTkLabel(master=tabview.tab("Amazon.com"), text=change["AMZN"])
AMZN_market_change_value.grid(row=1, column=1)

AMZN_market_change_per_label=CTkLabel(master=tabview.tab("Amazon.com"), text="Change Percent: ", anchor=W)
AMZN_market_change_per_label.grid(row=2, column=0)

AMZN_market_change_per_value=CTkLabel(master=tabview.tab("Amazon.com"), text=change_per["AMZN"])
AMZN_market_change_per_value.grid(row=2, column=1)

AMZN_market_volume_label=CTkLabel(master=tabview.tab("Amazon.com"), text="Market volume: ", anchor=W)
AMZN_market_volume_label.grid(row=3, column=0)

AMZN_market_volume_value=CTkLabel(master=tabview.tab("Amazon.com"), text=volume["AMZN"])
AMZN_market_volume_value.grid(row=3, column=1)

AMZN_market_cap_label=CTkLabel(master=tabview.tab("Amazon.com"), text="Market Cap: ", anchor=W)
AMZN_market_cap_label.grid(row=4, column=0)

AMZN_market_cap_value=CTkLabel(master=tabview.tab("Amazon.com"), text=market_cap["AMZN"])
AMZN_market_cap_value.grid(row=4, column=1)

AMD_market_price_label=CTkLabel(master=tabview.tab("AMD Inc."), text="Share Market Price: ", anchor=W)
AMD_market_price_label.grid(row=0, column=0)

AMD_market_price_value=CTkLabel(master=tabview.tab("AMD Inc."), text=prices["AMD"])
AMD_market_price_value.grid(row=0, column=1)

AMD_market_change_label=CTkLabel(master=tabview.tab("AMD Inc."), text="Change: ", anchor=W)
AMD_market_change_label.grid(row=1, column=0)

AMD_market_change_value=CTkLabel(master=tabview.tab("AMD Inc."), text=change["AMD"])
AMD_market_change_value.grid(row=1, column=1)

AMD_market_change_per_label=CTkLabel(master=tabview.tab("AMD Inc."), text="Change Percent: ", anchor=W)
AMD_market_change_per_label.grid(row=2, column=0)

AMD_market_change_per_value=CTkLabel(master=tabview.tab("AMD Inc."), text=change_per["AMD"])
AMD_market_change_per_value.grid(row=2, column=1)

AMD_market_volume_label=CTkLabel(master=tabview.tab("AMD Inc."), text="Market volume: ", anchor=W)
AMD_market_volume_label.grid(row=3, column=0)

AMD_market_volume_value=CTkLabel(master=tabview.tab("AMD Inc."), text=volume["AMD"])
AMD_market_volume_value.grid(row=3, column=1)

AMD_market_cap_label=CTkLabel(master=tabview.tab("AMD Inc."), text="Market Cap: ", anchor=W)
AMD_market_cap_label.grid(row=4, column=0)

AMD_market_cap_value=CTkLabel(master=tabview.tab("AMD Inc."), text=market_cap["AMD"])
AMD_market_cap_value.grid(row=4, column=1)

INTC_market_price_label=CTkLabel(master=tabview.tab("Intel Corp."), text="Share Market Price: ", anchor=W)
INTC_market_price_label.grid(row=0, column=0)

INTC_market_price_value=CTkLabel(master=tabview.tab("Intel Corp."), text=prices["INTC"])
INTC_market_price_value.grid(row=0, column=1)

INTC_market_change_label=CTkLabel(master=tabview.tab("Intel Corp."), text="Change: ", anchor=W)
INTC_market_change_label.grid(row=1, column=0)

INTC_market_change_value=CTkLabel(master=tabview.tab("Intel Corp."), text=change["INTC"])
INTC_market_change_value.grid(row=1, column=1)

INTC_market_change_per_label=CTkLabel(master=tabview.tab("Intel Corp."), text="Change Percent: ", anchor=W)
INTC_market_change_per_label.grid(row=2, column=0)

INTC_market_change_per_value=CTkLabel(master=tabview.tab("Intel Corp."), text=change_per["INTC"])
INTC_market_change_per_value.grid(row=2, column=1)

INTC_market_volume_label=CTkLabel(master=tabview.tab("Intel Corp."), text="Market volume: ", anchor=W)
INTC_market_volume_label.grid(row=3, column=0)

INTC_market_volume_value=CTkLabel(master=tabview.tab("Intel Corp."), text=volume["INTC"])
INTC_market_volume_value.grid(row=3, column=1)

INTC_market_cap_label=CTkLabel(master=tabview.tab("Intel Corp."), text="Market Cap: ", anchor=W)
INTC_market_cap_label.grid(row=4, column=0)

INTC_market_cap_value=CTkLabel(master=tabview.tab("Intel Corp."), text=market_cap["INTC"])
INTC_market_cap_value.grid(row=4, column=1)

NVDA_market_price_label=CTkLabel(master=tabview.tab("NVIDIA Corp."), text="Share Market Price: ", anchor=W)
NVDA_market_price_label.grid(row=0, column=0)

NVDA_market_price_value=CTkLabel(master=tabview.tab("NVIDIA Corp."), text=prices["NVDA"])
NVDA_market_price_value.grid(row=0, column=1)

NVDA_market_change_label=CTkLabel(master=tabview.tab("NVIDIA Corp."), text="Change: ", anchor=W)
NVDA_market_change_label.grid(row=1, column=0)

NVDA_market_change_value=CTkLabel(master=tabview.tab("NVIDIA Corp."), text=change["NVDA"])
NVDA_market_change_value.grid(row=1, column=1)

NVDA_market_change_per_label=CTkLabel(master=tabview.tab("NVIDIA Corp."), text="Change Percent: ", anchor=W)
NVDA_market_change_per_label.grid(row=2, column=0)

NVDA_market_change_per_value=CTkLabel(master=tabview.tab("NVIDIA Corp."), text=change_per["NVDA"])
NVDA_market_change_per_value.grid(row=2, column=1)

NVDA_market_volume_label=CTkLabel(master=tabview.tab("NVIDIA Corp."), text="Market volume: ", anchor=W)
NVDA_market_volume_label.grid(row=3, column=0)

NVDA_market_volume_value=CTkLabel(master=tabview.tab("NVIDIA Corp."), text=volume["NVDA"])
NVDA_market_volume_value.grid(row=3, column=1)

NVDA_market_cap_label=CTkLabel(master=tabview.tab("NVIDIA Corp."), text="Market Cap: ", anchor=W)
NVDA_market_cap_label.grid(row=4, column=0)

NVDA_market_cap_value=CTkLabel(master=tabview.tab("NVIDIA Corp."), text=market_cap["NVDA"])
NVDA_market_cap_value.grid(row=4, column=1)

AAPL_market_price_label=CTkLabel(master=tabview.tab("Apple Inc."), text="Share Market Price: ", anchor=W)
AAPL_market_price_label.grid(row=0, column=0)

AAPL_market_price_value=CTkLabel(master=tabview.tab("Apple Inc."), text=prices["AAPL"])
AAPL_market_price_value.grid(row=0, column=1)

AAPL_market_change_label=CTkLabel(master=tabview.tab("Apple Inc."), text="Change: ", anchor=W)
AAPL_market_change_label.grid(row=1, column=0)

AAPL_market_change_value=CTkLabel(master=tabview.tab("Apple Inc."), text=change["AAPL"])
AAPL_market_change_value.grid(row=1, column=1)

AAPL_market_change_per_label=CTkLabel(master=tabview.tab("Apple Inc."), text="Change Percent: ", anchor=W)
AAPL_market_change_per_label.grid(row=2, column=0)

AAPL_market_change_per_value=CTkLabel(master=tabview.tab("Apple Inc."), text=change_per["AAPL"])
AAPL_market_change_per_value.grid(row=2, column=1)

AAPL_market_volume_label=CTkLabel(master=tabview.tab("Apple Inc."), text="Market volume: ", anchor=W)
AAPL_market_volume_label.grid(row=3, column=0)

AAPL_market_volume_value=CTkLabel(master=tabview.tab("Apple Inc."), text=volume["AAPL"])
AAPL_market_volume_value.grid(row=3, column=1)

AAPL_market_cap_label=CTkLabel(master=tabview.tab("Apple Inc."), text="Market Cap: ", anchor=W)
AAPL_market_cap_label.grid(row=4, column=0)

AAPL_market_cap_value=CTkLabel(master=tabview.tab("Apple Inc."), text=market_cap["AAPL"])
AAPL_market_cap_value.grid(row=4, column=1)

stock.mainloop()
