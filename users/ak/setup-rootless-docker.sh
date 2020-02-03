# From: https://www.slideshare.net/AkihiroSuda/dockercon-2019-hardening-docker-daemon-with-rootless-mode
#       https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo
#       https://www.katacoda.com/courses/docker/rootless
apt-get install -y uidmap
sudo apt install libseccomp-dev

# Build and install slirp4netns from source or directly from binary
git clone https://github.com/rootless-containers/slirp4netns.git

# Install slirp4netns and add to PATH
# Setup Docker env variables.
export XDG_RUNTIME_DIR=/tmp/docker-1001
export PATH=/home/hiraditya/bin:$PATH
export DOCKER_HOST=unix:///run/user/1000/docker.sock
docker run -it ubuntu bash
