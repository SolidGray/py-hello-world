from setuptools import setup

setup(
    name="py-hello-world",
    version="0.0.1",
    packages=[
        "py_hello_world",
    ],
    entry_points={
        "console_scripts": [
            "py-hello-world = py_hello_world.main:say_hi",
        ]
    }
)
