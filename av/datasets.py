from urllib.request import urlopen
import errno
import logging
import os
import sys


log = logging.getLogger(__name__)


def iter_data_dirs(check_writable: bool = False):
    try:
        yield os.environ["PYAV_TESTDATA_DIR"]
    except KeyError:
        pass

    if os.name == "nt":
        yield os.path.join(sys.prefix, "pyav", "datasets")
        return

    bases = [
        "/usr/local/share",
        "/usr/local/lib",
        "/usr/share",
        "/usr/lib",
    ]

    # Prefer the local virtualenv.
    if hasattr(sys, "real_prefix"):
        bases.insert(0, sys.prefix)

    for base in bases:
        dir_ = os.path.join(base, "pyav", "datasets")
        if check_writable:
            if os.path.exists(dir_):
                if not os.access(dir_, os.W_OK):
                    continue
            else:
                if not os.access(base, os.W_OK):
                    continue
        yield dir_

    yield os.path.join(os.path.expanduser("~"), ".pyav", "datasets")


def cached_download(url: str, name: str) -> str:
    """Download the data at a URL, and cache it under the given name.

    The file is stored under `pyav/test` with the given name in the directory
    :envvar:`PYAV_TESTDATA_DIR`, or the first that is writeable of:

    - the current virtualenv
    - ``/usr/local/share``
    - ``/usr/local/lib``
    - ``/usr/share``
    - ``/usr/lib``
    - the user's home

    """

    clean_name = os.path.normpath(name)
    if clean_name != name:
        raise ValueError(f"{name} is not normalized.")

    for dir_ in iter_data_dirs():
        path = os.path.join(dir_, name)
        if os.path.exists(path):
            return path

    dir_ = next(iter_data_dirs(True))
    path = os.path.join(dir_, name)

    log.info(f"Downloading {url} to {path}")

    response = urlopen(url)
    if response.getcode() != 200:
        raise ValueError(f"HTTP {response.getcode()}")

    dir_ = os.path.dirname(path)
    try:
        os.makedirs(dir_)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    tmp_path = path + ".tmp"
    with open(tmp_path, "wb") as fh:
        while True:
            chunk = response.read(8196)
            if chunk:
                fh.write(chunk)
            else:
                break

    os.rename(tmp_path, path)

    return path


def fate(name: str) -> str:
    return cached_download(
        f"http://fate.ffmpeg.org/fate-suite/{name}",
        os.path.join("fate-suite", name.replace("/", os.path.sep)),
    )


def curated(name: str) -> str:
    return cached_download(
        f"https://pyav.org/datasets/{name}",
        os.path.join("pyav-curated", name.replace("/", os.path.sep)),
    )
