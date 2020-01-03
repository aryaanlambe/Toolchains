#Cloning and installing GNU RISCV toolchain

export TOP=$(pwd)
export RISCV_GNU_TOOLCHAIN_INSTALL_ROOT=/$TOP/riscv-gnu-toolchain/install
export LLVM_INSTALL_ROOT=/$TOP/llvm-project/install

cd $TOP
git clone --recursive https://github.com/riscv/riscv-gnu-toolchain
cd riscv-gnu-toolchain
mkdir install && export RISCV_GNU_TOOLCHAIN_INSTALL_ROOT=$(pwd)/install
./configure --prefix=$RISCV_GNU_TOOLCHAIN_INSTALL_ROOT --with-arch=rv32imc --with-abi=ilp32
make -j20

#Cloning and installing LLVM for RISCV target

cd $TOP
git clone https://github.com/llvm/llvm-project.git
cd $TOP/llvm-project
git reset --hard llvmorg-7.0.1
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


