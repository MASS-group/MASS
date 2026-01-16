from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mass-pkdv",  # PyPI 上的包名
    version="0.1.0",
    author="MASS-group",
    author_email="",
    description="Product Kernel Density Visualization (pKDV) algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MASS-group/MASS",
    packages=find_packages(),  # 自动查找 mass_pkdv 包
    include_package_data=True,
    package_data={
        "mass_pkdv": ["bin/mass_pkdv.exe"]
    },
    python_requires=">=3.7",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
