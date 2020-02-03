## Run any program using qemu riscv linux

### Get the scripts:
```sh
git clone https://github.com/hiraditya/Toolchains.git
```

### Setup docker1:
Use https://github.com/hiraditya/Toolchains/blob/master/users/rc/envsetup

Provide symlinks at the end such that
```sh
/usr/bin/riscv-cc -> your_newly_built_riscv_c_cross-compiler
/usr/bin/riscv-cxx -> your_newly_built_riscv_cxx_cross-compiler
```

## Setup docker2:
```sh
docker pull reshabhsh/riscv-linux:latest
docker run -it --privileged reshabhsh/riscv-linux:latest 

# You are now inside the docker container

# Use ifconfig to find ip, netmask, gateway and broadcast
# Say the ip was 172.17.0.4, save a new ip say N_IP which differs 
# from the original ip but is on the same subnet example
# 172.17.0.3 or 172.17.0.5

# We have 5 variables now (find the examples below)
# IP = 172.17.0.4
# NETMASK = 255.255.0.0
# BROADCAST = 172.17.255.255
# GATEWAY = 172.17.0.1
# N_IP = 172.17.0.5

# Update /busybear-linux/etc/network/interfaces with the values we
# found but use the new ip (N_IP)

brctl addbr virbr0
tunctl -t tap0
brctl addif virbr0 eth0
brctl addif virbr0 tap0

ifconfig eth0 up
ifconfig tap0 up
ifconfig virbr0 up

ifconfig virbr0 $IP/16 # IP is the original IP
ifconfig eth0 0.0.0.0 promisc

route add default gw  $GATEWAY 
cd /proc/sys/net/bridge
for f in bridge-nf-*; do echo 0 > $f; done
cd /

bash image.sh

# Username: root
# Password: busybear

# From the host run riscv-compiler
# Get script -> https://github.com/hiraditya/Toolchains/blob/master/users/reshabh/riscv-compiler
# Usage: riscv-compiler container1 container2 file.c
```
