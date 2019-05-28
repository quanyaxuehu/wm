from setuptools import setup

setup(
    name='wm',
    version='1.0',
    packages=['wm', 'wm.commands'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        wm=wm.cli:cli
    ''',
)
