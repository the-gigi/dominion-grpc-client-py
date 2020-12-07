from setuptools import setup

setup(name='dominion-grpc-client',
      version='0.8.0',
      url='https://github.com/the-gigi/dominion-grpc-client-py',
      license='MIT',
      author='Gigi Sayfan',
      author_email='the.gigi@gmail.com',
      description='Dominion gRPC client library',
      packages=['dominion_grpc_client'],
      python_requires='>=3.8',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      zip_safe=False)
