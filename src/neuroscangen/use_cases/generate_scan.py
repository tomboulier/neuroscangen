from dataclasses import dataclass


@dataclass
class BrainScan:
    def __init__(self):
        pass


class GenerateScan:
    def __call__(self):
        return BrainScan()
