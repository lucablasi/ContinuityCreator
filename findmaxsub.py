from subber import srt2sub, cut, id_ital
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
title_path = askopenfilename()
sublist = srt2sub(title_path)
sublist = cut(sublist)
sublist = id_ital(sublist)

max_char = 0
index = 0
for i in range(len(sublist)):
    for j in range(len(sublist[i].content)):
        if len(sublist[i].content[j]) > max_char:
            max_char = len(sublist[i].content[j])
            index = sublist[i].index

print('Tallest boi is ' + str(max_char) + ' characters long')
print('With an index number of ' + str(index))
