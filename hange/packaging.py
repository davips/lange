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
from hange import version
import git

major = 0
if __name__ == "__main__":
    minor = int(version.split(".")[2]) + 1
    obj = git.Repo()
    d = obj.head.object.committed_datetime
    # ms = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    tag = f"{major}.{d.year - 2000}{str(d.month).rjust(2, '0')}.{minor}"
    with open("hange/__init__.py", "r") as f:
        txt = f.readlines()
    with open("hange/__init__.py", "w") as f:
        for l in txt:
            if "version = " in l:
                l = f'version = "{tag}"\n'
            f.write(l)
    if tag not in obj.tags:
        obj.create_tag(tag, message=f"Autoversioned tag from setup\n{d}")  # <- not working inside githubworkflow
    obj.remotes.origin.push(tag)
    print(tag)

# t = (d.hour * 60 * 12) + (d.minute * 12) + d.second // 5
# res, rem = divmod(t, 26 * 26)
# time = f"{chr(res + 97)}"
# res, rem = divmod(rem, 26)
# time += f"{chr(res + 97)}{chr(rem + 97)}"
