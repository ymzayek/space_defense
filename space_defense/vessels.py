"""Module for vessels of the space fleet."""
import numpy as np
from scipy.spatial import distance


# Base class for all types of vessels
class Vessel:
    def __init__(self, coords):
        self.coordinates = coords

    def move(self, coords_):
        self.coordinates = coords_


# Two main types of crafts
class SupportCraft(Vessel):
    def __init__(self, coords, medical_unit):
        super().__init__(coords)
        self.medical_unit = medical_unit


class OffensiveCraft(Vessel):
    def __init__(self, coords, cannons):
        super().__init__(coords)
        self.cannons = cannons

    def attack(self):
        raise NotImplementedError

    def raise_shields(self):
        raise NotImplementedError


# Three subtypes of support crafts
class RefuelingCraft(SupportCraft):
    def __init__(self, coords, medical_unit):
        super().__init__(coords, medical_unit)


class MechanicalAssistanceCraft(SupportCraft):
    def __init__(self, coords, medical_unit):
        super().__init__(coords, medical_unit)


class CargoCraft(SupportCraft):
    def __init__(self, coords, medical_unit):
        super().__init__(coords, medical_unit)


# Three subtypes of offensive crafts
class BattleshipCraft(OffensiveCraft):
    def __init__(self, coords):
        super().__init__(coords, 24)


class DestroyerCraft(OffensiveCraft):
    def __init__(self, coords):
        super().__init__(coords, 12)


class CruiserCraft(OffensiveCraft):
    def __init__(self, coords):
        super().__init__(coords, 6)


class CommandShip(BattleshipCraft):
    def __init__(self, coords):
        super().__init__(coords)


rng = np.random.RandomState(0)


def check_overlap(coords_list, new_coord):
    """Check if two coordinate pairs overlap"""
    for coord in coords_list:
        if coord[0] == new_coord[0] and coord[1] == new_coord[1]:
            return True
    return False


# Generate random list of coordinates to be assigned to the 50 vessels
coords_list = []
while len(coords_list) < 50:
    new_coord = (rng.randint(0, 99), rng.randint(0, 99))
    if not check_overlap(coords_list, new_coord):
        coords_list.append(new_coord)


# We only have one command ship and then add 24 offensive crafts
crafts_list = [CommandShip]
for i in range(8):
    crafts_list.append(CruiserCraft)
    crafts_list.append(DestroyerCraft)
    crafts_list.append(BattleshipCraft)
# Then add 25 support crafts
for i in range(8):
    crafts_list.append(RefuelingCraft)
    crafts_list.append(MechanicalAssistanceCraft)
    crafts_list.append(CargoCraft)
crafts_list.append(CargoCraft)


# Assign random coordsinates
ships = []
for coords, vessel in zip(coords_list, crafts_list):
    if issubclass(vessel, SupportCraft):
        ships.append(vessel((coords), 1))
    else:
        ships.append(vessel((coords)))


offensive_coords = [s.coordinates for s in ships[:25]]
support_coords = [s.coordinates for s in ships[25:50]]


# Calculate a distance matrix between offensive and defensive crafts
dist_matrix = distance.cdist(
    offensive_coords, support_coords, 'euclidean'
)


# Find the closest support ship for each offensive ship
for i in range(len(dist_matrix)):
    closest_index = np.argmin(dist_matrix[i])
    print(f"Closest point in offensive_coords for {offensive_coords[i]} is {support_coords[closest_index]}")



