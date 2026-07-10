#!/bin/bash

VERSION=$1

ARCH=$(uname -m)

case $ARCH in
    x86_64)
        ARCH_NAME=x64
        ;;
    i686)
        ARCH_NAME=x86
        ;;
    armv5*)
        ARCH_NAME=armv5
        ;;
    armv6*)
        ARCH_NAME=armv6
        ;;
    armv7*)
        ARCH_NAME=armv7
        ;;
    aarch64*)
        ARCH_NAME=arm64
        ;;
    mips*)
        ARCH_NAME=mips32
        ;;
    mipsle*)
        ARCH_NAME=mips32le
        ;;
    mips64*)
        ARCH_NAME=mips64
        ;;
    mips64le*)
        ARCH_NAME=mips64le
        ;;
    riscv64*)
        ARCH_NAME=riscv64
        ;;
    *)
        echo "Unsupported architecture: $ARCH"
        exit 1
        ;;
esac

BASE_URL=https://github.com/v2rayA/v2rayA/releases/download/v$VERSION
wget "$BASE_URL/v2raya_linux_${ARCH_NAME}_$VERSION"
wget "$BASE_URL/v2raya_core_linux_${ARCH_NAME}_$VERSION"
