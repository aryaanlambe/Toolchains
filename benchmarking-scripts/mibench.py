#!/usr/bin/env python3

'''
See help for more details.
Usage: python3 mibench.py --compiler-wrapper /riscv-compiler.py --toolchain_container docker1 --execution_container docker2
'''

from argparse import ArgumentParser
import sys
import os
import subprocess
import re

def main():

    parser = ArgumentParser(description="Compiler and run c/c++ programs on riscv environment")

    parser.add_argument('-cc', '--compiler-wrapper',
            action='store',
            help='Path to the compiler wrapper script',
            required=True)
    parser.add_argument('-c', '--toolchain-container',
            action='store',
            help='Name of container with toolchain',
            required=True)
    parser.add_argument('-ec', '--execution-container',
            action='store',
            help='Name of container where binaries are executed',
            required=True)

    try:
        args = parser.parse_args()
        print(args)

    except:
        parser.error("Invalid Options.")
        sys.exit(1)

    compiler = args.compiler_wrapper + " --toolchain-container " + args.toolchain_container + " --execution-container " + args.execution_container
    mibench(compiler)

def mibench(compiler):
    downloadSources()
    pwd = os.getcwd()
    newEnv = os.environ.copy()
    newEnv["CC"] = compiler
    newEnv["CXX"] = compiler
    for root, dirs, files in os.walk("mibench"):
        if 'Makefile' in files:
            file = pwd + "/" + root + "/Makefile"
            subprocess.run("sed -i 's/gcc/python3 " + re.escape(compiler) + "/g' " + file, shell = True, check = True)
            run(root, newEnv)

def downloadSources():
    subprocess.run(["git", "clone", "https://github.com/embecosm/mibench.git", "-b", "embedded"], check = True)

def run(root, newEnv):
    owd = os.getcwd()
    os.chdir(root)
    subprocess.run(["make"], check = True, env = newEnv)
    os.chdir(owd)

if __name__ == "__main__":
    main()
