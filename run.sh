set -eux
docker build --tag imageio-segfault .
docker run --rm imageio-segfault python segfault.py