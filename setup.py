import setuptools

with open("README.MD","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PayMe",
    version="0.0.1",
    author="Sadullayev Bekhzod",
    author_email="begymrx@gmail.com",
    description="Django_rest_frame_work_pay_me",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/begyy/PayMe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)