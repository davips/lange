#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the hange project.
#  Please respect the license - more about this in the section (*) below.
#  #
#  hange is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  #
#  hange is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  #
#  You should have received a copy of the GNU General Public License
#  along with hange.  If not, see <http://www.gnu.org/licenses/>.
#  #
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.

major = 0


def ver(increment=0):
    """Dated versioning for pypi."""
    import git
    obj = git.Repo()
    last_tag = obj.git.describe()
    minor = int(last_tag.split(".")[1].split("+")[0]) + increment
    d = obj.head.object.committed_datetime
    ms = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    # t = (d.hour * 60 * 12) + (d.minute * 12) + d.second // 5
    # res, rem = divmod(t, 26 * 26)
    # time = f"{chr(res + 97)}"
    # res, rem = divmod(rem, 26)
    # time += f"{chr(res + 97)}{chr(rem + 97)}"
    tag = f"{major}.{minor}+{d.year - 2000}{ms[d.month]}{str(d.day).rjust(2, '0')}"
    if tag not in obj.tags:
        obj.create_tag(tag, message="Autoversioned tag from setup")  # <- not working inside githubworkflow
        obj.remotes.origin.push(tag)
    return tag


if __name__ == "__main__":
    print(ver(1))
    exit()

import setuptools

NAME = "hange"

VERSION = ver()

AUTHOR = 'Davi Pereira-Santos'

AUTHOR_EMAIL = 'dpsabc@gmail.com'

DESCRIPTION = 'Haskell-like intervals for Python'

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

LICENSE = 'GPL3'

URL = 'https://github.com/davips/hange'

DOWNLOAD_URL = 'https://github.com/davips/hange/releases'

CLASSIFIERS = ['Intended Audience :: Science/Research',
               'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
               'Natural Language :: English',
               'Programming Language :: Python',
               'Topic :: Scientific/Engineering',
               # posix               'Operating System :: Linux',
               'Programming Language :: Python :: 3.8']

INSTALL_REQUIRES = [
]

EXTRAS_REQUIRE = {
}

SETUP_REQUIRES = ['wheel', 'gitpython']

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=CLASSIFIERS,
    description=DESCRIPTION,
    download_url=DOWNLOAD_URL,
    extras_require=EXTRAS_REQUIRE,
    install_requires=INSTALL_REQUIRES,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    packages=setuptools.find_packages(),
    setup_requires=SETUP_REQUIRES,
    url=URL,
)

package_dir = {'': 'hange'}  # For IDEs like Intellij to recognize the package.
