from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='c_out',
    packages=['c_out'],
    description='Colored Output - c_out. Python print with a style!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.3',
    license='GPL-3.0',
    author="Gautam Rajeev Singh",
    author_email='gautamsingh1997@gmail.com',
    url='https://github.com/singhgautam7/Python-GoldMine/tree/master/beauty_print',
    keywords='pyton print color styles',
    install_requires=[],
)
