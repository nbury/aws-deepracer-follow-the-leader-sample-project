from setuptools import setup
import os

package_name = 'aws_uploader_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), ['launch/aws_uploader_pkg_launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nbury',
    maintainer_email='nbury@gwu.edu',
    description='Uploads image data to aws',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aws_uploader_node = aws_uploader_pkg.aws_uploader_node:main'
        ],
    },
)
