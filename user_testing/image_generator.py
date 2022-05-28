import argparse
import os
import random
from matplotlib import image
from matplotlib import pyplot
import matplotlib as plt
import matplotlib.pyplot as pyplot
import numpy as np
import subprocess


def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--baseline', required=True, type=str, help='The directory which contains baseline model.')
    parser.add_argument('-m', '--modified', required=True, type=str, help='The directory which contains modified model.')
    parser.add_argument('-o', '--outdir', required=True, type=str, help='The directory into which generated samples are saved.')
    parser.add_argument('-t', '--script-dir', required=True, type=str, help='The directory with test.py script that runs model.')
    parser.add_argument('-f', '--flist', required=True, type=str, help='The .flist file.')
    parser.add_argument('-n', '--samples', required=True, type=int, help='The number of generated samples.')
    parser.add_argument('--show-names', default=False, action='store_true', help='If passed, then the app shows source of impainted image (baseline or modified model).')
    parser.add_argument('--save-only-inpainting', default=False, action='store_true', help='If passed, then only the inpainted regions are saved.')
    return parser


def random_bbox(image_h, image_w, max_bbox_h=128, max_bbox_w=128):
    t = random.randint(0, image_h - 30)
    l = random.randint(0, image_w - 30)
    h = random.randint(30, max_bbox_h)
    w = random.randint(30, max_bbox_w)
    b = min(t + h, image_h)
    r = min(l + w, image_w)
    return t, l, r, b


if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args()

    # convert relative to absolute paths
    original_cwd = os.getcwd() + '/'
    args.baseline = original_cwd + args.baseline
    args.modified = original_cwd + args.modified
    args.outdir   = original_cwd + args.outdir

    baseline_out_dir = args.outdir + 'baseline/'
    modified_out_dir = args.outdir + 'modified/'
    masks_out_dir    = args.outdir + 'masks/'

    # create output dirs
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    if not os.path.exists(baseline_out_dir):
        os.makedirs(baseline_out_dir)
    if not os.path.exists(modified_out_dir):
        os.makedirs(modified_out_dir)
    if not os.path.exists(masks_out_dir):
        os.makedirs(masks_out_dir)

    # load .flist
    with open(args.flist) as f:
        images = f.readlines()
        images = [img.rstrip() for img in images]

    max_mask_rectangles = 4

    # inpaint only a single region when we want to save it
    if args.save_only_inpainting:
        max_mask_rectangles = 1

    # generate samples
    for i in range(100, args.samples):
        # pick random image
        image_file = original_cwd + random.choice(images)
        image = plt.image.imread(image_file)
        h, w, c = image.shape

        # generate empty mask
        np.set_printoptions(threshold=np.inf)
        mask = np.zeros((h, w, c), dtype=float)

        # add rectangles to mask
        for _ in range(random.randint(1, max_mask_rectangles)):
            t, l, r, b = random_bbox(h, w)
            mask[t:b, l:r] = np.ones((b-t, r-l, c), dtype=float)

        # safe mask
        mask_file = masks_out_dir + str(i+1).rjust(4, '0') + '_mask.png'
        plt.image.imsave(mask_file, mask)

        # inpaint image using both models
        os.chdir(args.script_dir)

        out_baseline_file = baseline_out_dir + str(i+1).rjust(4, '0') + '.png'
        subprocess.run(['python3', 'test.py', '--image', image_file, '--mask', mask_file, '--output', out_baseline_file, '--checkpoint', args.baseline])

        out_modified_file = modified_out_dir + str(i+1).rjust(4, '0') + '.png'
        subprocess.run(['python3', 'test.py', '--image', image_file, '--mask', mask_file, '--output', out_modified_file, '--checkpoint', args.modified])

        os.chdir(original_cwd)

        # optionally save inpainted region
        region_baseline_file = baseline_out_dir + str(i+1).rjust(4, '0') + '_region.png'
        image_baseline = plt.image.imread(out_baseline_file)
        inpainted_region_baseline = image_baseline[t:b, l:r]
        plt.image.imsave(region_baseline_file, inpainted_region_baseline)

        region_modified_file = modified_out_dir + str(i+1).rjust(4, '0') + '_region.png'
        image_modified = plt.image.imread(out_modified_file)
        inpainted_region_modified = image_modified[t:b, l:r]
        plt.image.imsave(region_modified_file, inpainted_region_modified)
