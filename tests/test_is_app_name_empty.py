#!/usr/bin/env python3

import pytest
from determine_docker_tags import is_app_name_empty


def test_is_app_name_empty():
    with pytest.raises(ValueError):
        is_app_name_empty("   ")

    with pytest.raises(ValueError):
        is_app_name_empty("")

    assert is_app_name_empty("test") is None
