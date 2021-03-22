#!/usr/bin/env python3

from determine_docker_tags import determine_tags


def test_determine_tags():
    assert determine_tags("1.18.0", "", "yes", "yes") == "1.18.0,1.18,1"
    assert determine_tags("1.18.0", "", "yes", "no") == "1.18.0,1.18,1"
    assert determine_tags("1.18.0", "", "no", "yes") == "1.18.0,1.18"
    assert determine_tags("1.18.0", "", "no", "no") == "1.18.0,1.18"

    assert determine_tags("thisisastring", "", "yes", "yes") == "thisisastring"
    assert determine_tags("thisisastring", "", "yes", "no") == "thisisastring"
    assert determine_tags("thisisastring", "", "no", "yes") == ""
    assert determine_tags("thisisastring", "", "no", "no") == ""


def test_determine_tags_with_suffix():
    assert (
        determine_tags("1.18.0-alpine", "", "yes", "yes")
        == "1.18.0-alpine,1.18-alpine,1-alpine"
    )
    assert determine_tags("1.18.0-alpine", "", "yes", "no") == "1.18.0,1.18,1"
    assert (
        determine_tags("1.18.0-alpine", "", "no", "yes") == "1.18.0-alpine,1.18-alpine"
    )
    assert determine_tags("1.18.0-alpine", "", "no", "no") == "1.18.0,1.18"

    assert (
        determine_tags("thisisastring-suffix", "", "yes", "yes")
        == "thisisastring-suffix"
    )
    assert determine_tags("thisisastring-suffix", "", "yes", "no") == "thisisastring"
    assert determine_tags("thisisastring-suffix", "", "no", "yes") == ""
    assert determine_tags("thisisastring-suffix", "", "no", "no") == ""


def test_determine_tags_with_app_env():
    assert (
        determine_tags("1.18.0", "test", "yes", "yes") == "1.18.0-test,1.18-test,1-test"
    )
    assert (
        determine_tags("1.18.0", "test", "yes", "no") == "1.18.0-test,1.18-test,1-test"
    )
    assert determine_tags("1.18.0", "test", "no", "yes") == "1.18.0-test,1.18-test"
    assert determine_tags("1.18.0", "test", "no", "no") == "1.18.0-test,1.18-test"

    assert determine_tags("thisisastring", "test", "yes", "yes") == "thisisastring-test"
    assert determine_tags("thisisastring", "test", "yes", "no") == "thisisastring-test"
    assert determine_tags("thisisastring", "test", "no", "yes") == ""
    assert determine_tags("thisisastring", "test", "no", "no") == ""


def test_determine_tags_with_suffix_app_env():
    assert (
        determine_tags("1.18.0-alpine", "test", "yes", "yes")
        == "1.18.0-alpine-test,1.18-alpine-test,1-alpine-test"
    )
    assert (
        determine_tags("1.18.0-alpine", "test", "yes", "no")
        == "1.18.0-test,1.18-test,1-test"
    )
    assert (
        determine_tags("1.18.0-alpine", "test", "no", "yes")
        == "1.18.0-alpine-test,1.18-alpine-test"
    )
    assert (
        determine_tags("1.18.0-alpine", "test", "no", "no") == "1.18.0-test,1.18-test"
    )

    assert (
        determine_tags("thisisastring-suffix", "test", "yes", "yes")
        == "thisisastring-suffix-test"
    )
    assert (
        determine_tags("thisisastring-suffix", "test", "yes", "no")
        == "thisisastring-test"
    )
    assert determine_tags("thisisastring-suffix", "test", "no", "yes") == ""
    assert determine_tags("thisisastring-suffix", "test", "no", "no") == ""
