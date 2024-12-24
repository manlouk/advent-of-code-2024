import pytest 
from solutions.day9 import convert_disk_map, checksum

# def test_convert_disk_map():

#     assert convert_disk_map("12345") == ["0",".",".","1","1","1",".",".",".",".","2","2","2","2","2"]
#     assert convert_disk_map("2333133121414131402") ==  [c for c in "00...111...2...333.44.5555.6666.777.888899"]

def test_checksum():
    
    #assert checksum(convert_disk_map("2333133121414131402"))==2858

    # assert checksum(convert_disk_map("23321"))==22
    # assert checksum(convert_disk_map("23223"))==21
    assert checksum(convert_disk_map("2333133121414131402"))==2858