#!/usr/bin/env python3

'''
See help for more details.
usage: riscv-compiler.py --toolchain-container docker1 --execution-container docker2 --source-file file.c
'''

from argparse import ArgumentParser
import sys
import os
import subprocess


DOCKER_INVOKE = ['sudo', 'docker', 'exec', '-i', '-t']
DOCKER_CP = ['sudo', 'docker', 'cp']

def main():

    parser = ArgumentParser(description="Compiler and run c/c++ programs on riscv environment")

    parser.add_argument('-c', '--toolchain-container',
            action='store',
            help='Name of container with the toolchain',
            required=True)
    parser.add_argument('-ec', '--execution-container',
            action='store',
            help='Name of container where we execute binaries',
            required=True)
    parser.add_argument('-src', '--source-file',
            action='store',
            help='Path of source code to be compiled',
            required=True)

    try:
        args = parser.parse_args()
    #   print(args)

    except:
        parser.error("Invalid Options.")
        sys.exit(1)
    fileName = args.source_file
    containerName = args.toolchain_container
    exeContainerName = args.execution_container

    compilerPipeline(fileName, containerName, exeContainerName)

def getExtention(fileName):
    return fileName.split('.')[-1]

def selectCompiler(extention):
    compiler = ""
    if extention == "c":
            compiler = "riscv-cc"
    elif extention == "cpp":
            compiler = "riscv-cxx"
    return compiler

def sourceToExecutable(compiler, fileName, toolchainContainerName):
    # docker exec -i toolchainContainerName -c "compiler fileName -o executableFile"
    executableFile = "riscv.out"
    subprocess.run(DOCKER_INVOKE + [toolchainContainerName, compiler, fileName, "-o", executableFile ], check = True)
    return executableFile

def dockerToHost(containerName, fileNameHost, fileNameDocker):
    # docker cp containerName:/fileNameDocker pathToFileOnHost
    subprocess.run(DOCKER_CP + [containerName + ":/" + fileNameDocker, fileNameHost], check = True)

def hostToDocker(containerName, fileNameHost, fileNameDocker):
    # docker cp fileNameHost containerName:/fileNameDocker
    subprocess.run(DOCKER_CP + [fileNameHost, containerName + ":/" + fileNameDocker], check = True)

def sendToQemuAndRun(exeContainerName, fileName):
    # docker exec -it exeContainerName send fileName
    subprocess.run(DOCKER_INVOKE + [exeContainerName, "send", fileName])

def compilerPipeline(fileName, containerName, exeContainerName):
    extention = getExtention(fileName)
    compiler = selectCompiler(extention)
    hostToDocker(containerName, fileName, fileName)
    executableFile = sourceToExecutable(compiler, fileName, containerName)
    tempPathOnHost = "/tmp/riscv.out"
    tempPathOnExeDocker = "/root/riscv.out"
    dockerToHost(containerName, tempPathOnHost, executableFile)
    hostToDocker(exeContainerName, tempPathOnHost, tempPathOnExeDocker)
    sendToQemuAndRun(exeContainerName, tempPathOnExeDocker)

if __name__ == "__main__":
    main()
