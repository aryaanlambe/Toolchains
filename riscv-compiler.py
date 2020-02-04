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
            nargs='+',
            help='Path of source code to be compiled',
            required=True)
    parser.add_argument('-o', '--output',
            action='store',
            help='Path to output executable file, default is /tmp/riscv.out',
            required=False)

    try:
        args, compilerOptions = parser.parse_known_args()
    #   print(args)

    except:
        parser.error("Invalid Options.")
        sys.exit(1)

    fileNames = args.source_file
    containerName = args.toolchain_container
    exeContainerName = args.execution_container

    output = "/tmp/riscv.out"
    if args.output:
        output = args.output

    compilerPipeline(fileNames, containerName, exeContainerName, compilerOptions, output)

def getExtention(fileNames):
    return fileNames[0].split('.')[-1]

def selectCompiler(extention):
    compiler = ""
    if extention == "c":
            compiler = "riscv-cc"
    elif extention == "cpp":
            compiler = "riscv-cxx"
    return compiler

def sourceToExecutable(compiler, fileNames, toolchainContainerName, compilerOptions):
    # docker exec -i toolchainContainerName -c "compiler fileName -o executableFile"
    executableFile = "riscv.out"
    subprocess.run(DOCKER_INVOKE + [toolchainContainerName, compiler, *fileNames, *compilerOptions, "-o", executableFile ], check = True)
    return executableFile

def dockerToHost(containerName, fileNameHost, fileNameDocker):
    # docker cp containerName:/fileNameDocker pathToFileOnHost
    subprocess.run(DOCKER_CP + [containerName + ":/" + fileNameDocker, fileNameHost], check = True)

def sendSourceToDocker(containerName, fileNamesHost, fileNamesDocker):
    for fileName in fileNamesHost:
        hostToDocker(containerName, fileName, fileName)

def hostToDocker(containerName, fileNameHost, fileNameDocker):
    # docker cp fileNameHost containerName:/fileNameDocker
    subprocess.run(DOCKER_CP + [fileNameHost, containerName + ":/" + fileNameDocker], check = True)

def sendToQemuAndRun(exeContainerName, fileName):
    # docker exec -it exeContainerName send fileName
    subprocess.run(DOCKER_INVOKE + [exeContainerName, "send", fileName])

def compilerPipeline(fileNames, containerName, exeContainerName, compilerOptions, output):
    extention = getExtention(fileNames)
    compiler = selectCompiler(extention)
    sendSourceToDocker(containerName, fileNames, fileNames)
    executableFile = sourceToExecutable(compiler, fileNames, containerName, compilerOptions)
    tempPathOnHost = output
    tempPathOnExeDocker = "/root/riscv.out"
    dockerToHost(containerName, tempPathOnHost, executableFile)
    hostToDocker(exeContainerName, tempPathOnHost, tempPathOnExeDocker)
    sendToQemuAndRun(exeContainerName, tempPathOnExeDocker)

if __name__ == "__main__":
    main()
