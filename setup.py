import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enjoy",
    version="0.0.1",
    author="Matteo Nastasi",
    author_email="nastasi@alternativeoutput.it",
    description="Backend for full interactive web-app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alternativeoutput/enjoy",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
