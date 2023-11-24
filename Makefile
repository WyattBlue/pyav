LDFLAGS ?= ""
CFLAGS ?= "-O0"

PYAV_PYTHON ?= python
PYTHON := $(PYAV_PYTHON)

.PHONY: default build fate-suite test clean-build clean-src clean test
default: build

build:
	CFLAGS=$(CFLAGS) LDFLAGS=$(LDFLAGS) $(PYTHON) setup.py build_ext --inplace --debug

fate-suite:
	# Grab ALL of the samples from the ffmpeg site.
	rsync -vrltLW rsync://fate-suite.ffmpeg.org/fate-suite/ tests/assets/fate-suite/

test:
	$(PYTHON) setup.py test

clean-build:
	- rm -rf build
	- find av -name '*.so' -delete

clean-src:
	- rm -rf src

clean: clean-build clean-src
