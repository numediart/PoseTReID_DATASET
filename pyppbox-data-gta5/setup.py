# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                           #
#   Code: MIT License                                                       #
#                                                                           #
#   Dataset: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)        #
#                                                                           #
#   Copyright (c) 2023 Ratha SIV                                            #
#                                                                           #
#   pyppbox-data-gta5: The restructured GTA_V_DATASET for pyppbox V3.       #
#                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from setuptools import setup

def main():

    long_description = open("README.md", encoding="utf-8").read()

    packages = ["pyppbox.data.datasets.GTA_V_DATASET"]
    package_data = {"pyppbox.data.datasets.GTA_V_DATASET": ["*"]}

    setup(
        name="pyppbox-data-gta5",
        version="2.0",
        url="https://github.com/rathaumons/PoseTReID_DATASET",
        license="MIT",
        description="The restructured GTA_V_DATASET for pyppbox V3.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=packages,
        package_data=package_data,
        include_package_data=True,
        author="Ratha SIV",
        maintainer="rathaROG",
        install_requires=None,
        python_requires=">=3.8",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Information Technology",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Software Development",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS",
        ],
    )

if __name__ == "__main__":
    main()
