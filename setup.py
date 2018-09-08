from distutils.core import setup
import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='sqlask',
  version='0.1',
  description='lightweight python framework for webapplications',
  url='http://github.com/codejunker1/sqlask',
  author='Venkata Sai Katepalli',
  author_email='venkatasaisoft@gmail.com',
  license='MIT',
  scripts=['sqlask/bin/sqlask'],
  entry_points = {
      'console_scripts': ['sqlask=sqlask.core.managment:main'],
  },
  packages=find_packages(),
  install_requires=[
		'markdown',
	],
	include_package_data=True,
	zip_safe=False
)