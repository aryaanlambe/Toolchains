#!/bin/bash
#Please set $TOP first, see below
# and then run using
# ./runall.sh

#usage: Builds riscv-gnu-toolchain, builds LLVM with sysroot as riscv-gnu-toolchain
#compiles C program, and finally tries to run it, which on other than riscv architecture shold throw error.

#NOTE: Script takes considerable amount of time, as we are building everything from source.
#Resource:
# https://colematt.github.io/2018/11/26/building-llvm-for-riscv-cross-compilation.html
#####################ENV VARIABLES###########################

#export TOP=$(pwd)
export TOP=<PATH WHERE YOU WANT CROSS COMPILER>>
export RISCV_GNU_TOOLCHAIN_INSTALL_ROOT=/$TOP/riscv-gnu-toolchain/install
export LLVM_INSTALL_ROOT=/$TOP/llvm-project/install

################################################
echo "START ALL"
echo "VARIABLES ALREADY SET"
echo "riscv gnu-toolchain"
../gcc-scripts/build_riscv_gnu_toolchain.sh > log_riscv_gnu_toolchains.log 2>&1
echo  "riscv-gnu-toolchains done"

echo "build llvm riscv"
../llvm-scripts/llvm_build.sh > log_llvm_riscv.log 2>&1
echo "build llvm riscv done"
echo "Testing compiler version"
$LLVM_INSTALL_ROOT/bin/clang   --sysroot=$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT/riscv32-unknown-elf   --gcc-toolchain=$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT   --target=riscv32-unknown-elf -v


echo "#include<stdio.h>" > check.c
echo "int main (){puts(\"SUCCESS\");}" >> check.c

echo "Checking executable "
$LLVM_INSTALL_ROOT/bin/clang   --sysroot=$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT/riscv32-unknown-elf   --gcc-toolchain=$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT   --target=riscv32-unknown-elf $TOP/examples/check.c
./a.out
err=$?
if [ "$err" -ne "0" ]; then
   echo "Unsuccessful...";
fi

return $err
