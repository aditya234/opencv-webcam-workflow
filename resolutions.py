import cv2
import csv

cap = cv2.VideoCapture(0)

all_resolutions = {}

with open("resolutions.csv") as csv_file:
    resolutions = csv.reader(csv_file, delimiter='\t')
    for row in resolutions:
        # print(row)
        width = int(row[1].split('Ã—')[0])
        height = int(row[1].split('Ã—')[1])
        print(f"{width} x {height}")
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        all_resolutions[str(width) + " x " + str(height)] = "Supported"
# {'160.0 x 120.0': 'Supported', '320.0 x 240.0': 'Supported', '424.0 x 240.0': 'Supported',
# '640.0 x 360.0': 'Supported', '640.0 x 480.0': 'Supported', '848.0 x 480.0': 'Supported',
# '960.0 x 540.0': 'Supported', '1280.0 x 720.0': 'Supported'}
print(all_resolutions)