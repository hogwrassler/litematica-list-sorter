# litematica-list-sorter

pass in a litematica material list and receive a sorted csv, grouped in order set by block-data/order.csv, with the total count, # stacks, # shulkers needed

How to use:
Must have python installed for use (https://www.python.org/downloads/)
Open command prompt, navigate to this repo and enter:
    python listSorter.py <path to litematica material list>

The sorted list will be output to the lists folder within this repo as a .csv.

To modify the order of block families, you can modify block-data/order.csv.
To modify the families of specific blocks, you can modify blockdata.json, replacing the "family" value with your choice from the options in order.csv.