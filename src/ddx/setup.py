from setuptools import setup

setup(name='ddx',
      version='0.1.0',
      description='DDX',
      url='https://github.com/LcsH0s',
      author='LcsH0s',
      author_email='N/A',
      license='MIT',
      packages=['error', 'manager', 'container'],
      install_requires=[
          'docker',
      ],
      zip_safe=False)
