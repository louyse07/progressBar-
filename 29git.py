from kivy.app import App 
from kivy.uix.progressBar import progressBar

class MinhaApp(App):
    def build(self):
        return progressBar (value=50)
    
    if __name__ == "__main__":
        MinhaApp().run()