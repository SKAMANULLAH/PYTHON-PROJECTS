from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)

        main_layout = GridLayout(cols=4, padding=10)
        main_layout.add_widget(self.result)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "C", "+",
            "=", "(", ")", ""
        ]

        for button in buttons:
            if button == "=":
                main_layout.add_widget(Button(text=button, on_press=self.on_solution))
            elif button == "C":
                main_layout.add_widget(Button(text=button, on_press=self.clear))
            else:
                main_layout.add_widget(Button(text=button, on_press=self.on_button_press))

        return main_layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text in self.operators:
            if current and (self.last_was_operator is False):
                self.result.text += button_text
            elif current == "":
                return
        else:
            self.result.text += button_text

        self.last_button = button_text
        self.last_was_operator = button_text in self.operators

    def on_solution(self, instance):
        text = self.result.text
        if text:
            try:
                solution = str(eval(self.result.text))
                self.result.text = solution
            except Exception as e:
                self.result.text = "Error"

    def clear(self, instance):
        self.result.text = ""

if __name__ == "__main__":
    CalculatorApp().run()