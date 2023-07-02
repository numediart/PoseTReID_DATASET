# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                           #
#   Code: MIT License                                                       #
#                                                                           #
#   Dataset: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)        #
#                                                                           #
#   Copyright (c) 2023 Ratha SIV                                            #
#                                                                           #
#   pyppbox-data-gta5: The restructured GTA_V_DATASET for pyppbox V3.       #
#                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import argparse

filename = 'GTA_V_DATASET.7z.001'
destination = '../pyppbox-data-gta5/pyppbox/data/datasets'

def install_dependencies():
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyunpack", "patool"])

def decompress(filename=filename, destination=destination, clear_destination=True):
    import os
    import shutil
    from pyunpack import Archive
    if clear_destination and os.path.exists(destination):
        shutil.rmtree(destination)
        os.makedirs(destination)
    if os.path.exists(filename) and os.path.exists(destination):
        try:
            Archive(filename).extractall(destination)
        except Exception as e:
            raise ValueError(e)
    else:
        raise ValueError('Invalid path(s)!')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Help you extract or decompress file.")
    parser.add_argument("--filename", type=str, default=filename, help="File to be extracted")
    parser.add_argument("--destination", type=str, default=destination, help="Path of where to extract to")
    parser.add_argument("--clear-destination", type=bool, default=True, help="Clear destination before extract")
    args = parser.parse_args()
    install_dependencies()
    decompress(filename=args.filename, destination=args.destination, clear_destination=args.clear_destination)
