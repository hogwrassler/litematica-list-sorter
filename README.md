# litematica-list-sorter

This script allows you to pass in a litematica material list and receive a sorted csv, grouped in order set by block-data/order.csv, with the total count, # stacks, # shulkers needed for each item.

# Tutorial:
* Install python (https://www.python.org/downloads/)

* Create your litematica schematic, and then write to file. This writes a text file to .minecraft/config/litematica/material_list_###.txt
* Open command prompt, navigate to this repo and enter:
    ```
    python listSorter.py <path to your material list>
    ```
* The sorted list will be output to the lists folder within this repo as a .csv.

* To modify the order of block families, you can modify block-data/order.csv.
* To modify the families of specific blocks, you can modify block-data/blockdata.json, replacing the "family" value with your choice from the options in order.csv.