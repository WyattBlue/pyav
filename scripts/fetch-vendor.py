from struct import calcsize
import argparse
import os
import platform
import shutil
import subprocess


def get_url():
    system = platform.system()
    machine = platform.machine()

    if system == "Linux":
        plat = f"manylinux_{machine}"

    elif system == "Darwin":
        # cibuildwheel sets ARCHFLAGS:
        # https://github.com/pypa/cibuildwheel/blob/5255155bc57eb6224354356df648dc42e31a0028/cibuildwheel/macos.py#L207-L220
        if "ARCHFLAGS" in os.environ:
            machine = os.environ["ARCHFLAGS"].split()[1]
        plat = f"macosx_{machine}"

    elif system == "Windows":
        plat = "win_amd64" if calcsize("P") * 8 == 64 else "win32"
    else:
        raise Exception(f"Unsupported system {system}")

    return f"https://github.com/WyattBlue/pyav-ffmpeg/releases/download/6.1-2/ffmpeg-{plat}.tar.gz"


parser = argparse.ArgumentParser(description="Fetch and extract tarballs")
parser.add_argument("destination_dir")
parser.add_argument("--cache-dir", default="tarballs")
args = parser.parse_args()

print(f"Creating directory {args.destination_dir}")
if os.path.exists(args.destination_dir):
    shutil.rmtree(args.destination_dir)
os.makedirs(args.destination_dir)

tarball_url = get_url()
tarball_name = tarball_url.split("/")[-1]
tarball_file = os.path.join(args.cache_dir, tarball_name)

if not os.path.exists(tarball_file):
    print(f"Downloading {tarball_url}")
    if not os.path.exists(args.cache_dir):
        os.mkdir(args.cache_dir)
    subprocess.run(
        ["curl", "--location", "--output", tarball_file, "--silent", tarball_url]
    )

print(f"Extracting {tarball_name}")
subprocess.run(["tar", "-C", args.destination_dir, "-xf", tarball_file])
