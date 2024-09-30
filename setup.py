from setuptools import setup, find_packages

setup(
    name="srta-ldpi",
    version="1.0",
    description="Lightweight Deep Anomaly Detection for Network Traffic",
    long_description=open("README.md").read(),
    url="https://github.com/everton-dematos/srta-ldpi",
    packages=find_packages(include=["ldpi", "ldpi.training", "sniffer"]),
    py_modules=["main", "main_debug", "options", "utils"],
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'scikit-learn',
        'torch',
        'matplotlib',
        'dpkt',
        'tqdm',
        'cycler',
        'netifaces',
        'systemd',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.11',
    include_package_data=True, 
    package_data={
        "ldpi.training": [
            "output/ResCNN/*.pth"
        ],
    },
    zip_safe=False, 
)