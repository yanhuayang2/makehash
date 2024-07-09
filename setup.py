from setuptools import setup, find_packages

setup(
    name='makehash',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
    ],
)

'''
python setup.py sdist bdist_wheel
这将在 dist/ 目录下生成一个 .tar.gz 文件和一个 .whl 文件
'''