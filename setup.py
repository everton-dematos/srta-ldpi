from setuptools import setup, find_packages

setup(
    name="srta-ldpi",
    version="1.0",
    description="Lightweight Deep Anomaly Detection for Network Traffic",
    long_description=open("README.md").read(),
    url="https://github.com/everton-dematos/srta-ldpi",
    packages=find_packages(include=["ldpi", "ldpi.*", "sniffer"]),
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
            "output/ResCNN/*.pth",
            "output/ResCNN/plots/*.pdf",
        ],
    },
    data_files=[
        ("ldpi/training", [
            "ldpi/training/data.py",
            "ldpi/training/losses.py",
            "ldpi/training/model.py",
            "ldpi/training/plots.py",
            "ldpi/training/preprocessing.py",
            "ldpi/training/training.py",
            "ldpi/training/transforms.py",
            "ldpi/training/output/ResCNN/best_model_with_center.pth",
            "ldpi/training/output/ResCNN/pretrained_model.pth",
            "ldpi/training/output/ResCNN/scripted_quantized_model.pth",
            "ldpi/training/output/ResCNN/traced_model.pth",
            "ldpi/training/output/ResCNN/plots/hundred_one.pdf",
            "ldpi/training/output/ResCNN/plots/max.pdf",
            "ldpi/training/output/ResCNN/plots/near_max.pdf",
            "ldpi/training/output/ResCNN/plots/ninety_nine.pdf"
        ])
    ],
    zip_safe=False,
)