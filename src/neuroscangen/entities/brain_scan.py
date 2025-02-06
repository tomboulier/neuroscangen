"""
brain_scan.py
=============

This module contains the BrainScan class, which is used to represent a brain scan.

Classes
-------
BrainScan
    A class used to represent a brain scan with a 3D numpy array.

Examples
--------
>>> import numpy as np
>>> from neuroscangen.entities.brain_scan import BrainScan
>>> scan_data = np.random.rand(5, 5, 5)
>>> brain_scan = BrainScan(values=scan_data)
>>> array = brain_scan.to_numpy_array()
>>> print(array.shape)
(5, 5, 5)
"""

from dataclasses import dataclass, field
import numpy as np


@dataclass
class BrainScan:
    """
    A class used to represent a Brain Scan.

    Attributes
    ----------
    values : np.ndarray
        A 3D numpy array representing the brain scan data.

    Methods
    -------
    to_numpy_array() -> np.ndarray
        Returns the brain scan data as a numpy array.
    """

    values: np.ndarray = field(default_factory=lambda: np.empty((0, 0, 0)))

    def to_numpy_array(self) -> np.ndarray:
        """
        Returns the brain scan data as a numpy array.

        Returns
        -------
        np.ndarray
            The brain scan data.
        """
        return self.values
