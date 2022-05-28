import argparse
from PIL import Image
import numpy as np
import os
import statistics


def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--baseline', required=True, type=str, help='The directory which contains baseline images named \'N_region.png\'.')
    parser.add_argument('-m', '--modified', required=True, type=str, help='The directory which contains modified images named \'N_region.png\'.')
    return parser


def sharpness(image_file):
    print(image_file)
    image = Image.open(image_file).convert('L')
    image = np.asarray(image, dtype=np.int32)
    h, w = image.shape

    # if the inpainted area is too small -- skip it
    if h == 1 or w == 1:
        return -1

    y_grad, x_grad = np.gradient(image)
    grad = np.sqrt(x_grad**2 + y_grad**2)
    sharpness = np.average(grad)
    return sharpness


if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args()

    print(sharpness('lena.png'))
    print(sharpness('lena_blurred.png'))
    exit()

    files = [file for file in os.listdir(args.baseline) if ("_region" in file) and (file in os.listdir(args.modified))]

    baseline = []
    modified = []

    for file in files:
        sharp_b = sharpness(args.baseline + file)
        sharp_m = sharpness(args.modified + file)

        if sharp_b == -1 or sharp_m == -1:
            continue

        baseline += [sharp_b]
        modified += [sharp_m]

    baseline_sharpness = statistics.mean(baseline)
    modified_sharpness = statistics.mean(modified)

    print("Baseline sharpness:   %.3f" % baseline_sharpness)
    print("Modified sharpness:   %.3f" % modified_sharpness)
