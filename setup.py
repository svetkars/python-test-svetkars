from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='CMD user management utility',
    long_description=readme,
    author='Svetlana Karslioglu',
    author_email='svetlana.karslioglu@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'hr=hr.cli:main',
    },
)
