from gi.repository import Gtk
from gi.repository import Gdk

class DeckleGui(Gtk.Window):


    def __init__(self):
        
        self.clicks = []
        
        builder = Gtk.Builder()
        builder.add_from_file("Deckle.glade")
        builder.connect_signals(self)

        self.window = builder.get_object("window1")
        self.menubar = builder.get_object("menubar1")
        self.toolbar = builder.get_object("toolbar1")
        
        self.drawingArea = builder.get_object("drawingarea1")
        self.drawingArea.add_events(Gdk.EventMask.BUTTON1_MOTION_MASK)
        self.drawingArea.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.drawingArea.add_events(Gdk.EventMask.BUTTON_RELEASE_MASK)
        
        self.statusbar = builder.get_object("statusbar1")

        self.window.show_all()

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onFileNew(self, *args):
        self.statusbar.push(0, "File>New")
   
    def mainDraw(self, drawingArea, cr):
        print ("Drawing...")
        cr.set_source_rgb(1,1,1)
        cr.paint()
        cr.set_source_rgb(0,0,0)
        if len(self.clicks) > 1:
            cr.move_to(self.clicks[0][0], self.clicks[0][1])
            for point in self.clicks:
                cr.line_to(point[0], point[1])
            cr.stroke()

    def onDAButtonPress(self, widget, event):
        print ("Click at:  ", 
            int(event.x), ", ", 
            int(event.y), sep="")
        return True

    def onDAButtonRelease(self, widget, event):
        print ("Gone!")

        return True

    def onDAMotion(self, widget, event):
        print ("Motion at: ", 
            int(event.x), ", ", 
            int(event.y), sep="")
        self.clicks.append( (int(event.x), int(event.y)) )
        self.drawingArea.queue_draw()

DeckleGui = DeckleGui()
Gtk.main()
