# pyav
pyav implements bindings for the [ffmpeg](https://ffmpeg.org) libraries. We aim to provide all of the power and control of the underlying library, but manage the gritty details as much as possible.

---
[![Actions Status](https://github.com/WyattBlue/PyAV/workflows/tests/badge.svg)](https://github.com/wyattblue/PyAV/actions?workflow=tests)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

pyav is for direct and precise access to your media via containers, streams, packets, codecs, and frames. It exposes a few transformations of that data, and helps you get your data to/from other packages (e.g. Numpy and Pillow).

This power does come with some responsibility as working with media is horrendously complicated and pyav can't make all the best decisions for you. If the `ffmpeg` cli does the job without you bending over backwards, use it. pyav is much more complicated than the standalone `ffmpeg` program.

## Installing
Just run:
```
pip install pyav
```

Running the command should install the binary wheel provided. Due to the complexity of the dependencies, pyav is not easy to install from source. If you want to try your luck anyway, you can run:

```
pip install pyav --no-binary pyav
```

And if you want to build the absolute latest (POSIX only):

```bash
git clone https://github.com/WyattBlue/pyav.git
cd pyav

source scripts/activate.sh
pip install -U -r tests/requirements.txt
./scripts/build-deps
make
deactivate
pip install .
```

## About
pyav is a friendly fork of [PyAV](https://github.com/PyAV-Org/PyAV) made by a PyAV maintainer. pyav offers bleeding-edge features in exchange for requiring more up to date Python and FFmpeg versions.
