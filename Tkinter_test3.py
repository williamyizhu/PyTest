import UfoRdsQuery
import tkinter as tk

class UfoRdsQuery2(UfoRdsQuery.UfoRdsQuery):
    def __init__(self):
        UfoRdsQuery.UfoRdsQuery.__init__(self)

#     def load_volatility_curve(self):
#         print('rewritten load volatility curve')

    def set(self):
        print('rewritten set volatility curve')

    def revert(self):
        print('rewritten revert volatility curve')

root = tk.Tk()

UfoRdsQuery2()

root.mainloop()