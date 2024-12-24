import pytest
from solutions.day8 import get_antennas_points, antinode_points, read_map, get_antinode_points

@pytest.fixture
def antenas_map():
    return [
       ['.','A','O','.'],
       ['.','O','.','.'],
       ['O','.','.','A'],
       ['.','.','O','.']
    ]


def test_get_antinode_points():
   
   assert get_antinode_points((2,5),(3,7)) == [(1,3),(4,9)]
   assert get_antinode_points((3,4),(5,5)) == [(1,3),(7,6)]
   assert get_antinode_points((3,4),(4,8)) == [(2,0),(5,12)]
   assert get_antinode_points((1,8),(2,5)) == [(0,11),(3,2)]
   assert get_antinode_points((4, 4), (3, 7)) == [()]


def test_get_antenas_points(antenas_map):

    assert get_antennas_points(antenas_map) == {"O":{(0,2),(1,1),(2,0),(3,2)},"A":{(0,1),(2,3)}}

def test_antinode_points():
    antennas_map = read_map("tests/data/test_input8.txt")
    assert antinode_points(antennas_map) == 14