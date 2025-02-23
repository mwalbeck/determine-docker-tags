#!/usr/bin/env python3

import os
import re
from datetime import date


def determine_tags(
        version_string, app_env, include_major, include_suffix, version_passthrough, image_name, separator
):
    tags = ""

    if version_passthrough == "yes":
        return version_string

    if "-" in version_string:
        extra_info = version_string[version_string.find("-"):]
        version_string = version_string[: version_string.find("-")]
    else:
        extra_info = ""

    if include_suffix == "no":
        extra_info = ""

    if app_env:
        app_env = "-" + app_env
    else:
        app_env = ""

    while "." in version_string:
        tags = tags + image_name + version_string + extra_info + app_env + separator
        version_string = version_string[: version_string.rfind(".")]

    if include_major == "yes" and version_string != "0":
        tags = tags + image_name + version_string + extra_info + app_env
    else:
        tags = tags[:-1]

    return tags


def write_tags_to_file(tags, path):
    print(tags)

    if path != ".tags":
        tags = "tags=" + tags

    with open(path, "w") as file:
        file.write(tags)


def is_app_name_empty(app_name):
    if not app_name or app_name.isspace():
        raise ValueError(
            "APP_NAME is required when VERSION_TYPE is docker_env or docker_from"
        )


def main():
    version_type = os.getenv("VERSION_TYPE", "")  # docker_env, docker_from or date
    image_name = os.getenv("IMAGE_NAME", "")  # The full name and path of the image
    app_name = os.getenv("APP_NAME", "")
    dockerfile_path = os.getenv("DOCKERFILE_PATH", "Dockerfile")
    app_env = os.getenv("APP_ENV", "")
    custom_tags = os.getenv("CUSTOM_TAGS", "")
    include_major = os.getenv("INCLUDE_MAJOR", "yes")  # yes or no
    include_suffix = os.getenv("INCLUDE_SUFFIX", "yes")  # yes or no
    version_passthrough = os.getenv("VERSION_PASSTHROUGH", "no")  # yes or no
    include_extra_info = os.getenv("INCLUDE_EXTRA_INFO", "")  # DEPRECATED
    separator = os.getenv("SEPARATOR", ",")
    path = os.getenv("GITHUB_OUTPUT", ".tags")

    if image_name != "":
        image_name = image_name + ":"

    if include_extra_info and not include_extra_info.isspace():
        print(
            "DEPRECATION NOTICE: INCLUDE_EXTRA_INFO is deprecated. Please use INCLUDE_SUFFIX instead."
        )
        include_suffix = include_extra_info

    if include_major == "positive":
        include_major = "yes"
    elif include_major == "negative":
        include_major = "no"

    if include_suffix == "positive":
        include_suffix = "yes"
    elif include_suffix == "negative":
        include_suffix = "no"

    if version_passthrough == "positive":
        version_passthrough = "yes"
    elif version_passthrough == "negative":
        version_passthrough = "no"

    if version_type == "docker_env":
        is_app_name_empty(app_name)

        with open(dockerfile_path) as dockerfile:
            for line in dockerfile:
                if re.search(rf"ENV {app_name}_VERSION=.*", line):
                    version_string = line[line.find("=", 4) + 1:].strip()
                    break
                elif re.search(rf"ENV {app_name}_VERSION .*", line):
                    version_string = line[line.find(" ", 4) + 1:].strip()
                    break

        if version_string[0] == "v":
            version_string = version_string[1:]

        if (
                "-" not in version_string
                and version_passthrough == "no"
                and re.fullmatch(r"v?\d+\.\d+\.\d+[A-Za-z_]{1}\w+", version_string)
        ):
            split_version_string = re.split(
                r"(\d+\.\d+\.\d+)([A-Za-z_]{1}.*)", version_string
            )

            if split_version_string[1] != "" and split_version_string[2] != "":
                version_string = split_version_string[1] + "-" + split_version_string[2]

        tags = determine_tags(
            version_string, app_env, include_major, include_suffix, version_passthrough, image_name, separator
        )

    elif version_type == "docker_from":
        is_app_name_empty(app_name)

        with open(dockerfile_path) as dockerfile:
            for line in dockerfile:
                if re.search(rf"FROM {app_name}:.*", line):
                    version_string = line[line.find(":") + 1:].strip()
                    break

        if "@" in version_string:
            version_string = version_string[: version_string.find("@")]

        tags = determine_tags(
            version_string, app_env, include_major, include_suffix, version_passthrough, image_name, separator
        )

    elif version_type == "date":
        version_string = date.today().strftime("%Y%m%d")
        tags = version_string

    elif custom_tags and not version_type:
        tags = image_name + custom_tags
        custom_tags = ""

    else:
        print("Please specify a VERSION_TYPE or set CUSTOM_TAGS.")
        exit(-1)

    if custom_tags:
        tags += separator + image_name + custom_tags

    write_tags_to_file(tags, path)


if __name__ == "__main__":
    main()
