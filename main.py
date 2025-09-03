from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import battery, notification
from kivy.core.audio import SoundLoader
import pyttsx3

FULL_CHARGE = 95


class BatteryApp(App):
    def build(self):
        self.label = Label(text="Checking battery...")
        Clock.schedule_interval(self.check_battery, 5)  # every 5 seconds for testing
        return self.label

    def play_sound(self,file_path):
        sound = SoundLoader.load(file_path)
        if sound:
            sound.play()

    def check_battery(self, dt):
        status = battery.status
        if status is not None:
            percent = status.get('percentage', 0)
            charging = status.get('isCharging', False)
            self.label.text = f"Battery: {percent}% | Charging: {charging}"

            if charging and percent >= FULL_CHARGE:
                notification.notify(
                    title="Battery Full",
                    message="Unplug the charger to save battery health.",
                    timeout=5
                )
                self.play_sound("alarm.mp3")
        else:
            self.label.text = "Battery info not available."


if __name__ == "__main__":
    BatteryApp().run()
