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

def ver(major=0):  # , increment=False):
    """Dated versioning for pypi."""
    import git
    obj = git.Repo()
    last_tag = obj.git.describe()
    # if not increment:
    #     return last_tag.split("-")[0]

    minor = int(last_tag.split(".")[1].split("+")[0]) + 1
    d = obj.head.object.committed_datetime
    ms = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    # t = (d.hour * 60 * 12) + (d.minute * 12) + d.second // 5
    # res, rem = divmod(t, 26 * 26)
    # time = f"{chr(res + 97)}"
    # res, rem = divmod(rem, 26)
    # time += f"{chr(res + 97)}{chr(rem + 97)}"
    tag = f"{major}.{minor}+{d.year - 2000}{ms[d.month]}{str(d.day).rjust(2, '0')}"
    # if tag not in obj.tags:
    #     obj.create_tag(tag, message="Autoversioned tag from setup")  # <- not working inside githubworkflow
    # obj.remotes.origin.push(tag)
    return tag


if __name__ == "__main__":
    print(ver())  # increment=True))
