import tkinter as tk
import OptionMenuChain

class tt():
    def __init__(self):

        omc_dict = {'Asia': {'East':['Japan', 'China', 'Korea'], 'South':['Malaysia']},
                    'Europe': {'West':['Germany', 'France', 'Switzerland'], 'East':['Poland', 'Russia']},
                    'Africa': {'Good':[], 'Bad':[]},
                    'America': {}}
        omc_label = ['Continent', 'Region', 'Country']
        
        self.root = tk.Tk()
        
        self.app1 = OptionMenuChain.OptionMenuChain(self.root, omc_dict, omc_label, text='Country Selection 1', font='Verdana 10 bold')
        self.app2 = OptionMenuChain.OptionMenuChain(self.root, omc_dict, omc_label, text='Country Selection 2', font='Verdana 10 bold')

        self.b = tk.Button(self.root, text="OK", command=self.callback)
        self.b.pack()
    
        self.root.mainloop()

    def callback(self):
        print('here')
        omc_dict = {'Asia2': {'East2':['Japan', 'China', 'Korea'], 'South':['Malaysia']},
                    'Europe2': {'West2':['Germany', 'France', 'Switzerland'], 'East':['Poland', 'Russia']},
                    'Africa2': {'Good2':[], 'Bad':[]},
                    'America2': {},
                    ' ': {}}
        self.app1.change_chain_dict(omc_dict)
        xx = self.app1.get()
        print(xx)
        
if __name__ == '__main__':
    tt()
