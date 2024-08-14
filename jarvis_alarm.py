from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import requests
import datetime

class AlarmApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Set Alarm Time (HH:MM):")
        self.layout.add_widget(self.label)

        self.time_input = TextInput(hint_text="Enter time", multiline=False)
        self.layout.add_widget(self.time_input)

        self.set_button = Button(text="Set Alarm")
        self.set_button.bind(on_press=self.set_alarm)
        self.layout.add_widget(self.set_button)

        self.weather_label = Label(text="Fetching weather...")
        self.layout.add_widget(self.weather_label)

        self.alarm_time = None
        self.sound = SoundLoader.load('jarvis_alarm.mp3')

        # Fetch weather data at startup
        self.fetch_weather()

        return self.layout

    def set_alarm(self, instance):
        self.alarm_time = self.time_input.text
        self.label.text = f"Alarm set for {self.alarm_time}"

    def fetch_weather(self):
        api_key = "YOUR_API_KEY"
        city = "YOUR_CITY"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            self.weather_label.text = f"Weather: {weather_description}, Temp: {temperature}°C"
        else:
            self.weather_label.text = "Failed to fetch weather data"

    def check_alarm(self, dt):
        current_time = datetime.datetime.now().strftime("%H:%M")
        if self.alarm_time == current_time:
            self.sound.play()
            self.label.text = "Good morning, sir. It's time to wake up."

    def on_start(self):
        Clock.schedule_interval(self.check_alarm, 60)

if __name__ == '__main__':
    AlarmApp().run()

'''
Krok 4: Przygotowanie dźwięku
Ściągnij dźwięk alarmu Jarvisa (np. jarvis_alarm.mp3) i umieść go w tym samym folderze co plik main.py.

Krok 5: Zdobądź klucz API dla OpenWeatherMap
Zarejestruj się na OpenWeatherMap i zdobądź klucz API. Zastąp "YOUR_API_KEY" swoim kluczem, a "YOUR_CITY" nazwą swojego miasta.

2. Proces aplikowania aplikacji na telefon
Android
Użyj narzędzia Buildozer: Buildozer to narzędzie do pakowania aplikacji Kivy na Androida.
Instalacja Buildozer:
bash
Skopiuj kod
pip install buildozer
Inicjalizacja projektu:
bash
Skopiuj kod
buildozer init
Konfiguracja pliku buildozer.spec: Otwórz plik buildozer.spec i skonfiguruj go według potrzeb.
Budowanie APK:
bash
Skopiuj kod
buildozer -v android debug
Znajdź plik APK w folderze bin i przenieś go na telefon, aby zainstalować.
iOS
Użyj narzędzia Kivy-ios: Proces tworzenia aplikacji na iOS jest bardziej skomplikowany i wymaga Maca oraz Xcode.
Instalacja Kivy-ios:
bash
Skopiuj kod
pip install kivy-ios
Skonfiguruj projekt Kivy-ios i utwórz plik Xcode.
Otwórz projekt w Xcode i skompiluj aplikację.
Podsumowanie
Stworzyliśmy prostą aplikację budzika z wykorzystaniem Kivy, która pobiera dane o pogodzie i używa dźwięku alarmu Jarvisa.
Aby wdrożyć aplikację na telefon, użyjemy Buildozera dla Androida i Kivy-ios dla iOS. Proces może wymagać dodatkowej konfiguracji,
zwłaszcza dla iOS, ale jest to ogólny zarys kroków potrzebnych do osiągnięcia celu.
'''