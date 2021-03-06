# Text to speech
from plyer import battery, tts, vibrator

import os
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from kivy.core.text import LabelBase

from kivy.core.audio import SoundLoader


LabelBase.register(name='NotoSans', fn_regular='NotoSans.otf')

# Size Dimensions based on Samsung Galaxy Note 5
Window.size = (640, 360)
Window.clearcolor = (1, 1, 1, 1)

# Tracks the screen (English/Cantonese) and also the menu (Liquid/Food/Toilet/Bed)
location = 'English_Main'

# Message Function for English Text to Speech
speak_command_message = ''

# Message Function for Cantonese Audio Files
cantonese_message_name = ''

class English_Window(Screen):
    def change_menu(self, menu):
        global location
        location = menu
        if location == 'English_Main':
            self.ids.Thumb_label.text = 'Liquid'
            self.ids.Index_label.text = 'Toilet'
            self.ids.Middle_label.text = 'Food'
            self.ids.Pinky_label.text = 'Bed'
        elif location == 'English_Liquid':
            self.ids.Thumb_label.text = 'Exit'
            self.ids.Index_label.text = 'Water'
            self.ids.Middle_label.text = 'Juice'
            self.ids.Pinky_label.text = 'Milk'
        elif location == 'English_Toilet':
            self.ids.Thumb_label.text = 'Exit'
            self.ids.Index_label.text = 'Urinate'
            self.ids.Middle_label.text = 'Poop'
            self.ids.Pinky_label.text = 'Help'
        elif location == 'English_Food':
            self.ids.Thumb_label.text = 'Exit'
            self.ids.Index_label.text = 'Rice'
            self.ids.Middle_label.text = 'Pork'
            self.ids.Pinky_label.text = 'Chicken'
        elif location == 'English_Bed':
            self.ids.Thumb_label.text = 'Exit'
            self.ids.Index_label.text = 'Down'
            self.ids.Middle_label.text = 'Up'
            self.ids.Pinky_label.text = 'Help'
        else:
            pass

    def button_press(self, button):
        def change_speak_message(message):
            global speak_command_message
            speak_command_message = message

        def speak_message(message='speak_command'):
            if message == 'speak_command':
                global speak_command_message
                tts.speak(speak_command_message)
            else:
                tts.speak(message)

        def change_menu(menu):
            global location
            location = menu
            if location == 'English_Main':
                self.ids.Thumb_label.text = 'Liquid'
                self.ids.Index_label.text = 'Toilet'
                self.ids.Middle_label.text = 'Food'
                self.ids.Pinky_label.text = 'Bed'
            elif location == 'English_Liquid':
                self.ids.Thumb_label.text = 'Exit'
                self.ids.Index_label.text = 'Water'
                self.ids.Middle_label.text = 'Juice'
                self.ids.Pinky_label.text = 'Milk'
            elif location == 'English_Toilet':
                self.ids.Thumb_label.text = 'Exit'
                self.ids.Index_label.text = 'Urinate'
                self.ids.Middle_label.text = 'Poop'
                self.ids.Pinky_label.text = 'Help'
            elif location == 'English_Food':
                self.ids.Thumb_label.text = 'Exit'
                self.ids.Index_label.text = 'Rice'
                self.ids.Middle_label.text = 'Pork'
                self.ids.Pinky_label.text = 'Chicken'
            elif location == 'English_Bed':
                self.ids.Thumb_label.text = 'Exit'
                self.ids.Index_label.text = 'Down'
                self.ids.Middle_label.text = 'Up'
                self.ids.Pinky_label.text = 'Help'
            else:
                pass

        global location
        if button == 'Thumb':
            if location == 'English_Main':
                change_menu('English_Liquid')
                speak_message('Liquid selected')
            elif location == 'English_Liquid':
                change_menu('English_Main')
                speak_message('Exited liquid menu')
                change_speak_message('')
            elif location == 'English_Toilet':
                change_menu('English_Main')
                speak_message('Exited toilet menu')
                change_speak_message('')
            elif location == 'English_Food':
                change_menu('English_Main')
                speak_message('Exited food menu')
                change_speak_message('')
            elif location == 'English_Bed':
                change_menu('English_Main')
                speak_message('Exited bed menu')
                change_speak_message('')
            else:
                pass

        elif button == 'Index':
            if location == 'English_Main':
                change_menu('English_Toilet')
                speak_message('Toilet selected')
            elif location == 'English_Liquid':
                speak_message('Water')
                change_speak_message('Please give me some water')
            elif location == 'English_Toilet':
                speak_message('Urinate')
                change_speak_message('I need to go urinate')
            elif location == 'English_Food':
                speak_message('Rice')
                change_speak_message('Please give me some rice')
            elif location == 'English_Bed':
                speak_message('Down')
                change_speak_message('Please move my bed down')
            else:
                pass

        elif button == 'Middle':
            if location == 'English_Main':
                change_menu('English_Food')
                speak_message('Food selected')
            elif location == 'English_Liquid':
                speak_message('Juice')
                change_speak_message('Please give me some juice')
            elif location == 'English_Toilet':
                speak_message('Poop')
                change_speak_message('I need to go poop')
            elif location == 'English_Food':
                speak_message('Pork')
                change_speak_message('Please give me some pork')
            elif location == 'English_Bed':
                speak_message('Up')
                change_speak_message('Please move my bed up')
            else:
                pass

        elif button == 'Pinky':
            if location == 'English_Main':
                change_menu('English_Bed')
                speak_message('Bed selected')
            elif location == 'English_Liquid':
                speak_message('Milk')
                change_speak_message('Please give me some milk')
            elif location == 'English_Toilet':
                speak_message('Help')
                change_speak_message('Please help me go to the bathroom')
            elif location == 'English_Food':
                speak_message('Chicken')
                change_speak_message('Please give me some chicken')
            elif location == 'English_Bed':
                speak_message('Help')
                change_speak_message('I need help with my bed')
            else:
                pass

        elif button == 'Speak_Command':
            speak_message()
            change_speak_message('')

        elif button == 'Cantonese':
            change_speak_message('')
            location = 'Cantonese'+location.replace('English','')
            screen_two = self.manager.get_screen('Cantonese_Window')
            screen_two.change_menu(location)

