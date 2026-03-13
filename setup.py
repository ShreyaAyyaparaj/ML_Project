from setuptools import find_packages, setup

def get_requirements(file_path):
    requirements = []

    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()

            # ignore editable install
            if req.startswith("-e"):
                continue

            requirements.append(req)

    return requirements


setup(
    name="Mlproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
