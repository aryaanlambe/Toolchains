If interested in building custom toolchain using binutils,gcc,and a library[categorization based on library used] from source.
Content below:
1. Build gcc with musl library
2. Build gcc with newlib library

1) Build gcc with musl library
Follow link[1] this is  similar to riscv_gnu_toolchain[2] where in simple steps you can build the toolchain.

2) Build gcc with newlib library
    
1. Create empty directory
2. Untar attached tar file to above folder.
3. Download sources from github
    git clone https://github.com/riscv/riscv-gcc.git
    git clone https://github.com/riscv/riscv-binutils-gdb
    git clone https://github.com/riscv/riscv-newlib
4. In runall.sh set $PREFIX to <where you want final toolchain>
5. run as ./runall.sh


Resource:[3]

If anything fails, please revert on list we will try solving it.
[1]https://colematt.github.io/2018/11/26/building-llvm-for-riscv-cross-compilation.html

Links:
[1]https://github.com/richfelker/musl-cross-make
[2]https://github.com/riscv/riscv-gnu-toolchain
[3]http://www.ifp.illinois.edu/~nakazato/tips/xgcc.html
