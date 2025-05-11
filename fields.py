from tkinter import *
from tkinter import ttk

def input_fields(root):
  frame = ttk.Frame(root)
  frame.grid(row=0, column=0,columnspan=4, sticky='w', padx=30, pady=10)
  field_1 = ttk.Entry(frame, width=120)
  field_1.grid(row=0, column=0, sticky='w') 
  field_1.insert(0, 'Path/to/your/file')

  frame_1 = ttk.Entry(root)
  frame_1.grid(row=1,column=0,columnspan=4, sticky='w', padx=30, pady=10)
  style = ttk.Style()
  style.configure('Transparent.TEntry', fieldbackground='white', borderwidth=0)
  label1 = ttk.Label(frame_1, text='From')
  label1.grid(row=0, column=0, padx=(0, 5), sticky='e')
  field_2 = ttk.Entry(frame_1, width=20, style='Transparent.TEntry')
  field_2.grid(row=0,column=1,  padx=(0, 10), sticky='w')
  field_2.insert(0,'2025-05-10')
  label2 = ttk.Label(frame_1, text='To')
  label2.grid(row=0, column=2, padx=(0, 5), sticky='e')
  field_3 = ttk.Entry(frame_1, width=20, style='Transparent.TEntry')
  field_3.grid(row=0,column=3,  padx=(0, 20), sticky='w')
  field_3.insert(0,'2025-05-10')

  return {'frame': frame, 'frame_1': frame_1, 'field_1': field_1, 'field_2': field_2, 'field_3': field_3}