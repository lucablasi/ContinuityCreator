from scene_detective import scene_detective
from subber import scene2sub, sub2srt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filepath = askopenfilename()
scene_list = scene_detective(filepath, threshold=30)
scene_sublist = scene2sub(scene_list)
sub2srt(scene_sublist, 'Takes')
print('Done!')
