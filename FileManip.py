import re
from gi.repository import Gtk

class File(Gtk.Window):

    def save_file (self, data):
        filepath = self.get_file("w")
        if filepath == "None":
            return
        f = open (filepath, "w")
        path_seg = ""
        width = 0
        height = 0
        if len(data) > 0:
            for line in data:
                path = self.make_path(line)
                path_seg += path[0]
                width = path[1] if path[1] > width else width
                height = path[2] if path[2] > height else height
        
        file_contents = [ 
            "<?xml version='1.0' encoding='UTF-8'?>",
            "<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='" + str(width+5) + "' height='" + str(height +5) + "'>\n",
            path_seg,
            "</svg>"]
        svg = "\n".join(file_contents)
        f.write(svg)
        print ("Saved")

    def make_path(self, line):
        width = 0
        height = 0
        line_text = "\t<path d=' M "
        for point in line:
             line_text += str(point[0]) + "," + str(point[1]) + " "
             width = point[0] if point[0] > width else width
             height = point[1] if point[1] > height else height
        line_text += "' style='fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1' />\n"

        return [line_text, width, height]
    
    def get_file (self, write):
        dialog = Gtk.FileChooserDialog("Please choose a file", self, Gtk.FileChooserAction.SAVE if write=="w" else Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE if write == "w" else Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        self.add_filters(dialog)
        response = dialog.run()
        filename = str(dialog.get_filename())
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
