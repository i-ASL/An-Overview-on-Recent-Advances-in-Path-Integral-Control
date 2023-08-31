from setuptools import setup
import os
from glob import glob 
package_name = 'autonomous_tb3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'world/maze'), glob('world/maze/*')),
        (os.path.join('share', package_name, 'world/hotel'), glob('world/hotel/*')),
        (os.path.join('share', package_name, 'models/table'), glob('models/table/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kazim',
    maintainer_email='kazim@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'occupancy_grid_pub = autonomous_tb3.occupancy_grid_pub:main',
            'sdf_spawner = autonomous_tb3.spawn_entity:main',
            'maze_solver = autonomous_tb3.maze_solver:main',
            'autonomous_waiter_lite = autonomous_tb3.hotel_waiter_single_button:start_app',
            'autonomous_waiter = autonomous_tb3.hotel_waiter_multi_button:start_app'
        ],
    },
)