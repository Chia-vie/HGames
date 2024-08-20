import setuptools

# Read in required packages from requirements.txt
with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="HGames",
    version="0.0.0",
    author='',
    author_email='hernsteincoders@gmail.com',
    description='Games developed during Code Camp Hernstein',
    long_description='''This package is currently under development. Stay tuned for updates.''',
    url="https://github.com/Chia-vie/HGames",
    license='BSD',
    keywords='games, Python, code camp, Hernstein',
    packages=setuptools.find_packages(),
    package_data={'HGames': ['default_config.yml']},
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',
    ],
    install_requires=requirements,
    include_package_data=True
)
