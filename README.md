# Cellpose Overlap Dataset

A small cell dataset with overlapped labels.

used with https://github.com/kirkegaardlab/diffusionsplit

## Instructions
Download this repository and place the original cellpose dataset (downloadable from https://www.cellpose.org/dataset) in the `cellposedataset` folder.
Run `python overlap_dataset.py` and the dataset is now available in the folder `overlapdataset`.
Note that there are multiple label files per image in order to account for overlapping masks.
