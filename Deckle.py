from gi.repository import Gtk

class DeckleGui(Gtk.Window):
    def __init__(self):
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
        cr.move_to(50, 50)
        cr.rel_line_to(0, 200)
        cr.rel_line_to(200, 0)
        cr.rel_line_to(0, -200)
        cr.rel_line_to(-200, 0)
        cr.set_source_rgb(0, 0, 0)
        cr.stroke()

DeckleGui = DeckleGui()
Gtk.main()

