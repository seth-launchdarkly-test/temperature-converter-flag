import os
import tkinter as tk
import ldclient
from ldclient import Context
from ldclient.config import Config
from threading import Lock, Event

# Set sdk_key to your LaunchDarkly SDK key.
sdk_key = os.getenv("LAUNCHDARKLY_SDK_KEY")

# Set feature_flag_key to the feature flag key you want to evaluate.
feature_flag_key = "temperature-converter"

def show_evaluation_result(key: str, value: bool):
    print(f"*** The {key} feature flag evaluates to {value}")

def show_banner():
    print("██ LAUNCHDARKLY █")

class FlagValueChangeListener:
    def __init__(self, result_label):
        self.__show_banner = True
        self.__lock = Lock()
        self.result_label = result_label

    def flag_value_change_listener(self, flag_change):
        with self.__lock:
            # Show the banner in the console when the flag is enabled
            if self.__show_banner and flag_change.new_value:
                show_banner()
                self.__show_banner = False
            show_evaluation_result(flag_change.key, flag_change.new_value)
            self.update_color_change_feature(flag_change.new_value)

    def update_color_change_feature(self, is_enabled):
        # Check if the temperature should change colors or stay black
        try:
            fahrenheit = float(entry.get())
            color = "blue" if fahrenheit <= 32 else "red" if is_enabled else "black"
            result_label.config(foreground=color)
        except ValueError:
            result_label.config(text="Please enter a valid number", fg="black")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        result_text = f"{fahrenheit}°F is {celsius:.2f}°C"
        result_label.config(text=result_text)

        # Check the flag and update the color based on the temperature
        color_change_enabled = ld_client.variation(feature_flag_key, context, False)
        listener.update_color_change_feature(color_change_enabled)
    except ValueError:
        result_label.config(text="Please enter a valid number", fg="black")

# Initialize LaunchDarkly
if not sdk_key:
    print("*** Please set the LAUNCHDARKLY_SDK_KEY env first")
    exit()

ldclient.set_config(Config(sdk_key))
ld_client = ldclient.get()
context = Context.builder('example-user-key').kind('user').name('Sandy').build()

if not ld_client.is_initialized():
    print("*** SDK failed to initialize. Check your SDK key and network connection.")
    exit()

print("*** SDK successfully initialized")

# Set up Tkinter app
app = tk.Tk()
app.title("Fahrenheit to Celsius Converter")

# UI setup
tk.Label(app, text="Enter Fahrenheit:").pack()
entry = tk.Entry(app)
entry.pack()
result_label = tk.Label(app, text="")
result_label.pack()

# Initialize FlagValueChangeListener
listener = FlagValueChangeListener(result_label)
ld_client.flag_tracker.add_flag_value_change_listener(
    feature_flag_key, context, listener.flag_value_change_listener
)

# Button to perform conversion
convert_button = tk.Button(app, text="Convert", command=fahrenheit_to_celsius)
convert_button.pack()

# Run the application
app.mainloop()

# Ensure clean shutdown
ld_client.close()
