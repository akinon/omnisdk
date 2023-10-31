from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="omnisdk",
    version="0.0.102",
    packages=["omnisdk", "omnisdk.omnitron"],
    url="https://bitbucket.org/akinonteam/omnisdk",
    description="SDK for Omni Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="akinonteam",
    python_requires=">=3.5",
    # We should pin the below to work with all the way from py27 to upto py39
    install_requires=["requests", "backoff"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
    ],
)
