from unittest import TestCase
from src.params import Params

params = Params(key="dummy_key", values="dummy_value")


class TestParams(TestCase):
    def test_init_valid_defaults(self):
        test_params = Params(key="dummy_key", values="dummy_value")
        assert test_params.type == "categorical"
        assert test_params.min == 0
        assert test_params.max == 0
        assert test_params.steps == 0
        assert test_params.scale == "linear"
        assert test_params.key == "dummy_key"
        assert test_params.values == "dummy_value"
