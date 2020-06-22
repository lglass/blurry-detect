from blurdetection.blur_detector import detect_blur_fft
from blurdetection.processing import load_scan, plot, reporting
import argparse
from glob import glob
from pathlib import Path
import os

AUSWERTUNG = "auswertung.xlsx"

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=False,
	help="path input image that we'll detect blur in")
ap.add_argument("-f", "--folder", type=str, required=False,
	help="directory path")
ap.add_argument("-t", "--thresh", type=float, default=2.8,
	help="threshold above which an image is not blurry")
args = vars(ap.parse_args())

if not os.path.exists('plots'):
	os.makedirs('plots')

# single image blurryness detection
if args["image"]:
	file_name = args["image"]

	file_id = Path(file_name).stem
	arr = load_scan(file_name)
	(mean, blurry) = detect_blur_fft(arr, keep_fraction=0.2,
									 thresh=args["thresh"])

	plot(arr, mean, blurry, file_id, "plots")

# create report for images in a folder
if args["folder"]:
	report = reporting(AUSWERTUNG)

	for file_name in glob("{}*.nii".format(args["folder"])):
		file_id = Path(file_name).stem
		arr = load_scan(file_name)
		(mean, blurry) = detect_blur_fft(arr, keep_fraction=0.2,
										 thresh=args["thresh"])

		print(mean, blurry)
		#plot(arr, mean, blurry, file_id, "plots")

		report.add_line(file_id, blurry)

	report.finish()