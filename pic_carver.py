import re
import zlib
import cv2

from scapy.all import *

pictures_directory = "/home/Pictures"
faces_directory = ""
pcap_file = ""

def http_assembler(pcap_file):
