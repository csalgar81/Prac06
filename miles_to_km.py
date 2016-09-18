from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKm(App):
    def build(self):
        self.title = "Miles to km"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self,increment):
        try:
            self.root.ids.input_number.text = str(int(self.root.ids.input_number.text)+increment)
        except ValueError:
            if increment == -1:
                self.root.ids.input_number.text = '-1'
            else:
                self.root.ids.input_number.text = '1'

    def convert_to_km(self,miles):
        try:
            self.root.ids.output_label.text =  "{:.2f}".format(int(miles)*1.61)
        except ValueError:
            self.root.ids.output_label.text = '0'

MilesToKm().run()



