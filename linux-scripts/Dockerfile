FROM ubuntu:18.04
LABEL maintainer="rvtc-group"
SHELL ["/bin/bash", "-c"]
RUN \
mkdir rvtc         &&  \
cd rvtc            &&  \
echo   "set -x                       "  > envsetup.sh  &&  \
echo   "apt-get update               "  >> envsetup.sh  && \
echo   "apt-get upgrade              "  >> envsetup.sh  && \
echo                                        >> envsetup.sh  && \
echo   "apt-get -y install                 \ "  >> envsetup.sh && \
echo   "               binutils            \ "  >> envsetup.sh && \
echo   "               build-essential     \ "  >> envsetup.sh && \
echo   "               libtool texinfo     \ "  >> envsetup.sh && \
echo   "               gzip                \ "  >> envsetup.sh && \
echo   "               zip                 \ "  >> envsetup.sh && \
echo   "               unzip               \ "  >> envsetup.sh && \
echo   "               patchutils          \ "  >> envsetup.sh && \
echo   "               curl                \ "  >> envsetup.sh && \
echo   "               git                 \ "  >> envsetup.sh && \
echo   "               make                \ "  >> envsetup.sh && \
echo   "               cmake               \ "  >> envsetup.sh && \
echo   "               ninja-build         \ "  >> envsetup.sh && \
echo   "               automake            \ "  >> envsetup.sh && \
echo   "               bison               \ "  >> envsetup.sh && \
echo   "               flex                \ "  >> envsetup.sh && \
echo   "               gperf               \ "  >> envsetup.sh && \
echo   "               grep                \ "  >> envsetup.sh && \
echo   "               sed                 \ "  >> envsetup.sh && \
echo   "               gawk                \ "  >> envsetup.sh && \
echo   "               python              \ "  >> envsetup.sh && \
echo   "               bc                  \ "  >> envsetup.sh && \
echo   "               zlib1g-dev          \ "  >> envsetup.sh && \
echo   "               libexpat1-dev       \ "  >> envsetup.sh && \
echo   "               libmpc-dev          \ "  >> envsetup.sh && \
echo   "               libglib2.0-dev      \ "  >> envsetup.sh && \
echo   "               libfdt-dev          \ "  >> envsetup.sh && \
echo   "               libpixman-1-dev && \n "  >> envsetup.sh && \
echo                                            >> envsetup.sh && \
echo   "mkdir riscv                          "  >> envsetup.sh && \
echo   "cd riscv                             "  >> envsetup.sh && \
echo   "mkdir _install                       "  >> envsetup.sh && \
echo                                            >> envsetup.sh && \
echo   "# GNU STUFF                                                         "  >> envsetup.sh && \
echo   "git clone --recursive https://github.com/riscv/riscv-gnu-toolchain  "  >> envsetup.sh && \
echo   "pushd riscv-gnu-toolchain                                           "  >> envsetup.sh && \
echo   "./configure --prefix=`pwd`/../_install --enable-multilib            "  >> envsetup.sh && \
echo   "make -j`nproc`                                                      "  >> envsetup.sh && \
echo                                    >> envsetup.sh && \
echo   "# Build QEMU                 "  >> envsetup.sh && \
echo   "make -j`nproc` build-qemu    "  >> envsetup.sh && \
echo   "popd                         "  >> envsetup.sh && \
echo                                                                        >> envsetup.sh && \
echo   "# LLVM_STUFF                                                     "  >> envsetup.sh && \
echo   "git clone https://github.com/llvm/llvm-project.git riscv-llvm    "  >> envsetup.sh && \
echo   "pushd riscv-llvm                                                 "  >> envsetup.sh && \
echo   "mkdir _build                                                     "  >> envsetup.sh && \
echo   "cd _build                                                        "  >> envsetup.sh && \
echo                                                                        >> envsetup.sh && \
echo   "cmake -G Ninja                                                 \ "  >> envsetup.sh && \
echo   "  -DCMAKE_BUILD_TYPE="Release"                                 \ "  >> envsetup.sh && \
echo   "  -DBUILD_SHARED_LIBS=True                                     \ "  >> envsetup.sh && \
echo   "  -DLLVM_USE_SPLIT_DWARF=True                                  \ "  >> envsetup.sh && \
echo   "  -DCMAKE_INSTALL_PREFIX="../../_install"                      \ "  >> envsetup.sh && \
echo   "  -DLLVM_OPTIMIZED_TABLEGEN=True                               \ "  >> envsetup.sh && \
echo   "  -DLLVM_BUILD_TESTS=False                                     \ "  >> envsetup.sh && \
echo   "  -DDEFAULT_SYSROOT="../../_install/riscv64-unknown-elf"       \ "  >> envsetup.sh && \
echo   "  -DLLVM_DEFAULT_TARGET_TRIPLE="riscv64-unknown-elf"           \ "  >> envsetup.sh && \
echo   "  -DLLVM_TARGETS_TO_BUILD="RISCV"                              \ "  >> envsetup.sh && \
echo   "  ../llvm                                                        "  >> envsetup.sh && \
echo                                          >> envsetup.sh && \ 
echo   "cmake --build . --target install   "  >> envsetup.sh && \
echo   "popd                               "  >> envsetup.sh && \
chmod +x envsetup.sh