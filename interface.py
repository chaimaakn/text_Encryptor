from tkinter import Image
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import Color, RoundedRectangle,Rectangle,Ellipse
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.uix.widget import Widget
from base64 import b64encode
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as symmetric_padding
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
import threading
import os
import base64
import cv2
import pygame
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import rsa,dh
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

kivy.require('1.11.1')

class CryptoApp(App):

    def build(self):
        self.icon = 'assets/Crypto.png'  # Set your app icon here if you have one
        self.title = 'CryptoApp'
        sm = ScreenManager(transition=FadeTransition())

        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(EncryptionMethodScreen(name='methods'))
        sm.add_widget(Asymmetricmethods(name='asymmetric'))
        sm.add_widget(Symmetricmethods(name='symmetric'))
        sm.add_widget(Hybridmethods(name='hybrid'))
        sm.add_widget(AESmethod(name=('AES')))
        sm.add_widget(TripleDESmethode(name=('3DES')))
        sm.add_widget(ChaCha20method(name=('chacha20')))
        sm.add_widget(RC4method(name=('RC4')))
        sm.add_widget(RSAmethod(name=('RSA')))
        sm.add_widget(Deffie_halmanmethode(name=('DH')))
        sm.add_widget(DSAmethod(name=('DSA')))
        sm.add_widget(ECDHmethod(name=('ECDH')))
        sm.add_widget(KeyGeneratorScreenAES(name=('keyAES')))
        sm.add_widget(KeyGeneratorScreen3DES(name=('key3DES')))
        sm.add_widget(KeyGeneratorScreenChacha20(name=('keycha')))
        sm.add_widget(KeyGeneratorScreenRC4(name=('keyRC4')))
        sm.add_widget(EncryptionScreenAES(name=('encryptAES')))
        sm.add_widget(DecryptionScreenAES(name=('decryptAES')))
        sm.add_widget(EncryptionScreen3DES(name=('encrypt3DES')))
        sm.add_widget(DecryptionScreen3DES(name=('decrypt3DES')))
        sm.add_widget(EncryptionScreenchacha20(name=('encryptchacha20')))
        sm.add_widget(DecryptionScreenchacha20(name=('decryptchacha20')))
        sm.add_widget(EncryptionScreenRC4(name=('encryptRC4')))
        sm.add_widget(DecryptionScreenRC4(name=('decryptRC4')))
        sm.add_widget(KeyGeneratorScreenRSA(name=('keyRSA')))

        sm.add_widget(EncryptionScreenRSA1(name=('RSAencrypt1')))

        sm.add_widget(DecryptionScreenRSA1(name=('RSAdecrypt1')))

        sm.add_widget(KeyGeneratorScreenDH(name='keyDH'))
        sm.add_widget(EncryptionScreenDH(name=('encryptDH')))
        sm.add_widget(DecryptionScreenDH(name=('decryptDH')))

        
        
        return sm

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[25])
            self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        
        # Add background image
        with self.canvas.before:
            self.bg = Rectangle(source='assets/page1.png', size=self.size, pos=self.pos)
            self.bind(size=self._update_bg, pos=self._update_bg)

        layout = BoxLayout(orientation='vertical', spacing=5, padding=(50, 50, 50, 250) ) # Padding adjusted for centering vertically

        # Add logo and welcome label in a horizontal layout

        logo = Image(source='assets/logo.png', size_hint=(None, None), size=(400, 200),pos_hint={'x': 0.3, 'y': 0.05})
        welcome_label = Label(text='Welcome To Crypto', font_size='45sp', color=(1, 1, 1, 1), halign='justify')
        
        # Add empty widgets for centering
        empty_space_top = Widget(size_hint_y=None, height=50)  # Adjusted for centering vertically
        empty_space_bottom = Widget(size_hint_y=None, height=20)  # Adjusted for centering vertically
        
       
        layout.add_widget(logo)
        layout.add_widget(empty_space_bottom)
        layout.add_widget(welcome_label)
        layout.add_widget(BoxLayout(size_hint_y=None, height=2))  # Spacer

        # Add start button
        start_button = RoundedButton(text='Start now !', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'x': 0.32, 'y': 0.2})
        start_button.bind(on_press=self.change_screen)
        layout.add_widget(start_button)

        layout.add_widget(BoxLayout(size_hint_y=None, height=10))  # Spacer
       
        
        self.add_widget(layout)

    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def change_screen(self, instance):
        self.manager.current = 'methods'

