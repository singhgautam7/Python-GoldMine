from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sick-dict',
    description='SickDict - An IDE-friendly python dictionary',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1',
    license='MIT',
    author="Gautam Rajeev Singh",
    author_email='gautamsingh1997@gmail.com',
    url='https://github.com/singhgautam7/Python-GoldMine/tree/master/sick_dict',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    keywords='pyton dictionary dict json',
    python_requires=">=3.0",
    install_requires=[],
)
