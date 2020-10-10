from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='classdojo',
    version='0.0.1',
    description='Tools to get points from the classdojo point system',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Toby Johnson',
    author_email='toby.e.m.Johnson@gmail.com',
    keywords=['Classdojo', 'Dojo', 'Class Points'],
    url='https://github.com/fishbigger/classdojo',
    download_url='https://pypi.org/project/classdojo/'
)

install_requires = [
    'requests==2.24.0',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)