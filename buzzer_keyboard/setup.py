from setuptools import find_packages, setup

package_name = 'buzzer_keyboard'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Henry Ilviro',
    maintainer_email='your_email@example.com',
    description='Sistem Kendali Buzzer ROS2 dengan Keyboard Input - Proyek Robotika Medis',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_publisher = buzzer_keyboard.keyboard_publisher:main',
            'buzzer_subscriber = buzzer_keyboard.buzzer_subscriber:main',
        ],
    },
)
