from tkinter import Tk, Frame, BOTH

class Window(Frame):

  def __init__(self, parent):
    Frame.__init__(self, parent, background='white')
    print('Application was opened')
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.parent.title('Log browser')
    self.parent.geometry('950x650')
    #self.pack(fill=BOTH, expand=1) # takes up an entire screen size
    #self.parent.resizable(False, False)
    self.parent.protocol('WM_DELETE_WINDOW', self.finish)
  
  def finish(self):
    self.parent.destroy()
    print('Application was closed')

def main():
  root = Tk()
  window = Window(root)
  root.mainloop()

if __name__ == '__main__':
  main()