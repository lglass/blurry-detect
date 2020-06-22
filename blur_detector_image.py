from blurdetection.blur_detector import detect_blur_fft
from blurdetection.processing import load_scan, plot
import argparse
from glob import glob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path
import numpy as np
import xlsxwriter

AUSWERTUNG = "auswertung.xlsx"
workbook = xlsxwriter.Workbook(AUSWERTUNG)
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "MRT-Bild")
worksheet.write(0, 1, "Motion")
worksheet.write(0, 2, 'Ghosting')
worksheet.write(0, 3, "Blurring")
worksheet.write(0, 4, "Noise")
worksheet.write(0, 5, "Kein Artefakt")

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=False,
	help="path input image that we'll detect blur in")
ap.add_argument("-f", "--folder", type=str, required=False,
	help="directory path")
ap.add_argument("-t", "--thresh", type=int, default=20,
	help="threshold for our blur detector to fire")
args = vars(ap.parse_args())


for file_name in glob("{}*.nii".format(args["folder"])):
	nr = Path(file_name).stem
	arr = load_scan(file_name)
	(mean, blurry) = detect_blur_fft(arr, size=30,
									 thresh=args["thresh"])

	#plot(arr, mean, blurry, nr, "plots")

	worksheet.write(int(nr), 0, int(nr))
	if blurry:
		worksheet.write(int(nr), 3, 1)
	else:
		worksheet.write(int(nr), 5, 1)

workbook.close()
