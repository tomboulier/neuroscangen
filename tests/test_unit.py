from neuroscangen.entities.brain_scan import BrainScan
from neuroscangen.use_cases.generate_scan import GenerateScan
from numpy import zeros
from numpy.testing import assert_array_equal


def test_generate_scan():
    generate_scan = GenerateScan()

    generated_scan = generate_scan()

    assert generated_scan is not None


def test_numpy_array():
    numy_array_3d = zeros((10, 10, 10))
    brain_scan = BrainScan(numy_array_3d)

    assert_array_equal(brain_scan.to_numpy_array(), numy_array_3d)
