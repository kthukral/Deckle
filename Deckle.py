from gi.repository import Gtk, Gdk
import cairo

class DeckleGui(Gtk.Window):

    lines = []
           
    def __init__(self):
        self.buildUI()

    def buildUI(self):
        
        builder = Gtk.Builder()
        builder.add_from_file("Deckle.glade")
        builder.connect_signals(self)

        self.window = builder.get_object("window1")
        self.menubar = builder.get_object("menubar1")
        self.toolbar = builder.get_object("toolbar1")
        self.drawingArea = builder.get_object("drawingarea1")
        self.statusbar = builder.get_object("statusbar1")

        self.window.show_all()

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onFileNew(self, *args):
        self.statusbar.push(0, "File>New")
   
    def mainDraw(self, drawingArea, cr):
        print ("Drawing...")
        cr.set_source_rgb(255/255, 243/255, 180/255)
        cr.paint()
        cr.set_source_rgb(35/255, 17/255, 9/255)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)
        if len(self.lines) > 0:
            for line in self.lines:
                if len(line) > 1:
                    cr.move_to(line[0][0], line[0][1])
                    for point in line:
                        cr.line_to(point[0], point[1])
                    cr.stroke()

    def onDAButtonPress(self, widget, event):
        print ("Click at:  ", 
            int(event.x), ", ", 
            int(event.y), sep="")
        self.lines.append([])
        self.lines[len(self.lines)-1].append((event.x, event.y))
        return True

    def onDAButtonRelease(self, widget, event):
        print ("Gone!")
        return True

    def onDAMotion(self, widget, event):
        print ("Motion at: ", 
            int(event.x), ", ", 
            int(event.y), sep="")
        self.lines[len(self.lines)-1].append( (event.x, event.y) )
        self.drawingArea.queue_draw()

DeckleGui = DeckleGui()
Gtk.main()
