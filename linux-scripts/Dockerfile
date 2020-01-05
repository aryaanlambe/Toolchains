FROM ubuntu:18.04
LABEL maintainer="rvtc-group"

RUN set -x

# Dependencies
RUN apt-get update
RUN apt-get upgrade
RUN apt-get -y install \
               binutils \
               build-essential \
               libtool texinfo \
               gzip \
               zip \
               unzip \
               patchutils \
               curl \
               git \
               make \
               cmake \
               ninja-build \
               automake \
               bison \
               flex \
               gperf \
               grep \
               sed \
               gawk \
               python \
               bc \
               zlib1g-dev \
               libexpat1-dev \
               libmpc-dev \
               libglib2.0-dev \
               libfdt-dev \
               libpixman-1-dev


# DIRECTORY_SETUP
RUN mkdir riscv && cd riscv && mkdir _install

# GNU_STUFF
RUN git clone --recursive https://github.com/riscv/riscv-gnu-toolchain
RUN pushd riscv-gnu-toolchain
RUN ./configure --prefix=`pwd`/../_install --enable-multilib
RUN make -j`nproc`

# Build QEMU
RUN make -j`nproc` build-qemu
RUN popd

# LLVM_STUFF
RUN git clone https://github.com/llvm/llvm-project.git riscv-llvm
RUN pushd riscv-llvm
RUN mkdir _build && cd _build
RUN cmake -G Ninja -DCMAKE_BUILD_TYPE="Release" \
  -DBUILD_SHARED_LIBS=True -DLLVM_USE_SPLIT_DWARF=True \
  -DCMAKE_INSTALL_PREFIX="../../_install" \
  -DLLVM_OPTIMIZED_TABLEGEN=True -DLLVM_BUILD_TESTS=False \
  -DDEFAULT_SYSROOT="../../_install/riscv64-unknown-elf" \
  -DLLVM_DEFAULT_TARGET_TRIPLE="riscv64-unknown-elf" \
  -DLLVM_TARGETS_TO_BUILD="RISCV" \
  ../llvm
RUN cmake --build . --target install
RUN popd

