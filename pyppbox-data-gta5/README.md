# `pyppbox-data-gta5`

* `pyppbox-data-gta5` is a package of the restructured `GTA_V_DATASET` for [`pyppbox`](https://github.com/rathaumons/pyppbox) V3.
* Download `.whl`: https://github.com/rathaumons/PoseTReID_DATASET/releases
* Structure `pyppbox-data-gta5`:

  ```
  GTA_V_DATASET  ............  PoseTReID's GTA_V_DATASET, pyppbox-data-gta5
  ├───body_128x256  .........  Cropped & classified body boxes in 128x256
  │   ├───Amanda
  │   │       *.jpg
  │   ├───Franklin
  │   │       *.jpg
  │   ├───Lester
  │   │       *.jpg
  │   ├───Michael
  │   │       *.jpg
  │   └───Trevor
  │           *.jpg
  ├───face_182x182  ........  Cropped & classified face boxes in 182x182
  │   ├───Amanda
  │   │       *.png
  │   ├───Franklin
  │   │       *.png
  │   ├───Lester
  │   │       *.png
  │   ├───Michael
  │   │       *.png
  │   └───Trevor
  │           *.png
  ├───ground_truth  .........  Ground-truth directory
  │       gt_map.txt  .......  VIDEO:TXT mapping file
  │       *.txt  ............  Ground-truth  .txt file
  │       *.csv  ............  Ground-truth  .csv file
  └───videos
          *.mp4
  ```

* `pyppbox-data-gta5` carries 2 licenses for both code and dataset:

  ```
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
  ```
