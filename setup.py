from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="grover-visualizer",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "qiskit>=1.0.0",
        "qiskit-aer>=0.13.0",
        "qiskit-ibm-runtime>=0.17.0",
        "matplotlib>=3.7.0",
        "numpy>=1.24.0"
    ],
    author="Silent Sword",
    description="Visualize Grover's Algorithm with quantum state animations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SilentSword123456/Groovers_Algorithm-Quantum",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)