class Cantonese_Window(Screen):
    def change_menu(self, menu):
        global location
        location = menu
        if location == 'Cantonese_Main':
            self.ids.Cantonese_Thumb_label.text = '??????'
            self.ids.Cantonese_Index_label.text = '??????'
            self.ids.Cantonese_Middle_label.text = '??????'
            self.ids.Cantonese_Pinky_label.text = '??????'
        elif location == 'Cantonese_Liquid':
            self.ids.Cantonese_Thumb_label.text = '??????'
            self.ids.Cantonese_Index_label.text = '???'
            self.ids.Cantonese_Middle_label.text = '??????'
            self.ids.Cantonese_Pinky_label.text = '??????'
        elif location == 'Cantonese_Toilet':
            self.ids.Cantonese_Thumb_label.text = '????????????'
            self.ids.Cantonese_Index_label.text = '???o??????'
            self.ids.Cantonese_Middle_label.text = '???o??????'
            self.ids.Cantonese_Pinky_label.text = '??????'
        elif location == 'Cantonese_Food':
            self.ids.Cantonese_Thumb_label.text = '????????????'
            self.ids.Cantonese_Index_label.text = '??????'
            self.ids.Cantonese_Middle_label.text = '??????'
            self.ids.Cantonese_Pinky_label.text = '??????'
        elif location == 'Cantonese_Bed':
            self.ids.Cantonese_Thumb_label.text = '????????????'
            self.ids.Cantonese_Index_label.text = '????????????'
            self.ids.Cantonese_Middle_label.text = '????????????'
            self.ids.Cantonese_Pinky_label.text = '??????'
        else:
            pass

    def button_press(self, button):
        def change_cantonese_message_name(file_name):
            global cantonese_message_name
            cantonese_message_name = file_name

        def speak_message(message='speak_command'):
            global cantonese_message_name
            if message == 'speak_command' and cantonese_message_name == '':
                pass
            elif message == 'speak_command':
                self.sound = SoundLoader.load(os.path.join('cantonese_audio',cantonese_message_name))
                self.sound.play()
                cantonese_message_name = ''
            else:
                self.sound = SoundLoader.load(os.path.join('cantonese_audio',message))
                self.sound.play()

        def change_menu(menu):
            global location
            location = menu
            if location == 'Cantonese_Main':
                self.ids.Cantonese_Thumb_label.text = '??????'
                self.ids.Cantonese_Index_label.text = '??????'
                self.ids.Cantonese_Middle_label.text = '??????'
                self.ids.Cantonese_Pinky_label.text = '??????'
            elif location == 'Cantonese_Liquid':
                self.ids.Cantonese_Thumb_label.text = '??????'
                self.ids.Cantonese_Index_label.text = '???'
                self.ids.Cantonese_Middle_label.text = '??????'
                self.ids.Cantonese_Pinky_label.text = '??????'
            elif location == 'Cantonese_Toilet':
                self.ids.Cantonese_Thumb_label.text = '????????????'
                self.ids.Cantonese_Index_label.text = '???o??????'
                self.ids.Cantonese_Middle_label.text = '???o??????'
                self.ids.Cantonese_Pinky_label.text = '??????'
            elif location == 'Cantonese_Food':
                self.ids.Cantonese_Thumb_label.text = '????????????'
                self.ids.Cantonese_Index_label.text = '??????'
                self.ids.Cantonese_Middle_label.text = '??????'
                self.ids.Cantonese_Pinky_label.text = '??????'
            elif location == 'Cantonese_Bed':
                self.ids.Cantonese_Thumb_label.text = '????????????'
                self.ids.Cantonese_Index_label.text = '????????????'
                self.ids.Cantonese_Middle_label.text = '????????????'
                self.ids.Cantonese_Pinky_label.text = '??????'
            else:
                pass

        global location
        if button == '??????':
            if location == 'Cantonese_Main':
                change_menu('Cantonese_Liquid')
                speak_message('??????????????????.mp3')
            elif location == 'Cantonese_Liquid':
                change_menu('Cantonese_Main')
                change_cantonese_message_name('')
                speak_message('????????????.mp3')
            elif location == 'Cantonese_Toilet':
                change_menu('Cantonese_Main')
                change_cantonese_message_name('')
                speak_message('????????????.mp3')
            elif location == 'Cantonese_Food':
                change_menu('Cantonese_Main')
                change_cantonese_message_name('')
                speak_message('????????????.mp3')
            elif location == 'Cantonese_Bed':
                change_menu('Cantonese_Main')
                change_cantonese_message_name('')
                speak_message('????????????.mp3')
            else:
                pass

        if button == '??????':
            if location == 'Cantonese_Main':
                change_menu('Cantonese_Toilet')
                speak_message('????????????????????????.mp3')
            elif location == 'Cantonese_Liquid':
                change_cantonese_message_name('????????????.mp3')
                speak_message('??????????????????.mp3')
            elif location == 'Cantonese_Toilet':
                change_cantonese_message_name('????????????o??????.mp3')
                speak_message('???????????????o????????????.mp3')
            elif location == 'Cantonese_Food':
                change_cantonese_message_name('???????????????.mp3')
                speak_message('??????????????????.mp3')
            elif location == 'Cantonese_Bed':
                change_cantonese_message_name('?????????????????????.mp3')
                speak_message('???????????????????????????.mp3')
            else:
                pass

        if button == '??????':
            if location == 'Cantonese_Main':
                change_menu('Cantonese_Food')
                speak_message('????????????????????????.mp3')
            elif location == 'Cantonese_Liquid':
                change_cantonese_message_name('???????????????.mp3')
                speak_message('?????????????????????.mp3')
            elif location == 'Cantonese_Toilet':
                change_cantonese_message_name('????????????o??????.mp3')
                speak_message('???????????????o????????????.mp3')
            elif location == 'Cantonese_Food':
                change_cantonese_message_name('???????????????.mp3')
                speak_message('??????????????????.mp3')
            elif location == 'Cantonese_Bed':
                change_cantonese_message_name('?????????????????????.mp3')
                speak_message('???????????????????????????.mp3')
            else:
                pass

        if button == '??????':
            if location == 'Cantonese_Main':
                change_menu('Cantonese_Bed')
                speak_message('????????????????????????.mp3')
            elif location == 'Cantonese_Liquid':
                change_cantonese_message_name('?????????????????????.mp3')
                speak_message('???????????????.mp3')
            elif location == 'Cantonese_Toilet':
                change_cantonese_message_name('?????????????????????.mp3')
                speak_message('???????????????.mp3')
            elif location == 'Cantonese_Food':
                change_cantonese_message_name('?????????????????????.mp3')
                speak_message('???????????????.mp3')
            elif location == 'Cantonese_Bed':
                change_cantonese_message_name('?????????????????????.mp3')
                speak_message('???????????????.mp3')
            else:
                pass

        elif button == 'English':
            location = 'English'+location.replace('Cantonese','')
            screen_one = self.manager.get_screen('English_Window')
            screen_one.change_menu(location)

        if button == 'Speak_Command':
            speak_message()
            change_cantonese_message_name('')

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("Tap_Speech.kv")

class Tap_SpeechApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    Tap_SpeechApp().run()
