import setuptools
import git
import datetime

repo = git.Repo(search_parent_directories=True)
commit_hash = repo.head.object.hexsha[:8]
date = datetime.datetime.utcnow().isoformat()[:10]

setuptools.setup(
    name="dota_webscraper",
    version=f"{date}_{commit_hash}",
    description="",
    author="Alex Pickering",
    author_email="",
    url="https://github.com/alexpickering/dota_webscraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[req.strip() for req in open("requirements.txt").readlines() if req.strip()]
)
