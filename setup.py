from setuptools import setup, find_packages

setup(
    name='photoencryption',
    packages=find_packages(),
    version='0.0.10',
    description='Encrypting and decrypting messages from images',
    author='Bruno Faliszewski',
    license='MIT',
    install_requires=['pillow', 'numpy'],
)