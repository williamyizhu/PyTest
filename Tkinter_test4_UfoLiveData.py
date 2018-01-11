import UfoLiveData
import tkinter as tk

class UfoLiveData2(UfoLiveData.UfoLiveData):
    def __init__(self):
        UfoLiveData.UfoLiveData.__init__(self)

#     def load_volatility_curve(self):
#         print('rewritten load volatility curve')

    def set(self):
        print('rewritten set volatility curve')

    def revert(self):
        print('rewritten revert volatility curve')

root = tk.Tk()

UfoLiveData2()

root.mainloop()