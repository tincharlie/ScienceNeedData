from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='datasciencelibrary',
  version='0.0.1',
  description='Contains replacer, model builder, cv tune, visualization etc libraries present.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Vipul Shukla',
  author_email='vipulshukla999@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='replacer', 
  packages=find_packages(),
  install_requires=[''] 
)
