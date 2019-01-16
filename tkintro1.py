
'''
How to change the Size, Colour and Font of text in tkinter widgets
https://www.tutorialspoint.com/python/tk_fonts.htm




grid is used to lay out widgets in a grid.
 Another answer says it "overlays a graph" which is a bit of a misnomer.
 It doesn't overlay anything, it merely arranges widgets
 along row and column boundaries. It is great for creating tables and other
  structured types of layouts.

pack lays things out along the sides of a box.
It excels at doing layouts where everything is on a single row or
in a single column (think rows of buttons in a toolbar or dialog box).
It's also useful for very simple layouts such as a navigator on the left
and a main work area on the right. It can be used
to create very complex layouts but
it gets tricky until you fully understand the packing algorithm.

You cannot use both grid and pack with widgets that have a common parent.
 Your app may work but it is much more likely to get into an infinite loop
 as each manager tries to layout the widgets, then the other notices
  the widgets change size and try to adjust, etc. etc.

The third manage is place. Place is great for doing either absolute positioning
 (ie: place widget at a given x/y)
 or relative (eg: place a widget on the right edge of some other widget).

While you cannot mix grid and pack within the same
container (a container is typically a frame),
you can use both grid and pack within a single application. 
This is very, very common since each has strengths and weaknesses.

'''
from tkinter import*

# create the root window

root = Tk()
root.title('Labeler')
root.geometry("200x200")

# create a frame in the window to hold other widgets

app = Frame(root)
app.grid()

# create a label widget in the frame

lbl1 = Label(app, text = " I'm just a simple label! Please, be kind to Me", font=('Comic Sans MS', 30," bold italic"), bg='Green', fg='blue')
lbl1.grid()

lbl2 = Label(app, text = " I'm just a simple label! Please, be kind to Me", font=('Comic Sans MS', 20," bold italic"), bg='Green', fg='yellow')
lbl2.grid()

lbl3 = Label(app, text = " I'm just a simple label! Please, be kind to Me", font=('Comic Sans MS', 15," bold italic"), bg='Green', fg='red')
lbl3.grid()

lbl4 = Label(app, text = " I'm just a simple label! Please, be kind to Me", font=('Comic Sans MS', 12," bold italic"), bg='Green', fg='magenta')
lbl4.grid()

lbl5 = Label(app, text = " I'm just a simple label! Please, be kind to Me", font=('Comic Sans MS', 10," bold italic"), bg='Green', fg='Fuchsia')
lbl5.grid()
# lbl.pack()


# kick off the window's event
root.mainloop()
