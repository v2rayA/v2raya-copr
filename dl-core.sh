#!/bin/bash

VERSION=$1

ARCH=$(uname -m)

case $ARCH in
    x86_64)
        FILE=v2raya_linux_x64_$VERSION
        ;;
    i686)
        FILE=v2raya_linux_x86_$VERSION
        ;;
    armv5*)
        FILE=v2raya_linux_armv5_$VERSION
        ;;
    armv6*)
        FILE=v2raya_linux_armv6_$VERSION
        ;;
    armv7*)
        FILE=v2raya_linux_armv7_$VERSION
        ;;
    aarch64*)
        FILE=v2raya_linux_arm64_$VERSION
        ;;
    mips*)
        FILE=v2raya_linux_mips32_$VERSION
        ;;
    mipsle*)
        FILE=v2raya_linux_mips32le_$VERSION
        ;;
    mips64*)
        FILE=v2raya_linux_mips64_$VERSION
        ;;
    mips64le*)
        FILE=v2raya_linux_mips64le_$VERSION
        ;;
    riscv64*)
        FILE=v2raya_linux_riscv64_$VERSION
        ;;
    *)
        echo "Unsupported architecture: $ARCH"
        exit 1
        ;;
esac

wget https://github.com/v2rayA/v2rayA/releases/download/v$VERSION/$FILE
