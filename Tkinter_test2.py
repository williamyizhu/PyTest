import tkinter as tk

# gui configuration list
config_list = list()
config_list.append({'var':'vol_ref', 'master':'section1', 'text':'Reference', 'fill':'both', 'expand':'yes', 'widget':'Spinbox', 'from_':0, 'to':10, 'increment':2})
config_list.append({'var':'slope_ref', 'master':'section2', 'text':'Volatility', 'fill':'both', 'expand':'yes', 'widget':'Spinbox', 'from_':0, 'to':10, 'increment':2})
config_list.append({'var':'VCR', 'master':'section2', 'text':'Slope', 'fill':'both', 'expand':'yes', 'widget':'Spinbox', 'from_':0, 'to':10, 'increment':1})

# create the root of the gui
root = tk.Tk()


section1 = tk.LabelFrame(master=root, text='abc')
section1.pack(side = tk.LEFT, fill='both', expand='yes')


section2 = tk.LabelFrame(master=root, text='xyz')
section2.pack(side = tk.LEFT, fill='both', expand='yes')

def comm(txt, obj_list):
    print('abc')
    print(obj_list[0].get())
    print(txt)
    
bluebutton = tk.Button(section2, text = "Blue", fg = "blue", command=comm)
bluebutton.pack()

obj_list = list()
for i in config_list:
#     create a label frame around the object
    labelframe = eval('''tk.LabelFrame(master=%s, text='%s')''' % (i['master'], i['text']))
    eval('''labelframe.pack(fill='%s', expand='%s')''' % (i['fill'], i['expand']))
#     different object may have different params
    if i['widget']=='Spinbox':
        obj = eval('''tk.Spinbox(labelframe, from_=%s, to=%s, increment=%s, command=lambda:comm('sbc',obj_list))''' % (i['from_'], i['to'], i['increment']))
        obj.pack()
#     append object to the obj_list
    obj_list.append(obj)


tk.mainloop()



