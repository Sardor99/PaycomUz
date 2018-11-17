import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PaycomUz",
    version="0.2",
    author="Sadullayev Bekhzod",
    author_email="begymrx@gmail.com",
    description="Django-RestFrameWork-PaycomUz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/begyy/PaycomUz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
