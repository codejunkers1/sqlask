from distutils.core import setup
import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='sqlask',
  version='1.0.0',
  description='lightweight python framework for webapplications',
  url='http://github.com/codejunker1/sqlask',
  author='Venkata Sai Katepalli',
  author_email='venkatasaisoft@gmail.com',
  license='MIT',
  scripts=['sqlask/bin/sqlask'],
  entry_points = {
      'console_scripts': ['sqlask=sqlask.core.management:main'],
  },
  packages=find_packages(),
  install_requires=[
		'flasgger==0.8.0',
    'Flask==0.12.2',
    'Flask-Cors==3.0.3',
    'Flask-JWT==0.3.2',
    'Flask-RESTful==0.3.6',
    'marshmallow==2.15.0',
    'bcrypt==3.1.4',
    'pandas==0.23.0'
	],
	include_package_data=True,
	zip_safe=False
)