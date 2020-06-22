import nibabel as nib
import matplotlib.pyplot as plt
import os

def load_scan(file_name):
    scan = nib.load(file_name)
    data = scan.get_fdata()

    if data.ndim == 2:
        arr = (data - data.min())/(data.max()-data.min()) * 255
        return arr
    # if data.ndim == 3:
    #     xdim, ydim, zdim = data.shape
    #     for idx in range(len(zdim)):
    #         data_slice = data[:, :, idx]
    #         arr = (data_slice - data_slice.min()) / (data_slice.max() - data_slice.min()) * 255
    #         return arr

def plot(image, mean, blurry, nr, fig_path):
    # draw on the image, indicating whether or not it is blurry
    color = (0, 0, 255) if blurry else (0, 255, 0)
    text = "Blurry ({:.4f})" if blurry else "Not Blurry ({:.4f})"
    text = text.format(mean)
    text = text + "\n{}".format(nr)
    # print("[INFO] {}".format(text))

    fig, ax = plt.subplots()
    title_obj = ax.set_title(text)
    if mean <= 17:
        plt.setp(title_obj, color='r')
    elif mean <= 23:
        plt.setp(title_obj, color='y')
    else:
        plt.setp(title_obj, color='g')
    ax.imshow(image)

    fig.savefig(os.path.join(fig_path, f"{nr}.jpg"))
    plt.close("all")



