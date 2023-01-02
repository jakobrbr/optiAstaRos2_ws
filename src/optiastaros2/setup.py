from setuptools import setup

package_name = 'optiastaros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('lib/' + package_name, [package_name+'/NatNetClient.py']),
        ('lib/' + package_name, [package_name+'/purePursuit.py']),
        ('lib/' + package_name, [package_name+'/generateRobotPath.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='jakobrb@outlook.dk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pubdata_node = optiastaros2.pubdata_node:main',
            'controller_node = optiastaros2.controller_node:main'
        ],
    },
)
