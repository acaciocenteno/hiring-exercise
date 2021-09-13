from setuptools import setup

setup(
    name='sales_consolidator',
    version='0.1.0',
    py_modules=['revenue'],
    install_requires=[
        'Click',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'revenue = revenue',
        ],
    },
)