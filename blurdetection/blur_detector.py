import numpy as np
from scipy import fftpack

def detect_blur_fft(arr: np.array, keep_fraction=0.2, thresh=2.8) -> tuple:
    # image dimension
    h, w = arr.shape

    # Fourier transform
    # change from spatial to spectral domain
    fft = fftpack.fft2(arr)

    # shift spectrum before filtering in the next step
    # this means low frequency (usually signal) is centric,
    # high frequency (noise) is at the border
    fft = np.fft.fftshift(fft)

    # Set to zero coefficients we're not keeping (1-keep_fraction)
    # This acts as a filter
    # What we keep is high frequency components
    fft[int(h * keep_fraction):int(h * (1 - keep_fraction)),
        int(w * keep_fraction):int(w * (1-keep_fraction))] = 0

    # undo shift before reconstructing image
    fft = np.fft.ifftshift(fft)

    # Reconstruct image
    rec = np.fft.ifft2(fft)

    # Compute mean absolute value of filtered image
    mean = np.mean(np.abs(rec))

    return (mean, mean <= thresh)
