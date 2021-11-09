import cv2 as cv


class ImageContext:
    def __init__(self, img_path, window, output_path, mark_config=None):
        self.poi_list = []

        self.window = window

        # Marks config
        if mark_config is None:
            self.mark_config = {
                'radius': 10,
                'color': (0, 255, 0),
                'thickness': 2,
                'output_path': output_path,
            }
        else:
            self.mark_config = mark_config

        self.img_path = img_path

        # Read image
        self.img_orig = cv.imread(img_path, 1)

        # Backup original image
        self.img = self.img_orig.copy()

    def showImage(self, hide_marks=False):
        poi_list = self.poi_list if not hide_marks else []
        img = self.img_orig.copy()

        cv.imshow(self.window, img)
        for poi in poi_list:
            cv.circle(
                img,
                poi,
                radius=self.mark_config['radius'],
                color=self.mark_config['color'],
                thickness=self.mark_config['thickness']
            )
            cv.imshow(self.window, img)

    def addMark(self, x, y):
        self.poi_list.append((x, y))

    def resetMarks(self):
        self.poi_list.clear()
        self.showImage()


class WindowContext:
    def __init__(self, root_window):
        self.root_window = root_window
        # Create window
        cv.namedWindow(root_window, flags=cv.WINDOW_NORMAL)
