# Networkscanner

Scan your local network using nmap and python

---

## Preview:

![alt tag](https://github.com/Wheele9/Networkscanner/blob/master/scan.gif)

---

## Usage

### Install python-nmap: 

`pip install python-nmap`

### Get the MAC adresses of your devices

#### On Linux: 

`ifconfig -a`

#### On Windows: 

`ipconfig`

### Fill the KNOWN_MACS dictionary in info.py with your devices, and device names

### Run 

`sudo python scan.py`

---
## Enjoy!


If you have problem importing nmap, try `sudo $(which python) scan.py`


