import json
import os 
from pathlib import Path
import shutil

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

with open(dir_path / 'assigned.json', 'r') as f:
    assigned = json.load(f)

if not (dir_path / 'cellposedataset/train/041_img.png').exists():
    print(f"Error: Cellpose train dataset should be in {dir_path / 'cellposedataset/train/'}")
    print('        Download from https://www.cellpose.org/dataset')
    exit()

if not (dir_path / 'cellposedataset/test/001_img.png').exists():
    print(f"Error: Cellpose train dataset should be in {dir_path / 'cellposedataset/test/'}")
    print('        Download from https://www.cellpose.org/dataset')
    exit()

for f_to, f_from in assigned.items():
    f_from = str(dir_path / f_from)
    f_to = str(dir_path / f_to)
    print(f'Copying {f_from} to {f_to}.')
    shutil.copy(f_from, f_to)
