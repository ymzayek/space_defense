"""Module for vessels of the space fleet."""
import numpy as np


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


rng = np.random.Random(0)


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


