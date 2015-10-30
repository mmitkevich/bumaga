from toolz.curried import *
from datetime import datetime, timedelta
from tupl import *

dt = datetime
Bar = Tupl('open first second close', type='Bar')
BidAsk = Tupl('bid ask', type='BidAsk')
BidAskVol = Tupl('bidvol askvol', type='BidAskVol')

Timed = lambda t: Tupl('time', t, type='Timed_%s'%t.__name__)

TBar = Timed(Bar)
TBarBA = Tupl((), BidAsk, TBar, type='TBarBA')  # TBar, BidAsk, ''

#print TBarBA(open=1, first=2, second=3, close=4, bid=[-1], ask=[1], time=dt(2015, 12, 1))

bars = [TBarBA(open=100., first=101, second=102., close=103, bid=[-1], ask=[1], time=dt(2015, 12, 01))]

future = Tupl('expiration bars', type='Future')(expiration=dt(2015, 11, 15), bars=bars)

print future

