from gi.repository import Gtk
from gi.repository import Gdk

class DeckleGui(Gtk.Window):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("Deckle.glade")
        builder.connect_signals(self)

        self.window = builder.get_object("window1")
        self.menubar = builder.get_object("menubar1")
        self.toolbar = builder.get_object("toolbar1")
        
        self.drawingArea = builder.get_object("drawingarea1")
        self.drawingArea.add_events(Gdk.EventMask.BUTTON1_MOTION_MASK)
        self.drawingArea.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        
        self.statusbar = builder.get_object("statusbar1")

        self.window.show_all()

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onFileNew(self, *args):
        self.statusbar.push(0, "File>New")
   
    def mainDraw(self, drawingArea, cr):
        print ("Drawing...")

    def onDAButtonPress(self, widget, event):
        print ("Click at:  ", 
            int(event.x), ", ", 
            int(event.y), ", state: ", 
            event.state, sep="")
        return True

    def onDAMotion(self, widget, event):
        print ("Motion at: ", 
            int(event.x), ", ", 
            int(event.y),", state: ", 
            event.state, sep="")

DeckleGui = DeckleGui()
Gtk.main()
