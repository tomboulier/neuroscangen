from dataclasses import dataclass, field
import numpy as np


@dataclass
class BrainScan:
    values: np.ndarray = field(default_factory=lambda: np.empty((0, 0, 0)))

    def to_numpy_array(self) -> np.ndarray:
        return self.values
