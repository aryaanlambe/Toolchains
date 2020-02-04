## Run any program using qemu riscv linux

### Get the scripts:
```sh
git clone https://github.com/hiraditya/Toolchains.git
```

### Setup docker1 and docker2:
Use https://github.com/hiraditya/Toolchains/blob/master/users/rc/envsetup

Provide symlinks at the end in docker1 container such that:
```sh
/usr/bin/riscv-cc -> your_newly_built_riscv_c_cross-compiler
/usr/bin/riscv-cxx -> your_newly_built_riscv_cxx_cross-compiler
```
```sh
python3 envsetup --llvm -mp /home/opt/docker_home --setup_exe
```

### Running c/cpp sources using the wrapper script
Use https://github.com/hiraditya/Toolchains/blob/master/riscv-compiler.py

```sh
python3 riscv-compiler.py --toolchain-container docker1 --execution-container docker2  file.c file1.c file2.c -o riscv.out -O3
```

