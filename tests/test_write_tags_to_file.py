#!/usr/bin/env python3

from unittest import mock
from determine_docker_tags import write_tags_to_file


def test_write_tags_to_file():
    with mock.patch("determine_docker_tags.open", mock.mock_open()) as file:
        write_tags_to_file("1.18.0,1.18,1")

    file.assert_called_with(".tags", "w")
    file.return_value.write.assert_called_once_with("1.18.0,1.18,1")
