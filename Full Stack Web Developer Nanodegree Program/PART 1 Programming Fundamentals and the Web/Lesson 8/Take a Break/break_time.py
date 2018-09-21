import time
import webbrowser

break_counter = 3
i = 0

while i < break_counter:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=niMxkET9zTE")
    i += 1
