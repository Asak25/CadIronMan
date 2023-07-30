import pyautogui
import time

# Define your scale and offsets here
scale_factor = 1.25
x_offset = 800
y_offset = 600
time.sleep(3)

def start_polyline():
    command_line_position = (500, 500) # Replace with the position of your AutoCAD's command line
    pyautogui.click(command_line_position)
    time.sleep(0.1)
    pyautogui.write('pline')
    time.sleep(0.1)
    pyautogui.press('enter')

def draw_polygon(points):
    for point in points:
        # Scale the points and add offset
        x = point[0]*scale_factor + x_offset
        # Invert the y-coordinate
        y = -point[1]*scale_factor + y_offset
        pyautogui.moveTo(x, y, duration=0.25)  # Moves the mouse to the specified location over a period of 0.25 seconds.
        pyautogui.click(x, y)
        time.sleep(0.1)

# At the end of your drawing:
def end_drawing():
    command_line_position = (100, 200)  # Replace with the position of your AutoCAD's command line
    pyautogui.click(command_line_position)
    time.sleep(0.1)
    pyautogui.write('c')  # 'c' command to close the polyline
    time.sleep(0.1)
    pyautogui.press('enter')

# Define the coordinates of the Iron Man face parts
piece1=[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
piece2=[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],[(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
piece3=[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],[(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]

# Draw the Iron Man face
for piece in [piece1, piece2, piece3]:
    start_polyline()
    for subpiece in piece:
        draw_polygon(subpiece)
    end_drawing()

def hatch_polygon():
    time.sleep(0.5)
    pyautogui.write('hatch')
    pyautogui.press('enter')
    pyautogui.write('all')
    pyautogui.press('enter')
    pyautogui.press('enter')

hatch_polygon()