import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scinet-josugoar",
    version="0.5.0",
    description="Network science abstract data types",
    author="josugoar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/josugoar/scinet",
    download_url="https://github.com/josugoar/scinet/archive/v0.5.0.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="algorithms data-structures docker graph library pipenv python",
    project_urls={"Source": "https://github.com/josugoar/scinet"},
    python_requires=">=3.8",
)
