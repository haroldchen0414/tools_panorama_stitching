# 示例
# python panorama.py --first images/example_1.png --second images/example_2.png
from tools.stitcher import Stitcher
import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="path to the first image")
ap.add_argument("-s", "--second", required=True, help="path to the second image")
args = vars(ap.parse_args())

imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)

