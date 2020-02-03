#!/bin/bash
cd $TOP
git clone https://github.com/llvm/llvm-project.git
cd $TOP/llvm-project
mkdir build install && export LLVM_INSTALL_ROOT=$(pwd)/install
cd build
cmake -G Ninja \
  -DCMAKE_BUILD_TYPE="Release" \
  -DCMAKE_INSTALL_PREFIX="$LLVM_INSTALL_ROOT" \
  -DBUILD_SHARED_LIBS=True \
  -DLLVM_USE_SPLIT_DWARF=True \
  -DLLVM_OPTIMIZED_TABLEGEN=True \
  -DLLVM_BUILD_TESTS=True \
  -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD="RISCV" \
  -DLLVM_ENABLE_PROJECTS="clang;lld;" \
  -DDEFAULT_SYSROOT="$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT/riscv32-unknown-elf" \
  -DGCC_INSTALL_PREFIX="$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT" \
  -DLLVM_DEFAULT_TARGET_TRIPLE="riscv32-unknown-elf" \
  ../llvm
cmake --build . --target install
#comment if want to skip testing
cmake --build . --target check-all

