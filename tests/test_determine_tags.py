#!/usr/bin/env python3

from determine_docker_tags import determine_tags


def test_determine_tags():
    assert determine_tags("1.18.0", "", "yes", "yes", "no", "", ",") == "1.18.0,1.18,1"
    assert determine_tags("1.18.0", "", "yes", "no", "no", "", ",") == "1.18.0,1.18,1"
    assert determine_tags("1.18.0", "", "no", "yes", "no", "", ",") == "1.18.0,1.18"
    assert determine_tags("1.18.0", "", "no", "no", "no", "", ",") == "1.18.0,1.18"

    assert determine_tags("thisisastring", "", "yes", "yes", "no", "", ",") == "thisisastring"
    assert determine_tags("thisisastring", "", "yes", "no", "no", "", ",") == "thisisastring"
    assert determine_tags("thisisastring", "", "no", "yes", "no", "", ",") == ""
    assert determine_tags("thisisastring", "", "no", "no", "no", "", ",") == ""


def test_determine_tags_with_suffix():
    assert (
            determine_tags("1.18.0-alpine", "", "yes", "yes", "no", "", ",")
            == "1.18.0-alpine,1.18-alpine,1-alpine"
    )
    assert determine_tags("1.18.0-alpine", "", "yes", "no", "no", "", ",") == "1.18.0,1.18,1"
    assert (
            determine_tags("1.18.0-alpine", "", "no", "yes", "no", "", ",") == "1.18.0-alpine,1.18-alpine"
    )
    assert determine_tags("1.18.0-alpine", "", "no", "no", "no", "", ",") == "1.18.0,1.18"

    assert (
            determine_tags("thisisastring-suffix", "", "yes", "yes", "no", "", ",")
            == "thisisastring-suffix"
    )
    assert determine_tags("thisisastring-suffix", "", "yes", "no", "no", "", ",") == "thisisastring"
    assert determine_tags("thisisastring-suffix", "", "no", "yes", "no", "", ",") == ""
    assert determine_tags("thisisastring-suffix", "", "no", "no", "no", "", ",") == ""


def test_determine_tags_with_app_env():
    assert (
            determine_tags("1.18.0", "test", "yes", "yes", "no", "", ",") == "1.18.0-test,1.18-test,1-test"
    )
    assert (
            determine_tags("1.18.0", "test", "yes", "no", "no", "", ",") == "1.18.0-test,1.18-test,1-test"
    )
    assert determine_tags("1.18.0", "test", "no", "yes", "no", "", ",") == "1.18.0-test,1.18-test"
    assert determine_tags("1.18.0", "test", "no", "no", "no", "", ",") == "1.18.0-test,1.18-test"

    assert determine_tags("thisisastring", "test", "yes", "yes", "no", "", ",") == "thisisastring-test"
    assert determine_tags("thisisastring", "test", "yes", "no", "no", "", ",") == "thisisastring-test"
    assert determine_tags("thisisastring", "test", "no", "yes", "no", "", ",") == ""
    assert determine_tags("thisisastring", "test", "no", "no", "no", "", ",") == ""


def test_determine_tags_with_suffix_app_env():
    assert (
            determine_tags("1.18.0-alpine", "test", "yes", "yes", "no", "", ",")
            == "1.18.0-alpine-test,1.18-alpine-test,1-alpine-test"
    )
    assert (
            determine_tags("1.18.0-alpine", "test", "yes", "no", "no", "", ",")
            == "1.18.0-test,1.18-test,1-test"
    )
    assert (
            determine_tags("1.18.0-alpine", "test", "no", "yes", "no", "", ",")
            == "1.18.0-alpine-test,1.18-alpine-test"
    )
    assert (
            determine_tags("1.18.0-alpine", "test", "no", "no", "no", "", ",") == "1.18.0-test,1.18-test"
    )

    assert (
            determine_tags("thisisastring-suffix", "test", "yes", "yes", "no", "", ",")
            == "thisisastring-suffix-test"
    )
    assert (
            determine_tags("thisisastring-suffix", "test", "yes", "no", "no", "", ",")
            == "thisisastring-test"
    )
    assert determine_tags("thisisastring-suffix", "test", "no", "yes", "no", "", ",") == ""
    assert determine_tags("thisisastring-suffix", "test", "no", "no", "no", "", ",") == ""


def test_determine_tags_with_image_name():
    assert determine_tags("1.18.0", "", "yes", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          ",") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0,git.walbeck.it/walbeck-it/walbeck-it:1.18,git.walbeck.it/walbeck-it/walbeck-it:1"
    assert determine_tags("1.18.0", "", "yes", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          ",") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0,git.walbeck.it/walbeck-it/walbeck-it:1.18,git.walbeck.it/walbeck-it/walbeck-it:1"
    assert determine_tags("1.18.0", "", "no", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          ",") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0,git.walbeck.it/walbeck-it/walbeck-it:1.18"
    assert determine_tags("1.18.0", "", "no", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          ",") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0,git.walbeck.it/walbeck-it/walbeck-it:1.18"

    assert determine_tags("thisisastring", "", "yes", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          ",") == "git.walbeck.it/walbeck-it/walbeck-it:thisisastring"
    assert determine_tags("thisisastring", "", "yes", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          ",") == "git.walbeck.it/walbeck-it/walbeck-it:thisisastring"
    assert determine_tags("thisisastring", "", "no", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it", ",") == ""
    assert determine_tags("thisisastring", "", "no", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it", ",") == ""


def test_determine_tags_with_image_name_and_separator():
    assert determine_tags("1.18.0", "", "yes", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          "\n") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0\ngit.walbeck.it/walbeck-it/walbeck-it:1.18\ngit.walbeck.it/walbeck-it/walbeck-it:1"
    assert determine_tags("1.18.0", "", "yes", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          "\n") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0\ngit.walbeck.it/walbeck-it/walbeck-it:1.18\ngit.walbeck.it/walbeck-it/walbeck-it:1"
    assert determine_tags("1.18.0", "", "no", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          "\n") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0\ngit.walbeck.it/walbeck-it/walbeck-it:1.18"
    assert determine_tags("1.18.0", "", "no", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          "\n") == "git.walbeck.it/walbeck-it/walbeck-it:1.18.0\ngit.walbeck.it/walbeck-it/walbeck-it:1.18"

    assert determine_tags("thisisastring", "", "yes", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          "\n") == "git.walbeck.it/walbeck-it/walbeck-it:thisisastring"
    assert determine_tags("thisisastring", "", "yes", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it",
                          "\n") == "git.walbeck.it/walbeck-it/walbeck-it:thisisastring"
    assert determine_tags("thisisastring", "", "no", "yes", "no", "git.walbeck.it/walbeck-it/walbeck-it", "\n") == ""
    assert determine_tags("thisisastring", "", "no", "no", "no", "git.walbeck.it/walbeck-it/walbeck-it", "\n") == ""
