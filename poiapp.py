import numpy as np
import cv2 as cv
import argparse
import tempfile
from eventListener import click_listener, reset_listener, hide_marks_listener, save_marks_listener
from context import ImageContext, WindowContext

# driver function
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Mark points of interest in a image.')
    parser.add_argument('img_path',
                        help='Image path')
    parser.add_argument('output_path', default=tempfile.gettempdir(),
                        help='Path to save marks information')
    args = parser.parse_args()
    # Image path
    img_path = args.img_path
    output_path = args.output_path

    # # Window name
    root_window = "PoI"

    wc = WindowContext(root_window)
    ic = ImageContext(img_path, root_window, output_path)

    # # Read image
    img = cv.imread(img_path, 1)
    #
    # displaying the initial image
    cv.imshow(root_window, img)

    params = {
        # 'wc': wc,
        'ic': ic,
    }

    # # Prepare Callbacks
    cv.setMouseCallback(root_window, click_listener, params)
    cv.createButton("Save marks", save_marks_listener, params)
    cv.createButton("Reset", reset_listener, params)
    cv.createButton("Hide marks", hide_marks_listener, params, cv.QT_CHECKBOX)

    while cv.getWindowProperty(root_window, cv.WND_PROP_VISIBLE) > 0:
        # wait for a key to be pressed to exit
        if cv.waitKey(100) == 27:   # Quit when key "ESC"
            break

    print(F"PoI list: {ic.poi_list}")

    # close the window
    cv.destroyAllWindows()
