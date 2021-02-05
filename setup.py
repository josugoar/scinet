import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scinet-josugoar",
    version="0.5.0",
    author="josugoar",
    description="Network science abstract data types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/josugoar/scinet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
