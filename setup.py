from setuptools import setup, find_packages

setup(
    name="path_finding_2d",
    version="1.0.0",
    author="tbogard",
    author_email="",
    description="",
    packages= find_packages(
        include=["lib",'lib*']
        ),
    include_package_data=True,
    python_requires=">=3.11",
)
