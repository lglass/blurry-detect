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
ap.add_argument("-t", "--thresh", type=int, default=20,
	help="threshold for our blur detector to fire")
args = vars(ap.parse_args())

if not os.path.exists('my_folder'):
	os.makedirs('my_folder')

# single image blurryness detection
if args["image"]:
	file_name = args["image"]

	file_id = Path(file_name).stem
	arr = load_scan(file_name)
	(mean, blurry) = detect_blur_fft(arr, size=30,
									 thresh=args["thresh"])


	plot(arr, mean, blurry, file_id, "plots")


if args["folder"]:
	report = reporting(AUSWERTUNG)

	for file_name in glob("{}*.nii".format(args["folder"])):
		file_id = Path(file_name).stem
		arr = load_scan(file_name)
		(mean, blurry) = detect_blur_fft(arr, size=30,
										 thresh=args["thresh"])

		plot(arr, mean, blurry, file_id, "plots")

		report.add_line(file_id, blurry)

	report.finish()