from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

class SharedNotepad(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        self.textbox = TextInput(
            text=self.load_file(),
            font_size='16sp',
            background_color=(1,1,1,1)
        )
        
        btn = Button(
            text='保存内容',
            size_hint_y=None,
            height='50dp'
        )
        btn.bind(on_press=self.save_file)
        
        layout.add_widget(self.textbox)
        layout.add_widget(btn)
        return layout
    
    def load_file(self):
        if os.path.exists('notes.txt'):
            with open('notes.txt', 'r') as f:
                return f.read()
        return "输入内容..."
    
    def save_file(self, instance):
        with open('notes.txt', 'w') as f:
            f.write(self.textbox.text)

if __name__ == '__main__':
    SharedNotepad().run()
