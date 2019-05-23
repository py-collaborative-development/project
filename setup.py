import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-collab-minesweeper",
    version="0.8.0",
    author="Imeev Mergen, Navolotskyi Alexey, Bulanbaev Arthur",
    author_email="imeevma@gmail.com",
    description="Python collaborative course project",
    long_description="Minesweeper - Python collaborative course project",
    long_description_content_type="text/markdown",
    url="https://github.com/py-collaborative-development/project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
