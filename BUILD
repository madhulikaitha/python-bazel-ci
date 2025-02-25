
load("@rules_python//python:defs.bzl", "py_library", "py_test")


py_library(
    name = "math_utils_lib",
    srcs = ["src/math_utils.py"],
    visibility = ["//visibility:public"],
)


py_library(
    name = "string_utils_lib",
    srcs = ["src/string_utils.py"],
    visibility = ["//visibility:public"],
)


py_test(
    name = "test_math_utils",
    srcs = ["tests/test_math_utils.py"],
    deps = [":math_utils_lib"],
)

py_test(
    name = "test_string_utils",
    srcs = ["tests/test_string_utils.py"],
    deps = [":string_utils_lib"],
)


sh_test(
    name = "lint_check",
    srcs = ["scripts/lint.sh"],
)

sh_test(
    name = "format_check",
    srcs = ["scripts/format.sh"],
)
