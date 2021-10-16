def setup_package():
    metadata = dict(
        name="identity",
        packages=["identity"],
        version="1.0",

        description="It is a small library for solving some mathematical alliances and some mathematical instructions such as factorial",
        author="mahdiyavari",
        author_email="mahdiyyv@gmail.com",
        url="https://github.com/mahdiyyv117/identity",
        keywords=[
            "اتحاد",
            "identity",

        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6",
    )
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
