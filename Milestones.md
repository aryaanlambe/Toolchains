# Milestones

## Milestone 1:
- End to end compile and run infra.
  - Ability to build a toolchain from a script. The script should only take flags like path to install directory, toolchain-type etc.
  - Ability to run self contained programs inside of a qemu.
  - A risc-v qemu that is to be used by all contributors.
  - A docker based fully reproducible compile and run framework.

## Milestone 2:
- Benchmarking, Testing and validation framework.
  - Ability to run benchmarks widely used in RISC-V community and get numbers. A script that does this (flags: toolchain path, benchmark type etc.)
  - Ability to compare different runs of same or different benchmarks. See https://chromium.googlesource.com/external/llvm.org/test-suite:utils/compare.py

## Milestone 3:
- Getting codesize numbers and trying low hanging fruits
  - Get codesize numbers with llvm, and gcc at different optimization levels.
  - Try machine outliner and get numbers.
  - Try merge similar functions and get numbers.

## Milestone 4:
- Branding, Reachout, and possible horizontal expansion.
  - Connect with hardware vendors to get their requirements.
  - Build website and show numbers, in comparison with other available toolchains.
  - Provide popular opensource prebuilt binaries for RISC-V.
