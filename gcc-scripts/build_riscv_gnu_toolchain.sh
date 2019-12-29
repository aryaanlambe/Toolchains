#!/bin/bash
cd $TOP
git clone --recursive https://github.com/riscv/riscv-gnu-toolchain
cd riscv-gnu-toolchain
mkdir install && export RISCV_GNU_TOOLCHAIN_INSTALL_ROOT=$(pwd)/install
./configure --prefix=$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT --with-arch=rv32imc --with-abi=ilp32
make -j16


