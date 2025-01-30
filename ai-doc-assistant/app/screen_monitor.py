import pygetwindow as gw
import pyautogui
import time
from datetime import datetime

class ScreenMonitor:
    def __init__(self):
        self.activities = []

    def capture_activity(self):
        # Get the currently active window
        active_window = gw.getActiveWindow()

        if active_window:
            window_title = active_window.title
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Capture a screenshot of the active window (optional)
            screenshot_path = f"screenshots/{timestamp}.png"
            pyautogui.screenshot(screenshot_path)

            activity = {
                'window_title': window_title,
                'timestamp': timestamp,
                'screenshot': screenshot_path
            }

            self.activities.append(activity)
            print(f"Captured activity: {window_title} at {timestamp}")

    def get_activity(self):
        return self.activities