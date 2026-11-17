from time import strftime

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label


class DigitalClockApp(App):
    def build(self):
        self.title = "Digital Clock"
        Window.clearcolor = (0, 0, 0, 1)

        self.clock_label = Label(
            text="",
            color=(0, 1, 0, 1),
            bold=True,
            halign="center",
            valign="middle",
        )

        self.clock_label.bind(size=self.resize_clock)
        self.resize_clock(self.clock_label, self.clock_label.size)

        self.update_clock()
        Clock.schedule_interval(self.update_clock, 1)

        return self.clock_label

    def resize_clock(self, label, size):
        label.text_size = size
        label.font_size = min(size[0] / 5.5, size[1] / 3)

    def update_clock(self, *args):
        self.clock_label.text = strftime("%H:%M:%S")


if __name__ == "__main__":
    DigitalClockApp().run()
