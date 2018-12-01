from pint.testing import assert_array_equal

from pint import UnitRegistry

from pint.compat import np
from pint.testsuite import QuantityTestCase, helpers


UREG = UnitRegistry()

@helpers.requires_numpy()
class TestTesting(QuantityTestCase):
    FORCE_NDARRAY = False


    def test_equal(self):
        a = np.array([1, 2]) * UREG("m")
        b = np.array([1, 2]) * UREG("m")

        assert_array_equal(a, b)

    def test_unequal_error(self):
        a = np.array([1, 2]) * UREG("m")
        b = np.array([1, 2]) * UREG("m")

        with self.assertRaises(AssertionError) as context:
            assert_array_equal(a, b)

        self.assertTrue("This is broken" in context.exception)
