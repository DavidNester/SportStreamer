#!/usr/bin/python
# -*- coding: utf-8 -*-
#from tkinter import *   # from x import * is bad practice
#from tkinter.ttk import *
from Utility import *
# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame


def MouseWheelHandler(event):

    def delta(event):
        if event.num == 5 or event.delta < 0:
            return -1
        return 1

    return delta(event)


class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, style, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = canvas = Canvas(self, bg=style,bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)

        # create a frame inside the canvas which will be scrolled with it
        #self.interior = interior = Frame(self.canvas,style='SF.TFrame')
        self.interior = interior = OldFrame(self.canvas, bg=style)
        interior_id = self.canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        self.interior.bind('<Enter>', self._bound_to_mousewheel)
        self.interior.bind('<Leave>', self._unbound_to_mousewheel)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        self.canvas.bind('<Configure>', _configure_canvas)

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(MouseWheelHandler(event), "units")


if __name__ == "__main__":

    class SampleApp(Tk):
        def __init__(self, *args, **kwargs):
            root = Tk.__init__(self, *args, **kwargs)
            style = Style(self)
            style.configure("TFrame", background="#333")
            style.configure('SF.TFrame', background='SeaGreen3')
            # sport button
            style.configure('SB.TButton', background='red', padx=2, pady=10)
            style.configure('TButton', padx=10)

            self.frame1 = VerticalScrolledFrame(root, style=style)
            self.frame1.pack(side=LEFT)
            buttons = []
            for i in range(10):
                buttons.append(Button(self.frame1.interior, text="Button " + str(i)))
                buttons[-1].pack()
            self.frame2 = VerticalScrolledFrame(root, style=style)
            self.frame2.pack(side=LEFT)
            buttons = []
            for i in range(10):
                buttons.append(Button(self.frame2.interior, text="Button " + str(i), style='SB.TButton'))
                buttons[-1].pack()
    class App(Tk):
        def __init__(self, *args, **kwargs):
            root = Tk.__init__(self, *args, **kwargs)
            #self.attributes('-alpha',0.3)
            style = Style(self)
            style.configure("TFrame", background="#333")
            style.configure('SF.TFrame', bg='SeaGreen3')
            # sport button
            style.configure('SB.TButton', highlightbackground='red', padx=2, pady=10)
            style.configure('TButton', padx=10)

            self.frame1 = Frame(root, style='SF.TFrame')
            self.frame1.pack(side=LEFT)
            buttons = []
            for i in range(10):
                buttons.append(Button(self.frame1, text="Button " + str(i)))
                buttons[-1].pack(pady=10)
            self.frame2 = Frame(root)
            self.frame2.pack(side=LEFT)
            buttons = []
            for i in range(10):
                buttons.append(Button(self.frame2, text="Button " + str(i), style='SB.TButton'))
                buttons[-1].pack()


    #app = SampleApp()
    app = App()
    app.mainloop()