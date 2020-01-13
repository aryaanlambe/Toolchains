#!/usr/bin/python3.5
#Give argument 1 as installation path and argument 2 as type of toolchain
#For building gnu-riscv-toolchain give --gnu-riscv-toolchain
#For building llvm-riscv-toolchain give --llvm-riscv-toolchain

import sys
import os

argumentList = sys.argv

#Cloning and installing GNU RISCV toolchain

path = sys.argv[1]
os.mkdir(path)

type = sys.argv[2]
os.chdir(path)

if type == "--gnu-riscv-toolchain":
 clone = "git clone --recursive https://github.com/riscv/riscv-gnu-toolchain"
 os.system(clone)
 dir = path + "/riscv-gnu-toolchain/install"
 os.mkdir(dir)
 riscvdir = path + "/riscv-gnu-toolchain"
 os.chdir(riscvdir)
 configure = "./configure --prefix=" + path + "/riscv-gnu-toolchain/install --with-arch=rv32imc --with-abi=ilp32"
 make = "make -j20"

 os.system(configure)
 os.system(make)

if type == "--llvm-riscv-toolchain":
 clone = "git clone --recursive https://github.com/riscv/riscv-gnu-toolchain"
 os.system(clone)
 dir = path + "/riscv-gnu-toolchain/install"
 os.mkdir(dir)
 riscvdir = path + "/riscv-gnu-toolchain"
 os.chdir(riscvdir)
 configure = "./configure --prefix=" + path + "/riscv-gnu-toolchain/install --with-arch=rv32imc --with-abi=ilp32"
 make = "make -j20"

 os.system(configure)
 os.system(make)

 clone = "git clone https://github.com/llvm/llvm-project.git"
 os.system(clone)
 dir1 = path + "/llvm-project/install"
 dir2 = path + "/llvm-project/build"
 os.mkdir(dir1)
 os.mkdir(dir2)
 os.chdir(dir1)
 configure = "cmake -G Ninja -DCMAKE_BUILD_TYPE=\"Release\" -DCMAKE_INSTALL_PREFIX=\"" + path + "/llvm-project/install\" -DBUILD_SHARED_LIBS=True -DLLVM_USE_SPLIT_DWARF=True -DLLVM_OPTIMIZED_TABLEGEN=True -DLLVM_BUILD_TESTS=True -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=\"RISCV\" -DLLVM_ENABLE_PROJECTS=\"clang;lld;\" -DDEFAULT_SYSROOT=\"" + path + "/riscv-gnu-toolchain/install/riscv32-unknown-elf\" -DGCC_INSTALL_PREFIX=\"" + path + "/riscv-gnu-toolchain/install\" -DLLVM_DEFAULT_TARGET_TRIPLE=\"riscv32-unknown-elf\" ../llvm"
 make = "cmake --build . --target install"

 os.system(configure)
 os.system(make)
