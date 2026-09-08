"""Hardware test: read battery voltage every 5 minutes and log to a file.

Each reading is appended as ``timestamp,voltage`` to ``battery_log.txt``
in the same directory as this script. Run with:

    python -m pidog_app.test_hardware

Stop with Ctrl+C.
"""
import time
from datetime import datetime
from pathlib import Path

from robot_hat import get_battery_voltage

LOG_PATH = Path(__file__).resolve().parent.parent / "battery.log"
INTERVAL_SEC = 300  # 5 minutes


def read_battery_voltage():
    """Read the battery pack voltage in volts."""
    return get_battery_voltage()


def log_battery_voltage(log_path: Path = LOG_PATH):
    """Read the battery voltage once and append ``timestamp,voltage`` to the log file."""
    voltage = read_battery_voltage()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp},{voltage:.2f}\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line)
    print(f"{timestamp}  Battery Voltage: {voltage:.2f}V  -> {log_path}")


def test_battery_voltage(interval_sec: float = INTERVAL_SEC,
                         log_path: Path = LOG_PATH):
    """Read the battery voltage every ``interval_sec`` seconds and log it.

    Takes one reading immediately, then waits ``interval_sec`` between
    subsequent readings. Runs until interrupted with Ctrl+C.
    """
    print(f"Logging battery voltage to {log_path} every {interval_sec}s "
          f"(Ctrl+C to stop)")
    try:
        while True:
            log_battery_voltage(log_path)
            time.sleep(interval_sec)
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    test_battery_voltage()
