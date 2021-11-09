# importing the module
import cv2 as cv
import json
from pathlib import Path
# from draw import drawImage


# function to display the coordinates of
# of the points clicked on the image
def click_listener(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        # print(f"x: {x}, y: {y}")

        params['ic'].addMark(x, y)
        params['ic'].showImage()

    # # checking for right mouse clicks
    # if event == cv.EVENT_RBUTTONDOWN:
    #     None


def reset_listener(*args):
    # print("Reset marks")
    params = args[1]
    params["ic"].resetMarks()


def hide_marks_listener(checked, params):
    if checked:
        params["ic"].showImage(hide_marks=True)
    else:
        params["ic"].showImage(hide_marks=False)


def open_file_listener(*args):
    None


def save_marks_listener(event, params):
    data = params['ic'].poi_list
    output_base_dir = Path(params['ic'].mark_config['output_path'])
    img_path = Path(params['ic'].img_path)

    base_dir = output_base_dir if output_base_dir else img_path.parent
    output_file = base_dir / (img_path.stem + '_marks.txt')

    # Create parent directories if needed
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(data, f)

    print(F"Saved PoI: {data}")
