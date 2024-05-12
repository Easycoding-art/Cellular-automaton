from setuptools import setup, find_packages
setup(
    name='cell_automat', 
	version='1.0', 
	description='Working with cell automats and creating video effects based on them', 
	author='Easycoding-Art',
    packages=find_packages(),
	install_requires=[ 
		'pygame', 
		'numpy',
        'moviepy',
        'Pillow'
	]
) 
