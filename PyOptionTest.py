import os
import sys
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\PyShare'))
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\PricingModel'))
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\VolatilityModel'))
sys.path.append(os.path.join(os.path.abspath('..'), 'PyShare\\OptionAnalysis'))
import datetime as dt
import Wing
import BlackScholesMerton

bsm = BlackScholesMerton.BlackScholesMerton()

expiry_date = dt.datetime.strptime('20170324', '%Y%m%d')
valuation_date = dt.datetime.strptime('20170322', '%Y%m%d')

diff = 0.01
option1, process1 = bsm.pricing('c', 1000, expiry_date, valuation_date, 1023, 0, 0, 0.3)
bsm.print_all(option1)

option2, process2 = bsm.pricing('c', 1000 + diff, expiry_date, valuation_date, 1023, 0, 0, 0.3)
bsm.print_all(option2)

option1.strikeSensitivity()
option2.strikeSensitivity()

(option1.strikeSensitivity() + option2.strikeSensitivity()) / 2

(option2.NPV() - option1.NPV()) / diff


# implied volatility

option, process = bsm.pricing('p', 1000, expiry_date, valuation_date, 1023, 0, 0, 0.3)
bsm.print_all(option)

bsm.implied_volatility('p', 1000, expiry_date, valuation_date, 1023, 0, 0, 0.3, 10)
