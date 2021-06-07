from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filepath = askopenfilename()
print("'"+filepath+"'")
