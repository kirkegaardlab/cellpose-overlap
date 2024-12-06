# Cellpose Overlap Dataset

A small cell dataset with overlapped labels.

Used with https://github.com/kirkegaardlab/diffusionsplit for the paper [Spontaneous breaking of symmetry in overlapping cell instance segmentation using diffusion models](https://academic.oup.com/biomethods/advance-article/doi/10.1093/biomethods/bpae084/7888887?login=true).

## Instructions
Download this repository and place the original cellpose dataset (downloadable from https://www.cellpose.org/dataset) in the `cellposedataset` folder.
Run `python overlap_dataset.py` and the dataset is now available in the folder `overlapdataset`.
Note that there are multiple label files per image in order to account for overlapping masks.
