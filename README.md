# blurry-detect
Determine an MRI image's blurriness with Fourier Analysis


To set up the environment, e.g. run

    python -m venv blurry_detect
    source blurry_detect/bin/activate
    pip install -r requirements.txt


To determine blurriness for all *.nii images in a folder, run

    python blur_detector_image.py --folder $FOLDER_NII

To make an animated video out of the predictions, run

    ffmpeg -framerate 3 -pattern_type glob -i 'plots/*.jpg' -c:v libx264 animated.mp4