import copy

import numpy as np


POWERS = np.arange(3, 16)

class LegHandelingOperation:
    """
    This is a class for handling leg operation. It calculates the equivalent distance and the damage from the operation leg data and the configuration settings.
    The leg data includes the load and the distance travelled by the leg. The configuration settings include the bin settings, the bin mapping for lifting and lowering, and the bin pinion loads.

    :param load: The load on the leg.
    :type load: float
    :param distance: The distance travelled by the leg.
    :type distance: float
    :param config_bin_settings: The configuration settings for the bins.
    :type config_bin_settings: dict

    """

    def __init__(
        self,
        load: float,
        distance: float,
        config_bin_settings: dict,
    ):
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
        """
        This method reads each operation and maps them to either lifting or lowering based on the positive or negative distance value, respectively.

        :param mapping_lifting: The mapping for lifting operations.
        :param mapping_lowering: The mapping for lowering operations.

        """
        if self.distance >= 0:
            self.is_in_bin_number = int(mapping_lifting[self.digitized])
        else:
            self.is_in_bin_number = int(mapping_lowering[self.digitized])

    def calculate_equivalent_distance(self, max_power_asset) -> float:
        """
        This method calculates the equivalent distance for each operation. It uses the maximum power of the asset to calculate the equivalent distance.

        :param max_power_asset: The power with the maximum damage of the asset.
        :type max_power_asset: int

        :return: The equivalent distance.
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
        """
        This method calculates the damage for each operation. It uses the factors to calculate the damage.

        :param factors: The factors for each bin.
        :type factors: np.ndarray

        :return: The damage.

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

    :param x: The first number.
    :type x: float or int
    :param y: The second number.
    :type y: float or int

    .. math::
        \sum_{i=1}^{n} \frac{d_i}{L_i} = 1

    where :math:`d_i` is the design distance and :math:`L_i` is the design pinion load for each bin. The factors are then calculated as follows:
    
    Returns:
        float or int: The result of the addition operation.
    """
    return x + y