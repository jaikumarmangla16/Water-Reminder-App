
# Water Reminder App

A simple Python script to remind you to drink water at regular intervals using desktop notifications.

## Features
- Displays a console message reminding you to drink water.
- Sends a desktop notification with a custom title and message.
- Runs indefinitely, reminding every specified interval (default: 10 seconds).

## Requirements
- Python 3.x
- `plyer` library for notifications

## Installation

1. Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required `plyer` library using pip:

```bash
pip install plyer
```

## Usage

1. Save the script to a file, e.g., `water_reminder.py`.
2. Run the script using Python:

```bash
python water_reminder.py
```

3. You will receive a notification every 10 seconds reminding you to drink water. You can adjust the `time.sleep(10)` interval in the script as per your preference.

## Notes

- This script uses the `plyer` library which supports notifications on multiple platforms including Windows, macOS, and Linux.
- The notification timeout is set to 1 second, but this may vary depending on the operating system's notification system.

## License

This project is licensed under the MIT License.
