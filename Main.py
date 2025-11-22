from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HolaApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=50)
        
        # Etiqueta de título
        titulo = Label(
            text='¡HOLA MUNDO!',
            font_size='40sp',
            color=[1, 1, 1, 1]
        )
        
        # Botón
        boton = Button(
            text='TOCA AQUÍ',
            font_size='30sp',
            size_hint_y=0.4,
            background_color=[0.8, 0.2, 0.2, 1]
        )
        
        # Función del botón
        def cambiar_texto(instance):
            titulo.text = '¡LO LOGASTE!'
            boton.text = '¡ÉXITO!'
            boton.background_color = [0.2, 0.8, 0.2, 1]
        
        boton.bind(on_press=cambiar_texto)
        
        # Agregar al layout
        layout.add_widget(titulo)
        layout.add_widget(boton)
        
        return layout

if __name__ == '__main__':
    HolaApp().run()
