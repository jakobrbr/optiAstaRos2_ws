from setuptools import find_packages
from setuptools import setup

setup(
    name='rigidbody_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('rigidbody_msgs', 'rigidbody_msgs.*')),
)
