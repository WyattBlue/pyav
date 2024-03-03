# pyav

Notice: [PyAV](https://github.com/PyAV-Org/PyAV) (upstream) and pyav have been merged! There is no reason to use `pyav` unless you want LGPLv3 builds!

---
[![Actions Status](https://github.com/WyattBlue/PyAV/workflows/tests/badge.svg)](https://github.com/wyattblue/PyAV/actions?workflow=tests)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

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

Notice: `av` and `pyav` have been merged, there is no reason to use `pyav` for source builds!
