from setuptools import setup,find_packages
setup(name="nullsec-ducky-payloads",version="2.0.0",author="bad-antics",description="Hak5 USB Rubber Ducky payload collection and builder",packages=find_packages(where="src"),package_dir={"":"src"},python_requires=">=3.8")
