import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shopstyle_api",
    version="0.0.5",
    author="aorzh",
    author_email="al.orzh@gmail.com",
    description="API client for Shopstylecollective",
    long_description=long_description,
    url="https://github.com/aorzh/shopstyle_api",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