class EncryptionMethodScreen(Screen):
    def __init__(self, **kwargs):
        super(EncryptionMethodScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        # Add background
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
            
        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='First choose a method', font_size='28sp', bold=True,color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_asymmetric = RoundedButton(text='Asymmetric Encryption', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_asymmetric.bind(on_press=lambda instance: self.change_screen('asymmetric'))
        btn_symmetric = RoundedButton(text='Symmetric Encryption', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_symmetric.bind(on_press=lambda instance: self.change_screen('symmetric'))
        btn_hybrid = RoundedButton(text='Hybrid Encryption', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_hybrid.bind(on_press=lambda instance:self.change_screen('hybrid'))

        # Ajoutez les boutons au layout
        layout.add_widget(btn_asymmetric)
        layout.add_widget(btn_symmetric)
        layout.add_widget(btn_hybrid)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def change_screen(self,name):
        self.manager.current = name
        
        
class Asymmetricmethods(Screen):  
    def __init__(self, **kwargs):
        super(Asymmetricmethods, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 350))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        
        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='Asymmetric methods', font_size='28sp', bold=True,color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='RSA', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Key.bind(on_press=lambda instance: self.change_screen('RSA'))
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Simulation', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_encrypt.bind(on_press=self.play_simulation)
        layout.add_widget(btn_encrypt)
        
        self.add_widget(layout)

        # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('methods'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

    def change_screen(self, name):
        self.manager.current = name   
    def play_simulation(self, instance):
        # Create a new window for the video
        self.video_screen = VideoScreen2(name='video')
        self.manager.add_widget(self.video_screen)
        self.change_screen('video')
        self.video_screen.play_video('assets/asymmetric.mp4')    
        
class Symmetricmethods(Screen):
    def __init__(self, **kwargs):
        super(Symmetricmethods, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 150))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect3 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect3, pos=self._update_rect3)
            
        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)         

        # Add instruction label
        instruction_label = Label(text='symmetric methods', font_size='28sp', bold=True,color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_AES = RoundedButton(text='AES', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_AES.bind(on_press=lambda instance: self.change_screen('AES'))
        layout.add_widget(btn_AES)

        btn_3DES = RoundedButton(text='Triple DES', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_3DES.bind(on_press=lambda instance: self.change_screen('3DES'))
        layout.add_widget(btn_3DES)

        btn_chacha20 = RoundedButton(text='ChaCha20', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_chacha20.bind(on_press=lambda instance: self.change_screen('chacha20'))
        layout.add_widget(btn_chacha20)

        btn_RC4 = RoundedButton(text='RC4', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_RC4.bind(on_press=lambda instance: self.change_screen('RC4'))
        layout.add_widget(btn_RC4)
        
        btn_simulation = RoundedButton(text='Simulation', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_simulation.bind(on_press=self.play_simulation)
        layout.add_widget(btn_simulation)
        self.add_widget(layout)
        
        # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('methods'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)
        
        

    def _update_rect3(self, instance, value):
        self.rect3.size = instance.size
        self.rect3.pos = instance.pos     

    def change_screen(self, name):
        self.manager.current = name

    def play_simulation(self, instance):
        # Create a new window for the video
        self.video_screen = VideoScreen(name='video')
        self.manager.add_widget(self.video_screen)
        self.change_screen('video')
        self.video_screen.play_video('assets/alice.mp4')

class VideoScreen(Screen):
    def __init__(self, **kwargs):
        super(VideoScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        with self.canvas.before:
            Color(156/255, 194/255, 164/255, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        self.video = Video(source='', state='stop', options={'allow_stretch': True, 'keep_ratio': False})
        self.layout.add_widget(self.video)

        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=self.stop_video)
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

        self.add_widget(self.layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def play_video(self, video_path):
        self.video.source = video_path
        self.video.state = 'play'

    def stop_video(self, instance):
        self.video.state = 'stop'
        self.manager.current = 'symmetric'
        

class VideoScreen2(Screen):
    def __init__(self, **kwargs):
        super(VideoScreen2, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        with self.canvas.before:
            Color(156/255, 194/255, 164/255, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        self.video = Video(source='', state='stop', options={'allow_stretch': True, 'keep_ratio': False})
        self.layout.add_widget(self.video)
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=self.stop_video)
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

        self.add_widget(self.layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def play_video(self, video_path):
        self.video.source = video_path
        self.video.state = 'play'

    def stop_video(self, instance):
        self.video.state = 'stop'
        self.manager.current = 'asymmetric'

class Hybridmethods(Screen):
    def __init__(self, **kwargs):
        super(Hybridmethods, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical',  spacing=35, padding=(50, 50, 50, 350))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='Hybrid methods', font_size='28sp',bold=True, color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Deffie = RoundedButton(text='Deffie_halman', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Deffie.bind(on_press=lambda instance: self.change_screen('DH'))
        layout.add_widget(btn_Deffie)
        btn_DSA = RoundedButton(text='Simulation', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_DSA.bind(on_press=self.play_simulation)
        layout.add_widget(btn_DSA)
        #btn_ECDH = RoundedButton(text='ECDH', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        #btn_ECDH.bind(on_press=lambda instance: self.change_screen('ECDH'))
        #layout.add_widget(btn_ECDH)
        self.add_widget(layout)
        # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('methods'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name   
    def play_simulation(self, instance):
        # Create a new window for the video
        self.video_screen = VideoScreen3(name='video')
        self.manager.add_widget(self.video_screen)
        self.change_screen('video')
        self.video_screen.play_video('assets/hybrid.mp4')
        
class VideoScreen3(Screen):
    def __init__(self, **kwargs):
        super(VideoScreen3, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        with self.canvas.before:
            Color(156/255, 194/255, 164/255, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        self.video = Video(source='', state='stop', options={'allow_stretch': True, 'keep_ratio': False})
        self.layout.add_widget(self.video)
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=self.stop_video)
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

        self.add_widget(self.layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def play_video(self, video_path):
        self.video.source = video_path
        self.video.state = 'play'

    def stop_video(self, instance):
        self.video.state = 'stop'
        self.manager.current = 'hybrid'  
        
        
           
class AESmethod(Screen):
    def __init__(self, **kwargs):
        super(AESmethod, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        
        # Add instruction label
        instruction_label = Label(text='AES', font_size='28sp', bold=True,color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Key.bind(on_press=lambda instance: self.change_screen('keyAES'))
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_encrypt.bind(on_press=lambda instance: self.change_screen('encryptAES'))
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        layout.add_widget(btn_decrypt)
        btn_decrypt.bind(on_press=lambda instance: self.change_screen('decryptAES'))
        self.add_widget(layout)

        # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('symmetric'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

    def change_screen(self, name):
        self.manager.current = name       
        
class TripleDESmethode(Screen):      
    def __init__(self, **kwargs):
        super(TripleDESmethode, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='Triple DES', font_size='28sp',bold=True, color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Key.bind(on_press=lambda instance: self.change_screen('key3DES'))
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_encrypt.bind(on_press=lambda instance: self.change_screen('encrypt3DES'))
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_decrypt.bind(on_press=lambda instance: self.change_screen('decrypt3DES'))
        layout.add_widget(btn_decrypt)

        # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('symmetric'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)
        self.add_widget(layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name        
        
        
class ChaCha20method(Screen):      
    def __init__(self, **kwargs):
        super(ChaCha20method, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='ChaCha20', font_size='28sp',bold=True, color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Key.bind(on_press=lambda instance: self.change_screen('keycha'))
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_encrypt.bind(on_press=lambda instance: self.change_screen('encryptchacha20'))
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_decrypt.bind(on_press=lambda instance: self.change_screen('decryptchacha20'))
        layout.add_widget(btn_decrypt)

        # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('symmetric'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)
        self.add_widget(layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name        
              
class RC4method(Screen):       
    def __init__(self, **kwargs):
        super(RC4method, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='RC4', font_size='28sp', bold=True,color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Key.bind(on_press=lambda instance: self.change_screen('keyRC4'))
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_encrypt.bind(on_press=lambda instance: self.change_screen('encryptRC4'))
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_decrypt.bind(on_press=lambda instance: self.change_screen('decryptRC4'))
        layout.add_widget(btn_decrypt)
        # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('symmetric'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)
        self.add_widget(layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name        
class RSAmethod(Screen):
    def __init__(self, **kwargs):
        super(RSAmethod, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='RSA', font_size='28sp', bold=True,color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Key.bind(on_press=lambda instance: self.change_screen('keyRSA'))
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_encrypt.bind(on_press=lambda instance: self.change_screen('RSAencrypt1'))
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_decrypt.bind(on_press=lambda instance: self.change_screen('RSAdecrypt1'))
        layout.add_widget(btn_decrypt)
        self.add_widget(layout)
                # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('asymmetric'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name
        
 
        
 
           
class Deffie_halmanmethode(Screen):
    def __init__(self, **kwargs):
        super(Deffie_halmanmethode, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='assets/Crypto.png', size_hint=(None, None), size=(150, 150))
        logo_layout.add_widget(logo)
        self.add_widget(logo_layout)
        # Add instruction label
        instruction_label = Label(text='Deffie_halman', font_size='28sp', bold=True,color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_Key.bind(on_press=lambda instance: self.change_screen('keyDH'))
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_encrypt.bind(on_press=lambda instance: self.change_screen('encryptDH'))
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        btn_decrypt.bind(on_press=lambda instance: self.change_screen('decryptDH'))
        layout.add_widget(btn_decrypt)
        self.add_widget(layout)
                # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('hybrid'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name

class DSAmethod(Screen): 
    def __init__(self, **kwargs):
        super(DSAmethod, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Add instruction label
        instruction_label = Label(text='DSA', font_size='28sp', color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        #btn_Rsa.bind(on_press=self.change_screen)
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        #btn_Rsa.bind(on_press=self.change_screen)
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        #btn_Rsa.bind(on_press=self.change_screen)
        layout.add_widget(btn_decrypt)
        self.add_widget(layout)
                # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(0.8, 0.8, 0.8, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('hybrid'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name
        
class ECDHmethod(Screen):
    
    def __init__(self, **kwargs):
        super(ECDHmethod, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 250))
        
        with self.canvas.before:
            Color(49/255, 167/255, 75/255, 1)  # 31A74B
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Add instruction label
        instruction_label = Label(text='ECDH', font_size='28sp', color=(1, 1, 1, 1), halign='justify')
        layout.add_widget(instruction_label)

        # Add encryption method buttons
        btn_Key = RoundedButton(text='Key Generator', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        #btn_Rsa.bind(on_press=self.change_screen)
        layout.add_widget(btn_Key)
        btn_encrypt = RoundedButton(text='Encrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        #btn_Rsa.bind(on_press=self.change_screen)
        layout.add_widget(btn_encrypt)
        btn_decrypt = RoundedButton(text='Decrypt', size_hint=(None, None), size=(350, 50), background_color=(49/255, 167/255, 75/255, 1), pos_hint={'center_x': 0.5})
        #btn_Rsa.bind(on_press=self.change_screen)
        layout.add_widget(btn_decrypt)
        layout.add_widget(BoxLayout(size_hint_y=None, height=20))
        self.add_widget(layout)
                # Ajouter le bouton "Back" avec AnchorLayout
        back_button_layout = AnchorLayout(anchor_x='left', anchor_y='bottom', size_hint=(None, None), size=(150, 50), padding=(20, 20, 20, 20))
        back_button = RoundedButton(text='Back', size_hint=(None, None), size=(100, 25), background_color=(0.8, 0.8, 0.8, 1))
        back_button.bind(on_press=lambda instance: self.change_screen('hybrid'))
        back_button_layout.add_widget(back_button)
        self.add_widget(back_button_layout)

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos     
    def change_screen(self,name):
        self.manager.current =name 
                  
class KeyGeneratorScreenAES(Screen):
    def __init__(self, **kwargs):
        super(KeyGeneratorScreenAES, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 50, 50, 50))
        
        # Add background color
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        
        # Add a semi-transparent green circle
        with self.canvas:
            Color(49/255, 167/255, 75/255, 0.3)  # Semi-transparent green
            self.circle = Ellipse(size=(300, 300), pos=(self.width / 2 - 150, self.height / 2 - 150))
            self.bind(size=self._update_circle, pos=self._update_circle)
            
        # Add explanation label
        explanation_label = Label(
            text="AES (Advanced Encryption Standard) is a symmetric encryption algorithm.\n "
                 "                    Click the button below to generate a random AES key",
            font_size='18sp',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(explanation_label)

        # Add button to generate key
        generate_button = Button(
            text='Generate Key',
            size_hint=(None, None),
            size=(200, 50),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0.5}
        )
        generate_button.bind(on_press=self.generate_key)
        layout.add_widget(generate_button)

        # Add a label to display the generated key with custom background
        self.key_display = Label(
            text='',
            font_size=18,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5},
            color=(49/255, 167/255, 75/255, 1) 
        )
        layout.add_widget(self.key_display)

        # Add a spacer
        layout.add_widget(BoxLayout(size_hint_y=None, height=20))

        # Add back button at the bottom
        bottom_layout = BoxLayout(size_hint_y=None, height=50)
        back_button = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 25),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0, 'center_y': 0.5}
        )
        back_button.bind(on_press=lambda x: self.change_screen('AES'))
        bottom_layout.add_widget(back_button)
        layout.add_widget(bottom_layout)
        
        self.add_widget(layout)

    def generate_key(self, instance):
        key = os.urandom(32)  # AES-256 key size
        key_base64 = b64encode(key).decode('utf-8')
        self.key_display.text = key_base64
        Clipboard.copy(key_base64)
        self.show_popup("Key has been copied to clipboard!")

    def show_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message, size_hint_y=None, height=50)
        popup_button = Button(text='Close', size_hint_y=None, height=50,background_color=(49/255, 167/255, 75/255, 1))
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title='Information', content=popup_layout, size_hint=(0.5, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name
        
    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos 

    def _update_circle(self, instance, value):
        self.circle.pos = (self.width / 2 - 150, self.height / 2 - 150)
        self.circle.size = (300, 300)

    def update_key_display_bg(self, instance, value):
        self.key_display_bg.pos = self.key_display.pos
        self.key_display_bg.size = self.key_display.size
        
        
class KeyGeneratorScreen3DES(Screen):
    def __init__(self, **kwargs):
        super(KeyGeneratorScreen3DES, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 25, 50, 50))
        
        # Add background color
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        
        # Add a semi-transparent green circle
        with self.canvas:
            Color(49/255, 167/255, 75/255, 0.3)  # Semi-transparent green
            self.circle = Ellipse(size=(300, 300), pos=(self.width / 2 - 150, self.height / 2 - 150))
            self.bind(size=self._update_circle, pos=self._update_circle)
            
        # Add explanation label
        explanation_label = Label(
            text="Triple DES (Data Encryption Standard) is a symmetric encryption algorithm with a key length of 168 bits  \n "
     
     "        Click the button below to generate a random Triple DES key ",
            font_size='18sp',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(explanation_label)

        # Add button to generate key
        generate_button = Button(
            text='Generate Key',
            size_hint=(None, None),
            size=(200, 50),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0.5}
        )
        generate_button.bind(on_press=self.generate_key)
        layout.add_widget(generate_button)

        # Add a label to display the generated key with custom background
        self.key_display = Label(
            text='',
            font_size=18,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5},
            color=(49/255, 167/255, 75/255, 1) 
        )
        layout.add_widget(self.key_display)

        # Add a spacer
        layout.add_widget(BoxLayout(size_hint_y=None, height=20))

        # Add back button at the bottom
        bottom_layout = BoxLayout(size_hint_y=None, height=50)
        back_button = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 25),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0, 'center_y': 0.5}
        )
        back_button.bind(on_press=lambda x: self.change_screen('3DES'))
        bottom_layout.add_widget(back_button)
        layout.add_widget(bottom_layout)
        
        self.add_widget(layout)

    def generate_key(self, instance):
        key = os.urandom(8)  
        key_base64 = b64encode(key).decode('utf-8')
        self.key_display.text = key_base64
        Clipboard.copy(key_base64)
        self.show_popup("Key has been copied to clipboard!")

    def show_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        popup_label = Label(text=message, size_hint_y=None, height=25)
        popup_button = Button(text='Close', size_hint_y=None, height=50,background_color=(49/255, 167/255, 75/255, 1))
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title='Information', content=popup_layout, size_hint=(0.5, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name
        
    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos 

    def _update_circle(self, instance, value):
        self.circle.pos = (self.width / 2 - 150, self.height / 2 - 150)
        self.circle.size = (300, 300)

    def update_key_display_bg(self, instance, value):
        self.key_display_bg.pos = self.key_display.pos
        self.key_display_bg.size = self.key_display.size
        
class KeyGeneratorScreenChacha20(Screen):
    def __init__(self, **kwargs):
        super(KeyGeneratorScreenChacha20, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 25, 50, 50))
        
        # Add background color
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        
        # Add a semi-transparent green circle
        with self.canvas:
            Color(49/255, 167/255, 75/255, 0.3)  # Semi-transparent green
            self.circle = Ellipse(size=(300, 300), pos=(self.width / 2 - 150, self.height / 2 - 150))
            self.bind(size=self._update_circle, pos=self._update_circle)
            
        # Add explanation label
        explanation_label = Label(
            text=
            "ChaCha20 is a secure symmetric encryption algorithm with a key length of 256 bits\n" 
            "                   Click the button below to generate a random ChaCha20 key",
            font_size='18sp',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(explanation_label)

        # Add button to generate key
        generate_button = Button(
            text='Generate Key',
            size_hint=(None, None),
            size=(200, 50),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0.5}
        )
        generate_button.bind(on_press=self.generate_key)
        layout.add_widget(generate_button)

        # Add a label to display the generated key with custom background
        self.key_display = Label(
            text='',
            font_size=18,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5},
            color=(49/255, 167/255, 75/255, 1) 
        )
        layout.add_widget(self.key_display)

        # Add a spacer
        layout.add_widget(BoxLayout(size_hint_y=None, height=20))

        # Add back button at the bottom
        bottom_layout = BoxLayout(size_hint_y=None, height=50)
        back_button = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 25),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0, 'center_y': 0.5}
        )
        back_button.bind(on_press=lambda x: self.change_screen('chacha20'))
        bottom_layout.add_widget(back_button)
        layout.add_widget(bottom_layout)
        
        self.add_widget(layout)

    def generate_key(self, instance):
        key = os.urandom(32)  
        key_base64 = base64.b64encode(key).decode('utf-8')
        self.key_display.text = key_base64
        Clipboard.copy(key_base64)
        self.show_popup("Key has been copied to clipboard!")

    def show_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        popup_label = Label(text=message, size_hint_y=None, height=50)
        popup_button = Button(text='Close', size_hint_y=None, height=50,background_color=(49/255, 167/255, 75/255, 1))
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title='Information', content=popup_layout, size_hint=(0.5, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name
        
    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos 

    def _update_circle(self, instance, value):
        self.circle.pos = (self.width / 2 - 150, self.height / 2 - 150)
        self.circle.size = (300, 300)

    def update_key_display_bg(self, instance, value):
        self.key_display_bg.pos = self.key_display.pos
        self.key_display_bg.size = self.key_display.size

class KeyGeneratorScreenRC4(Screen):
    def __init__(self, **kwargs):
        super(KeyGeneratorScreenRC4, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=35, padding=(50, 25, 50, 50))
        
        # Add background color
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        
        # Add a semi-transparent green circle
        with self.canvas:
            Color(49/255, 167/255, 75/255, 0.3)  # Semi-transparent green
            self.circle = Ellipse(size=(300, 300), pos=(self.width / 2 - 150, self.height / 2 - 150))
            self.bind(size=self._update_circle, pos=self._update_circle)
            
        # Add explanation label
        explanation_label = Label(
            text=
        "RC4 (Rivest Cipher 4) is a symmetric stream cipher algorithm with a key length of 128 bits \n"
        "                    Click the button below to generate a random RC4 key\n",
            font_size='18sp',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(explanation_label)

        # Add button to generate key
        generate_button = Button(
            text='Generate Key',
            size_hint=(None, None),
            size=(200, 50),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0.5}
        )
        generate_button.bind(on_press=self.generate_key)
        layout.add_widget(generate_button)

        # Add a label to display the generated key with custom background
        self.key_display = Label(
            text='',
            font_size=18,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5},
            color=(49/255, 167/255, 75/255, 1) 
        )
        layout.add_widget(self.key_display)

        # Add a spacer
        layout.add_widget(BoxLayout(size_hint_y=None, height=20))

        # Add back button at the bottom
        bottom_layout = BoxLayout(size_hint_y=None, height=50)
        back_button = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 25),
            background_color=(49/255, 167/255, 75/255, 1),
            pos_hint={'center_x': 0, 'center_y': 0.5}
        )
        back_button.bind(on_press=lambda x: self.change_screen('RC4'))
        bottom_layout.add_widget(back_button)
        layout.add_widget(bottom_layout)
        
        self.add_widget(layout)

    def generate_key(self, instance):
        key = os.urandom(16)  
        key_base64 = b64encode(key).decode('utf-8')
        self.key_display.text = key_base64
        Clipboard.copy(key_base64)
        self.show_popup("Key has been copied to clipboard!")

    def show_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        popup_label = Label(text=message, size_hint_y=None, height=50)
        popup_button = Button(text='Close', size_hint_y=None, height=50,background_color=(49/255, 167/255, 75/255, 1))
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title='Information', content=popup_layout, size_hint=(0.5, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name
        
    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos 

    def _update_circle(self, instance, value):
        self.circle.pos = (self.width / 2 - 150, self.height / 2 - 150)
        self.circle.size = (300, 300)

    def update_key_display_bg(self, instance, value):
        self.key_display_bg.pos = self.key_display.pos
        self.key_display_bg.size = self.key_display.size



class EncryptionScreenAES(Screen):
    def __init__(self, **kwargs):
        super(EncryptionScreenAES, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Encryption', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Encrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter plain text to be Encrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Encrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)

        # Encrypt button
        self.encrypt_button = Button(text='Encrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.encrypt_button.bind(on_press=self.encrypt_message)

        # Encrypted output label
        encrypted_label_title = Label(text='Encrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))

        self.encrypted_label = Label(text='', size_hint_y=None, height=40)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('AES'))

        # Adding widgets to the main layout
        self.main_layout.add_widget(self.key_input)
        self.key_input.opacity = 0  # Start with key_input hidden

        self.main_layout.add_widget(self.encrypt_button)
        self.main_layout.add_widget(encrypted_label_title)
        self.main_layout.add_widget(self.encrypted_label)
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
        else:
            self.key_input.opacity = 0  # Hide key_input

    def encrypt_message(self, instance):
        message = self.text_input.text.encode('utf-8')
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            key = base64.b64encode(os.urandom(32)).decode('utf-8')

        encrypted_data = encrypt_messageAES(message, key)
        self.encrypted_label.text = encrypted_data.decode('utf-8')
        Clipboard.copy(self.encrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 32
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos


def pad_messageAES(message):
      padder = symmetric_padding.PKCS7(algorithms.AES.block_size).padder()
      padded_message = padder.update(message) + padder.finalize()
      return padded_message

def encrypt_messageAES(message, encoded_key):
      iv = os.urandom(16)
      key = base64.b64decode(encoded_key)
      cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
      encryptor = cipher.encryptor()
      padded_message = pad_messageAES(message)
      ciphertext = encryptor.update(padded_message) + encryptor.finalize()
      return base64.b64encode(iv + ciphertext)
  
  
class DecryptionScreenAES(Screen):
    def __init__(self, **kwargs):
        super(DecryptionScreenAES, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Decryption', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Decrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter text to be Decrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Decrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)
        self.key_input.opacity = 0  # Start with key_input hidden
        self.main_layout.add_widget(self.key_input)

        # Decrypt button
        self.decrypt_button = Button(text='Decrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.decrypt_button.bind(on_press=self.decrypt_message)
        self.main_layout.add_widget(self.decrypt_button)

        # Decrypted output label
        decrypted_label_title = Label(text='Decrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(decrypted_label_title)

        self.decrypted_label = Label(text='', size_hint_y=None, font_size="23sp",bold=True,height=40)
        self.main_layout.add_widget(self.decrypted_label)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('AES'))
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
            self.key_input.disabled = False  # Enable key_input
        else:
            self.key_input.opacity = 0  # Hide key_input
            self.key_input.disabled = True  # Disable key_input

    def decrypt_message(self, instance):
        ciphertext = base64.b64decode(self.text_input.text.encode('utf-8'))
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            self.show_error("A custom key must be used for decryption.")
            return

        decrypted_data = decrypt_messageAES(ciphertext, base64.b64decode(key))
        self.decrypted_label.text = decrypted_data.decode('utf-8')
        Clipboard.copy(self.decrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 32
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

def unpad_messageAES(padded_message):
    unpadder = symmetric_padding.PKCS7(algorithms.AES.block_size).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message

def decrypt_messageAES(ciphertext, key):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(actual_ciphertext) + decryptor.finalize()
    message = unpad_messageAES(padded_message)
    return message
class EncryptionScreen3DES(Screen):
    def __init__(self, **kwargs):
        super(EncryptionScreen3DES, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Encryption', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Encrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter plain text to be Encrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Encrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)

        # Encrypt button
        self.encrypt_button = Button(text='Encrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.encrypt_button.bind(on_press=self.encrypt_message)

        # Encrypted output label
        encrypted_label_title = Label(text='Encrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))

        self.encrypted_label = Label(text='', size_hint_y=None, height=40)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('3DES'))

        # Adding widgets to the main layout
        self.main_layout.add_widget(self.key_input)
        self.key_input.opacity = 0  # Start with key_input hidden

        self.main_layout.add_widget(self.encrypt_button)
        self.main_layout.add_widget(encrypted_label_title)
        self.main_layout.add_widget(self.encrypted_label)
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
        else:
            self.key_input.opacity = 0  # Hide key_input

    def encrypt_message(self, instance):
        message = self.text_input.text.encode('utf-8')
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            key = base64.b64encode(os.urandom(8)).decode('utf-8')

        encrypted_data = encrypt_message3DES(message, key)
        self.encrypted_label.text = encrypted_data.decode('utf-8')
        Clipboard.copy(self.encrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 8
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

def pad_message3DES(message):
    padder = symmetric_padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_message = padder.update(message) + padder.finalize()
    return padded_message

def encrypt_message3DES(message, encoded_key):
    iv = os.urandom(8)  # DES utilise un IV de 8 octets
    key=base64.b64decode(encoded_key)
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = pad_message3DES(message)
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext)

class DecryptionScreen3DES(Screen):
    def __init__(self, **kwargs):
        super(DecryptionScreen3DES, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Decryption', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Decrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter text to be Decrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Decrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)
        self.key_input.opacity = 0  # Start with key_input hidden
        self.main_layout.add_widget(self.key_input)

        # Decrypt button
        self.decrypt_button = Button(text='Decrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.decrypt_button.bind(on_press=self.decrypt_message)
        self.main_layout.add_widget(self.decrypt_button)

        # Decrypted output label
        decrypted_label_title = Label(text='Decrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(decrypted_label_title)

        self.decrypted_label = Label(text='', size_hint_y=None, font_size="23sp",bold=True,height=40)
        self.main_layout.add_widget(self.decrypted_label)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('3DES'))
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
            self.key_input.disabled = False  # Enable key_input
        else:
            self.key_input.opacity = 0  # Hide key_input
            self.key_input.disabled = True  # Disable key_input

    def decrypt_message(self, instance):
        ciphertext = base64.b64decode(self.text_input.text.encode('utf-8'))
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            self.show_error("A custom key must be used for decryption.")
            return

        decrypted_data = decrypt_message3DES(ciphertext, base64.b64decode(key))
        self.decrypted_label.text = decrypted_data.decode('utf-8')
        Clipboard.copy(self.decrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 8
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

def unpad_message3DES(padded_message):
    unpadder = symmetric_padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message

def decrypt_message3DES(ciphertext, key):
    
    iv = ciphertext[:8]  # DES utilise un IV de 8 octets
    actual_ciphertext = ciphertext[8:]
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(actual_ciphertext) + decryptor.finalize()
    message = unpad_message3DES(padded_message)
    return message

class EncryptionScreenchacha20(Screen):
    def __init__(self, **kwargs):
        super(EncryptionScreenchacha20, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Encryption - ChaCha20', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Encrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter plain text to be Encrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Encrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)

        # Encrypt button
        self.encrypt_button = Button(text='Encrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.encrypt_button.bind(on_press=self.encrypt_message)

        # Encrypted output label
        encrypted_label_title = Label(text='Encrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))

        self.encrypted_label = Label(text='', size_hint_y=None, height=40)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('chacha20'))

        # Adding widgets to the main layout
        self.main_layout.add_widget(self.key_input)
        self.key_input.opacity = 0  # Start with key_input hidden

        self.main_layout.add_widget(self.encrypt_button)
        self.main_layout.add_widget(encrypted_label_title)
        self.main_layout.add_widget(self.encrypted_label)
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
        else:
            self.key_input.opacity = 0  # Hide key_input

    def encrypt_message(self, instance):
        message = self.text_input.text.encode('utf-8')
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            key = base64.b64encode(os.urandom(32)).decode('utf-8')

        encrypted_data = encrypt_messagechacha(message, key)
        self.encrypted_label.text = base64.b64encode(encrypted_data).decode('utf-8')
        Clipboard.copy(self.encrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 32
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

class DecryptionScreenchacha20(Screen):
    def __init__(self, **kwargs):
        super(DecryptionScreenchacha20, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Decryption - ChaCha20', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Decrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter text to be Decrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Decrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)
        self.key_input.opacity = 0  # Start with key_input hidden
        self.main_layout.add_widget(self.key_input)

        # Decrypt button
        self.decrypt_button = Button(text='Decrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.decrypt_button.bind(on_press=self.decrypt_message)
        self.main_layout.add_widget(self.decrypt_button)

        # Decrypted output label
        decrypted_label_title = Label(text='Decrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(decrypted_label_title)

        self.decrypted_label = Label(text='', size_hint_y=None, font_size="23sp",bold=True,height=40)
        self.main_layout.add_widget(self.decrypted_label)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('chacha20'))
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
            self.key_input.disabled = False  # Enable key_input
        else:
            self.key_input.opacity = 0  # Hide key_input
            self.key_input.disabled = True  # Disable key_input

    def decrypt_message(self, instance):
        ciphertext = self.text_input.text.encode('utf-8')
        ciphertext = base64.b64decode(ciphertext)
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            self.show_error("A custom key must be used for decryption.")
            return

        decrypted_data = decrypt_messagechacha(ciphertext, key)
        self.decrypted_label.text = decrypted_data.decode('utf-8')
        Clipboard.copy(self.decrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 32
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

# Encryption and Decryption functions using ChaCha20
def encrypt_messagechacha(message, encoded_key):
    nonce = os.urandom(16)  # Generate a random nonce of 16 bytes
    key = base64.b64decode(encoded_key)
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return nonce + ciphertext

def decrypt_messagechacha(ciphertext, encoded_key):
    key = base64.b64decode(encoded_key)
    nonce = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

class EncryptionScreenRC4(Screen):
    def __init__(self, **kwargs):
        super(EncryptionScreenRC4, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Encryption - RC4', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Encrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter plain text to be Encrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Encrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)

        # Encrypt button
        self.encrypt_button = Button(text='Encrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.encrypt_button.bind(on_press=self.encrypt_message)

        # Encrypted output label
        encrypted_label_title = Label(text='Encrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))

        self.encrypted_label = Label(text='', size_hint_y=None, height=40)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('RC4'))

        # Adding widgets to the main layout
        self.main_layout.add_widget(self.key_input)
        self.key_input.opacity = 0  # Start with key_input hidden

        self.main_layout.add_widget(self.encrypt_button)
        self.main_layout.add_widget(encrypted_label_title)
        self.main_layout.add_widget(self.encrypted_label)
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
        else:
            self.key_input.opacity = 0  # Hide key_input

    def encrypt_message(self, instance):
        message = self.text_input.text.encode('utf-8')
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            key = base64.b64encode(os.urandom(16)).decode('utf-8')

        encrypted_data = encrypt_messageRC4(message, base64.b64decode(key))
        self.encrypted_label.text = base64.b64encode(encrypted_data).decode('utf-8')
        Clipboard.copy(self.encrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 16
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

class DecryptionScreenRC4(Screen):
    def __init__(self, **kwargs):
        super(DecryptionScreenRC4, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Decryption - RC4', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Decrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter text to be Decrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Decrypt with a custom secret key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter key', size_hint_y=None, height=40)
        self.key_input.opacity = 0  # Start with key_input hidden
        self.main_layout.add_widget(self.key_input)

        # Decrypt button
        self.decrypt_button = Button(text='Decrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.decrypt_button.bind(on_press=self.decrypt_message)
        self.main_layout.add_widget(self.decrypt_button)

        # Decrypted output label
        decrypted_label_title = Label(text='Decrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(decrypted_label_title)

        self.decrypted_label = Label(text='', size_hint_y=None, font_size="23sp",bold=True,height=40)
        self.main_layout.add_widget(self.decrypted_label)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('RC4'))
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
            self.key_input.disabled = False  # Enable key_input
        else:
            self.key_input.opacity = 0  # Hide key_input
            self.key_input.disabled = True  # Disable key_input

    def decrypt_message(self, instance):
        ciphertext = self.text_input.text.encode('utf-8')
        ciphertext = base64.b64decode(ciphertext)
        if self.use_custom_key.active:
            key = self.key_input.text
            if not self.validate_key(key):
                self.show_error("Invalid key\nPlease enter a valid base64-encoded key.")
                return
        else:
            self.show_error("A custom key must be used for decryption.")
            return

        decrypted_data = decrypt_messageRC4(ciphertext, base64.b64decode(key))
        self.decrypted_label.text = decrypted_data.decode('utf-8')
        Clipboard.copy(self.decrypted_label.text)

    def validate_key(self, key):
        try:
            decoded_key = base64.b64decode(key)
            return len(decoded_key) == 16
        except Exception:
            return False

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

# Encryption and Decryption functions using RC4
def encrypt_messageRC4(message, key):
    cipher = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message)
    return ciphertext

def decrypt_messageRC4(ciphertext, key):
    cipher = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext)
    return plaintext

def key_to_base64(key, is_private=False):
    #Convertit une clé RSA en Base64
    if is_private:
        key_bytes = key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        key_bytes = key.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    return base64.b64encode(key_bytes).decode('utf-8')

def base64_to_private_key(b64_key):
    #Convertit une clé privée Base64 en objet clé RSA
    key_bytes = base64.b64decode(b64_key.encode('utf-8'))
    return serialization.load_der_private_key(key_bytes, password=None, backend=None)

def base64_to_public_key(b64_key):
    #Convertit une clé publique Base64 en objet clé RSA
    key_bytes = base64.b64decode(b64_key.encode('utf-8'))
    return serialization.load_der_public_key(key_bytes, backend=None)

class KeyGeneratorScreenRSA(Screen):
    def __init__(self, **kwargs):
        super(KeyGeneratorScreenRSA, self).__init__(**kwargs)
        
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        
        layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=dp(20))
        


        self.private_key_sender, self.public_key_sender = self.generate_key_pair()
        self.private_key_receiver, self.public_key_receiver = self.generate_key_pair()

        # Conversion des clés en Base64
        self.b64_private_key_sender = key_to_base64(self.private_key_sender, is_private=True)
        self.b64_public_key_sender = key_to_base64(self.public_key_sender, is_private=False)
        self.b64_private_key_receiver = key_to_base64(self.private_key_receiver, is_private=True)
        self.b64_public_key_receiver = key_to_base64(self.public_key_receiver, is_private=False)

        # ScrollView pour permettre le défilement du contenu si nécessaire
        scroll_view = ScrollView()
        inner_layout = BoxLayout(orientation='vertical', spacing=dp(25), padding=dp(10), size_hint_y=None)
        inner_layout.bind(minimum_height=inner_layout.setter('height'))

        # Affichage des clés du sender
        sender_label = Label(text="Sender keys ", font_size=24, bold=True, color=[0.2, 0.6, 0.2, 1])
        inner_layout.add_widget(sender_label)

        private_key_sender_label = Label(text="Private key ", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(private_key_sender_label)
        self.private_key_sender_input = TextInput(text=self.b64_private_key_sender, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.private_key_sender_input)

        # Espace entre les clés privées et publiques du sender
        inner_layout.add_widget(Widget(size_hint_y=None, height=dp(10)))

        public_key_sender_label = Label(text="Public key ", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(public_key_sender_label)
        self.public_key_sender_input = TextInput(text=self.b64_public_key_sender, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.public_key_sender_input)

        copy_sender_button = Button(text="Copy the sender's keys", size_hint=(0.5, None), height=dp(50), background_color=[0.2, 0.6, 0.2, 1])
        copy_sender_button.bind(on_press=self.copy_sender_keys)
        inner_layout.add_widget(copy_sender_button)

        # Affichage des clés du receiver
        receiver_label = Label(text="Receiver keys ", font_size=24, bold=True, color=[0.2, 0.6, 0.2, 1])
        inner_layout.add_widget(receiver_label)

        private_key_receiver_label = Label(text="Private key ", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(private_key_receiver_label)
        self.private_key_receiver_input = TextInput(text=self.b64_private_key_receiver, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.private_key_receiver_input)

        # Espace entre les clés privées et publiques du receiver
        inner_layout.add_widget(Widget(size_hint_y=None, height=dp(10)))

        public_key_receiver_label = Label(text="Public key ", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(public_key_receiver_label)
        self.public_key_receiver_input = TextInput(text=self.b64_public_key_receiver, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.public_key_receiver_input)

        copy_receiver_button = Button(text="Copy the receiver's keys", size_hint=(0.5, None), height=dp(50), background_color=[0.2, 0.6, 0.2, 1])
        copy_receiver_button.bind(on_press=self.copy_receiver_keys)
        inner_layout.add_widget(copy_receiver_button)

        # Bouton Back
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=self.go_back)
        inner_layout.add_widget(back_button)

        scroll_view.add_widget(inner_layout)
        layout.add_widget(scroll_view)
        self.add_widget(layout)

    def generate_key_pair(self):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    def copy_sender_keys(self, instance):
        keys = (
            f"Clé privée du sender : {self.private_key_sender_input.text}\n"
            f"Clé publique du sender : {self.public_key_sender_input.text}"
        )
        Clipboard.copy(keys)
        self.show_popup("The sender's keys have been copied to the clipboard")

    def copy_receiver_keys(self, instance):
        keys = (
            f"Clé privée du receiver : {self.private_key_receiver_input.text}\n"
            f"Clé publique du receiver : {self.public_key_receiver_input.text}"
        )
        Clipboard.copy(keys)
        self.show_popup("The receiver's keys have been copied to the clipboard")

    def go_back(self, instance):
        self.manager.current = 'RSA'

    def show_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(5))
        popup_label = Label(text=message, size_hint_y=None, height=dp(50))
        popup_button = Button(text='Close', size_hint_y=None, height=dp(50))
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title='Information', content=popup_layout, size_hint=(0.5, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos
def encryptRSA(message, public_key):
    """Chiffre un message avec la clé publique RSA"""
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decryptRSA(ciphertext, private_key):
    """Déchiffre un message avec la clé privée RSA"""
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

class EncryptionScreenRSA1(Screen):
    def __init__(self, **kwargs):
        super(EncryptionScreenRSA1, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Encryption - RSA', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Encrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter plain text to be Encrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Encrypt with a custom public key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter public key', size_hint_y=None, height=40)

        # Encrypt button
        self.encrypt_button = Button(text='Encrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.encrypt_button.bind(on_press=self.encrypt_message)

        # Encrypted output label
        encrypted_label_title = Label(text='Encrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))

        self.encrypted_label = Label(text='', size_hint_y=None, height=40)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('RSA'))

        # Adding widgets to the main layout
        self.main_layout.add_widget(self.key_input)
        self.key_input.opacity = 0  # Start with key_input hidden

        self.main_layout.add_widget(self.encrypt_button)
        self.main_layout.add_widget(encrypted_label_title)
        self.main_layout.add_widget(self.encrypted_label)
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
        else:
            self.key_input.opacity = 0  # Hide key_input

    def encrypt_message(self, instance):
        message = self.text_input.text.encode('utf-8')
        if self.use_custom_key.active:
            key = self.key_input.text
            try:
                public_key = base64_to_public_key(key)
            except Exception:
                self.show_error("Invalid public key\nPlease enter a valid base64-encoded key.")
                return
        else:
            private_key, public_key = self.generate_key_pair()
            self.show_keys(private_key, public_key)
        
        encrypted_data = encryptRSA(message, public_key)
        self.encrypted_label.text = base64.b64encode(encrypted_data).decode('utf-8')
        Clipboard.copy(self.encrypted_label.text)

    def generate_key_pair(self):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    def show_keys(self, private_key, public_key):
        b64_private_key = key_to_base64(private_key, is_private=True)
        b64_public_key = key_to_base64(public_key, is_private=False)
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        private_key_label = Label(text=f'Private Key: {b64_private_key}', font_size='14sp', size_hint_y=None, height=100)
        public_key_label = Label(text=f'Public Key: {b64_public_key}', font_size='14sp', size_hint_y=None, height=100)
        popup_content.add_widget(private_key_label)
        popup_content.add_widget(public_key_label)
        popup = Popup(title='Generated RSA Keys', content=popup_content, size_hint=(None, None), size=(400, 300))
        popup.open()

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

def encrypt_with_private_key(message, private_key):
    """Chiffre un message avec la clé privée RSA"""
    ciphertext = private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return ciphertext





class DecryptionScreenRSA1(Screen):
    def __init__(self, **kwargs):
        super(DecryptionScreenRSA1, self).__init__(**kwargs)
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Decryption - RSA', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter encrypted text to be Decrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input for encrypted text
        self.text_input = TextInput(hint_text='Enter encrypted text to be Decrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Key input for private key
        key_label = Label(text='Enter private key (Base64)', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(key_label)
        self.key_input = TextInput(hint_text='Enter private key', size_hint_y=None, height=40)
        self.main_layout.add_widget(self.key_input)

        # Decrypt button
        self.decrypt_button = Button(text='Decrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.decrypt_button.bind(on_press=self.decrypt_message)
        self.main_layout.add_widget(self.decrypt_button)

        # Decrypted output label
        decrypted_label_title = Label(text='Decrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(decrypted_label_title)
        self.decrypted_label = Label(text='', size_hint_y=None,font_size="23sp",bold=True, height=40)
        self.main_layout.add_widget(self.decrypted_label)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('RSA'))
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def decrypt_message(self, instance):
        ciphertext_b64 = self.text_input.text
        private_key_b64 = self.key_input.text
        try:
            ciphertext = base64.b64decode(ciphertext_b64)
            private_key = base64_to_private_key(private_key_b64)
            plaintext = decryptRSA(ciphertext, private_key)
            self.decrypted_label.text = plaintext.decode('utf-8')
        except Exception as e:
            self.show_error(f"Decryption failed: {str(e)}")

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos       
        



def key_to_base642(key, is_private):
    """Convertit une clé en Base64"""
    if is_private:
        key_bytes = key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        key_bytes = key.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    return base64.b64encode(key_bytes).decode('utf-8')

def base64_to_private_key2(b64_key):
    """Convertit une clé privée Base64 en objet clé RSA"""
    key_bytes = base64.b64decode(b64_key.encode('utf-8'))
    return serialization.load_der_private_key(key_bytes, password=None)

def base64_to_public_key2(b64_key):
    """Convertit une clé publique Base64 en objet clé RSA"""
    key_bytes = base64.b64decode(b64_key.encode('utf-8'))
    return serialization.load_der_public_key(key_bytes)

def encrypt_with_private_key2(message, private_key):
    """Chiffre un message avec la clé privée RSA"""
    ciphertext = private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return ciphertext

def decrypt_with_public_key2(ciphertext, public_key):
    """Déchiffre un message chiffré avec une clé privée, en utilisant la clé publique RSA"""
    try:
        plaintext = public_key.decrypt(
            ciphertext,
            padding.PKCS1v15()
        )
        return plaintext
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")





parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

def generate_private_keyDH():
    """Génère une clé privée Diffie-Hellman"""
    private_key = parameters.generate_private_key()
    return private_key

def generate_public_keyDH(private_key):
    """Génère une clé publique Diffie-Hellman"""
    public_key = private_key.public_key()
    return public_key

def generate_shared_keyDH(private_key, peer_public_key):
    """Génère une clé partagée Diffie-Hellman"""
    shared_key = private_key.exchange(peer_public_key)
    # Utiliser HKDF pour dériver une clé de 32 bytes (256 bits) pour AES
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'dh key exchange',
        backend=default_backend()
    ).derive(shared_key)
    return derived_key

def key_to_base64DH(key, is_private=False):
    """Convertit une clé en Base64"""
    if is_private:
        key_bytes = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        key_bytes = key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    return base64.b64encode(key_bytes).decode('utf-8')

class KeyGeneratorScreenDH(Screen):
    def __init__(self, **kwargs):
        super(KeyGeneratorScreenDH, self).__init__(**kwargs)
        
        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)
        
        layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=dp(20))

        self.private_key_sender, self.public_key_sender = self.generate_key_pair()
        self.private_key_receiver, self.public_key_receiver = self.generate_key_pair()

        # Generate shared keys
        self.shared_key_sender = generate_shared_keyDH(self.private_key_sender, self.public_key_receiver)
        self.shared_key_receiver = generate_shared_keyDH(self.private_key_receiver, self.public_key_sender)

        # Convert keys to Base64
        self.b64_private_key_sender = key_to_base64(self.private_key_sender, is_private=True)
        self.b64_public_key_sender = key_to_base64(self.public_key_sender, is_private=False)
        self.b64_private_key_receiver = key_to_base64(self.private_key_receiver, is_private=True)
        self.b64_public_key_receiver = key_to_base64(self.public_key_receiver, is_private=False)
        self.b64_shared_key_sender = base64.b64encode(self.shared_key_sender).decode('utf-8')
        self.b64_shared_key_receiver = base64.b64encode(self.shared_key_receiver).decode('utf-8')

        # ScrollView to allow scrolling of content if necessary
        scroll_view = ScrollView()
        inner_layout = BoxLayout(orientation='vertical', spacing=dp(25), padding=dp(10), size_hint_y=None)
        inner_layout.bind(minimum_height=inner_layout.setter('height'))

        # Display sender keys
        sender_label = Label(text="Sender keys", font_size=24, bold=True, color=[0.2, 0.6, 0.2, 1])
        inner_layout.add_widget(sender_label)

        private_key_sender_label = Label(text="Private key", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(private_key_sender_label)
        self.private_key_sender_input = TextInput(text=self.b64_private_key_sender, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.private_key_sender_input)

        public_key_sender_label = Label(text="Public key", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(public_key_sender_label)
        self.public_key_sender_input = TextInput(text=self.b64_public_key_sender, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.public_key_sender_input)

        shared_key_sender_label = Label(text="Shared key", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(shared_key_sender_label)
        self.shared_key_sender_input = TextInput(text=self.b64_shared_key_sender, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.shared_key_sender_input)

        copy_sender_button = Button(text="Copy the sender's keys.", size_hint=(0.5, None), height=dp(50), background_color=[0.2, 0.6, 0.2, 1])
        copy_sender_button.bind(on_press=self.copy_sender_keys)
        inner_layout.add_widget(copy_sender_button)

        # Display receiver keys
        receiver_label = Label(text="Receiver keys", font_size=24, bold=True, color=[0.2, 0.6, 0.2, 1])
        inner_layout.add_widget(receiver_label)

        private_key_receiver_label = Label(text="Private key", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(private_key_receiver_label)
        self.private_key_receiver_input = TextInput(text=self.b64_private_key_receiver, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.private_key_receiver_input)

        public_key_receiver_label = Label(text="Public key", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(public_key_receiver_label)
        self.public_key_receiver_input = TextInput(text=self.b64_public_key_receiver, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.public_key_receiver_input)

        shared_key_receiver_label = Label(text="Shared key", font_size=18, bold=True, color=[0.2, 0.2, 0.2, 1])
        inner_layout.add_widget(shared_key_receiver_label)
        self.shared_key_receiver_input = TextInput(text=self.b64_shared_key_receiver, readonly=True, size_hint_y=None, height=dp(100), background_color=[0.9, 0.9, 0.9, 1], foreground_color=[0, 0, 0, 1])
        inner_layout.add_widget(self.shared_key_receiver_input)

        copy_receiver_button = Button(text="Copy the receiver's keys", size_hint=(0.5, None), height=dp(50), background_color=[0.2, 0.6, 0.2, 1])
        copy_receiver_button.bind(on_press=self.copy_receiver_keys)
        inner_layout.add_widget(copy_receiver_button)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=self.go_back)
        inner_layout.add_widget(back_button)

        scroll_view.add_widget(inner_layout)
        layout.add_widget(scroll_view)
        self.add_widget(layout)

    def generate_key_pair(self):
        private_key = generate_private_keyDH()
        public_key = generate_public_keyDH(private_key)
        return private_key, public_key

    def copy_sender_keys(self, instance):
        keys = (
            f"Clé privée du sender : {self.private_key_sender_input.text}\n"
            f"Clé publique du sender : {self.public_key_sender_input.text}\n"
            f"Clé partagée du sender : {self.shared_key_sender_input.text}"
        )
        Clipboard.copy(keys)
        self.show_popup("The sender's keys have been copied to the clipboard")

    def copy_receiver_keys(self, instance):
        keys = (
            f"Clé privée du receiver : {self.private_key_receiver_input.text}\n"
            f"Clé publique du receiver : {self.public_key_receiver_input.text}\n"
            f"Clé partagée du receiver : {self.shared_key_receiver_input.text}"
        )
        Clipboard.copy(keys)
        self.show_popup("The receiver's keys have been copied to the clipboard")

    def go_back(self, instance):
        self.manager.current = 'DH'

    def show_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(5))
        popup_label = Label(text=message, size_hint_y=None, height=dp(50))
        popup_button = Button(text='Close', size_hint_y=None, height=dp(50))
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title='Information', content=popup_layout, size_hint=(0.5, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos




class EncryptionScreenDH(Screen):
    def __init__(self, **kwargs):
        super(EncryptionScreenDH, self).__init__(**kwargs)

        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Encryption - DH', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Encrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter plain text to be Encrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)

        # Checkbox and key input
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.use_custom_key = CheckBox(size_hint=(None, None), size=(40, 40), color=(0, 0, 0, 1))
        self.use_custom_key.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(self.use_custom_key)

        checkbox_label = Label(text='Encrypt with a custom shared key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        checkbox_layout.add_widget(checkbox_label)

        self.main_layout.add_widget(checkbox_layout)

        self.key_input = TextInput(hint_text='Enter shared key', size_hint_y=None, height=40)

        # Encrypt button
        self.encrypt_button = Button(text='Encrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.encrypt_button.bind(on_press=self.encrypt_message)

        # Encrypted output label
        encrypted_label_title = Label(text='Encrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))

        self.encrypted_label = Label(text='', size_hint_y=None, height=40)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('DH'))

        # Adding widgets to the main layout
        self.main_layout.add_widget(self.key_input)
        self.key_input.opacity = 0  # Start with key_input hidden

        self.main_layout.add_widget(self.encrypt_button)
        self.main_layout.add_widget(encrypted_label_title)
        self.main_layout.add_widget(self.encrypted_label)
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

        # Generate DH parameters and initial key pair
        self.private_key, self.public_key = self.generate_dh_key_pair()

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.key_input.opacity = 1  # Show key_input
        else:
            self.key_input.opacity = 0  # Hide key_input

    def generate_dh_key_pair(self):
        private_key = generate_private_keyDH()
        public_key = generate_public_keyDH(private_key)
        return private_key, public_key

    def encrypt_message(self, instance):
        message = self.text_input.text.encode('utf-8')
        
        if self.use_custom_key.active:
            try:
                shared_key_b64 = self.key_input.text
                self.shared_key = base64.b64decode(shared_key_b64)
                if len(self.shared_key) != 32:
                    raise ValueError("Invalid shared key length")
            except Exception as e:
                self.show_error(f"Invalid shared key\nPlease enter a valid Base64-encoded key. Error: {str(e)}")
                return
        else:
            peer_private_key, peer_public_key = self.generate_dh_key_pair()
            self.shared_key = generate_shared_keyDH(self.private_key, peer_public_key)
            self.show_keys(self.private_key, self.public_key)

        encrypted_data = self.encrypt(message, self.shared_key)
        self.encrypted_label.text = base64.b64encode(encrypted_data).decode('utf-8')
        Clipboard.copy(self.encrypted_label.text)

    def encrypt(self, message, key):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message) + encryptor.finalize()
        return iv + ciphertext

    def show_keys(self, private_key, public_key):
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        b64_private_key = base64.b64encode(private_key_pem).decode('utf-8')
        b64_public_key = base64.b64encode(public_key_pem).decode('utf-8')
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        private_key_label = Label(text=f'Private Key: {b64_private_key}', font_size='14sp', size_hint_y=None, height=100)
        public_key_label = Label(text=f'Public Key: {b64_public_key}', font_size='14sp', size_hint_y=None, height=100)
        popup_content.add_widget(private_key_label)
        popup_content.add_widget(public_key_label)
        popup = Popup(title='Generated DH Keys', content=popup_content, size_hint=(None, None), size=(400, 300))
        popup.open()

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos

class DecryptionScreenDH(Screen):
    def __init__(self, **kwargs):
        super(DecryptionScreenDH, self).__init__(**kwargs)

        with self.canvas.before:
            Color(114/255, 222/255, 138/255, 1)  # Background color: #72DE8A
            self.rect4 = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect4, pos=self._update_rect4)

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title_label = Label(text='Text Decryption - DH', font_size='24sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(title_label)

        # Instructions
        instructions_label = Label(text='Enter any text to be Decrypted', font_size='18sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(instructions_label)

        # Text input
        self.text_input = TextInput(hint_text='Enter encrypted text to be Decrypted', size_hint_y=None, height=100)
        self.main_layout.add_widget(self.text_input)
        
        checkbox_label = Label(text='Decrypt with a custom shared key', font_size='16sp', color=(49/255, 167/255, 75/255, 1))
        self.main_layout.add_widget(checkbox_label)
        # Key input
        self.key_input = TextInput(hint_text='Enter shared key', size_hint_y=None, height=40)
        self.main_layout.add_widget(self.key_input)

        # Decrypt button
        self.decrypt_button = Button(text='Decrypt', size_hint=(None, None), size=(200, 50), background_color=(49/255, 167/255, 75/255, 1))
        self.decrypt_button.bind(on_press=self.decrypt_message)

        # Decrypted output label
        decrypted_label_title = Label(text='Decrypted Output:', font_size='18sp', color=(49/255, 167/255, 75/255, 1))

        self.decrypted_label = Label(text='', size_hint_y=None, font_size="23sp",bold=True,height=40)

        # Back button
        back_button = Button(text='Back', size_hint=(None, None), size=(100, 25), background_color=(49/255, 167/255, 75/255, 1))
        back_button.bind(on_press=lambda x: self.change_screen('DH'))

        # Adding widgets to the main layout
        self.main_layout.add_widget(self.decrypt_button)
        self.main_layout.add_widget(decrypted_label_title)
        self.main_layout.add_widget(self.decrypted_label)
        self.main_layout.add_widget(back_button)

        self.add_widget(self.main_layout)

    def decrypt_message(self, instance):
        encrypted_message = base64.b64decode(self.text_input.text.encode('utf-8'))
        try:
            shared_key_b64 = self.key_input.text
            shared_key = base64.b64decode(shared_key_b64)
            if len(shared_key) != 32:
                raise ValueError("Invalid shared key length")
        except Exception as e:
            self.show_error(f"Invalid shared key\nPlease enter a valid Base64-encoded key. Error: {str(e)}")
            return

        try:
            decrypted_data = self.decrypt(encrypted_message, shared_key)
            self.decrypted_label.text = decrypted_data.decode('utf-8')
            Clipboard.copy(self.decrypted_label.text)
        except Exception as e:
            self.show_error(f"Decryption failed. Error: {str(e)}")

    def decrypt(self, encrypted_message, key):
        iv = encrypted_message[:16]
        ciphertext = encrypted_message[16:]
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def change_screen(self, screen_name):
        self.manager.current = screen_name

    def _update_rect4(self, instance, value):
        self.rect4.size = instance.size
        self.rect4.pos = instance.pos
        
        
        

if __name__ == '__main__':
    CryptoApp().run()








