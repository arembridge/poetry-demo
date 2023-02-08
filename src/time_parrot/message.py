from datetime import datetime


def time():
    now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    return f"Hello! The time is {now}"
