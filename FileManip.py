import re
from gi.repository import Gtk

class File(Gtk.Window):

    def save_file (self, data):
        filepath = self.get_file()
        f = open (filepath, 'w')
        paths = ""
        if len(data) > 0:
            for line in data:
                paths += self.make_path(line)
        
        file_contents = [ 
            "<?xml version='1.0' encoding='UTF-8'?>",
            "<svg xmlns='http://www.w3.org/2000/svg' version='1.1'>",
            paths,
             "</svg>"]
        svg = "\n".join(file_contents)
        f.write(svg)
        print (svg)

    def make_path(self, line):
        line_text = "<path d=' M "
        tmp_txt = re.sub ("\),", "", str(line))
        tmp_txt = re.sub (", ", ",", tmp_txt)
        tmp_txt = re.sub("[\(\)\[\]]", "", tmp_txt)
        line_text += tmp_txt
        line_text += "' style='fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:round;stroke-opacity:1' />\n"

        return line_text
    
    def get_file (self):
        dialog = Gtk.FileChooserDialog("Please choose a file", self, Gtk.FileChooserAction.SAVE)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        self.add_filters(dialog)
        response = dialog.run()
        filename = dialog.get_filename()
        if response == Gtk.ResponseType.OK:
            print ("File selected: " + filename)
        elif response == Gtk.ResponseType.CANCEL:
            print ("Cancel clicked")
        dialog.destroy()
        return filename

    def add_filters(self, dialog):
        filter_svg = Gtk.FileFilter()
        filter_svg.set_name("SVG files")
        filter_svg.add_mime_type("image/svg+xml")
        dialog.add_filter(filter_svg)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)  
