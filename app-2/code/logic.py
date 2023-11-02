import copy

import numpy as np


POWERS = np.arange(3, 16)

class LegHandelingOperation:
    """This is a class for handling leg operation. 
    
    Attributes
    ----------
    attr1: load (float): The load on the leg.
    attr2: distance (float): The distance the leg has moved.
    attr3: is_in_bin_number (int): The bin number the operation is in.
    attr4: config_bin_settings (dict): The bin settings.
    
    """
    def __init__(
        self,
        load: float,
        distance: float,
        config_bin_settings: dict,
    ):
        """Initializes LegHandelingOperation with load, distance, and bin settings.

        Args:
            load (float): The load on the leg.
            distance (float): The distance the leg has moved.
            config_bin_settings (dict): The configuration settings for the bin.
        """
        self.load = load
        self.distance = distance
        self.is_in_bin_number: int
        self.config_bin_settings = config_bin_settings
        self.calculate_digitize(self.config_bin_settings["bin_settings"])
        self.apply_mapping(
            self.config_bin_settings["bin_mapping_lowering"],
            self.config_bin_settings["bin_mapping_lifting"],
        )

    def calculate_digitize(self, bins) -> None:
        self.digitized = np.digitize(self.load, bins, right=True) - 1

    def apply_mapping(self, mapping_lifting, mapping_lowering) -> None:
        """This method reads each operation and maps them to either lifting or lowering based on the positive or negative distance value, respectively.

        Args
        ----
        arg1: mapping_lifting: The mapping for lifting operations.
        arg2: mapping_lowering: The mapping for lowering operations.
        """
        
        if self.distance >= 0:
            self.is_in_bin_number = int(mapping_lifting[self.digitized])
        else:
            self.is_in_bin_number = int(mapping_lowering[self.digitized])

    def calculate_equivalent_distance(self, max_power_asset) -> float:
        """Calculates the equivalent distance for the leg operation.

        Args:
            max_power_asset: The maximum power of the asset.

        Returns:
            The equivalent distance for the leg operation.
        """
        equivalent_distance = (
            np.abs(self.distance)
            * (
                self.load
                / self.config_bin_settings["bin_pinion_loads"][self.is_in_bin_number]
            )
            ** max_power_asset
        )
        return equivalent_distance

    def calculate_damage(self, factors) -> np.ndarray:
        """Calculates the damage to the leg.

        Args:
            factors: The factors affecting the damage.

        Returns:
            The damage to the leg.
        """
        damage = abs(
            self.distance * factors * np.power(self.load, POWERS, dtype=np.float64)
        )
        return damage

    def get_name(self) -> str:
        if self.load != 0:
            return self.config_bin_settings["bin_names"][self.is_in_bin_number]
        return "None"

    def __str__(self) -> str:
        return f"""LegHandelingOperation(load={self.load},
          distance={self.distance}, is_in_bin_number={self.is_in_bin_number})"""

def add(x, y):
    """
    Perform addition of two numbers.

    Args:
        x (float or int): The first number.
        y (float or int): The second number.

    Returns:
        float or int: The result of the addition operation.
    """
    return x + y