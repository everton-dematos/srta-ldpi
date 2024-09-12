from setuptools import setup, find_packages

setup(
    name="srta-ldpi",
    version="1.0.0",
    description="Lightweight Deep Anomaly Detection for Network Traffic",
    long_description=open("README.md").read(),
    url="https://github.com/everton-dematos/srta-ldpi",
    packages=find_packages(),
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
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
