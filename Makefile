#
# This file is part of ${project.title}.

# ${project.title} is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# ${project.title} is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with ${project.title}.  If not, see <http://www.gnu.org/licenses/>.

PYTHON = python
SETUP = $$(PYTHON) setup.py
LINT = flake8


all: build

build:
	$$(SETUP) build

devel:
	$$(SETUP) develop

clean:
	rm -rf build html *.egg-info _trial_temp

test:
	@$$(SETUP) test

lint:
	@$$(LINT) .

html:
	sphinx-build -b html docs html

.PHONY: build html
