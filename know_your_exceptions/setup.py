from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='know_your_exceptions',
    description='Identitfy the exact exception class',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.3',
    license='MIT',
    author="Gautam Rajeev Singh",
    author_email='gautamsingh1997@gmail.com',
    url='https://github.com/singhgautam7/Python-GoldMine/tree/master/know_your_exceptions',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    keywords='pyton print color styles',
    python_requires=">=3.0",
    install_requires=[],
)
