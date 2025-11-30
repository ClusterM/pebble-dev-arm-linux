FROM debian:bookworm-slim

WORKDIR /app

ENV STOP_AFTER=30
ENV DEBIAN_FRONTEND=noninteractive

COPY stpyv8_arm_package /root/stpyv8_arm_package
COPY patches /root/patches
COPY content/docker-entrypoint.sh /root/docker-entrypoint.sh
COPY content/qemu-pebble /usr/local/bin/qemu-pebble

# Add Debian Stretch repository for python2 and configure package priorities
RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list.d/stretch.list && \
    printf "Package: *\nPin: release n=stretch\nPin-Priority: 100\n" > /etc/apt/preferences.d/stretch && \
    printf "Package: python\nPin: release n=stretch\nPin-Priority: 500\n" >> /etc/apt/preferences.d/stretch && \
    printf "Package: python2*\nPin: release n=stretch\nPin-Priority: 500\n" >> /etc/apt/preferences.d/stretch && \
    apt-get update && apt-get install -y --no-install-recommends \
        tini \
        curl \
        wget \
        ca-certificates \
        qemu-user-static \
        binfmt-support \
        libc6-armhf-cross \
        libc6-dev-armhf-cross \
        gcc-arm-none-eabi \
        binutils-arm-none-eabi \
        libnewlib-arm-none-eabi \
        build-essential \
        pkg-config \
        zlib1g-dev \
        libglib2.0-dev \
        libpixman-1-dev \
        device-tree-compiler \
        libgtk-3-0 \
        libgtk-3-dev \
        libgdk-pixbuf2.0-dev \
        libx11-6 \
        libx11-dev \
        libgettextpo-dev \
        gettext \
        meson \
        cmake \
        flex \
        bison \
        gnupg \
        git \
        python \
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        npm \
        patch \
        patchelf \
        zip \
        gdb-multiarch \
    && cd /root/stpyv8_arm_package && pip3 install . --break-system-packages --no-deps --no-build-isolation --no-index --find-links /dev/null \
    && cd /root \
    && git clone https://github.com/coredevices/pebble-tool.git --branch=v5.0.16 \
    && cd /root/pebble-tool \
    && git apply /root/patches/pebble-tool.patch \
    && pip3 install . --break-system-packages \
    && cd /root \
    && git clone https://gitlab.com/qemu-project/dtc.git --branch=v1.7.2 \
    && cd /root/dtc \
    && meson build \
    && cd build \
    && ninja \
    && meson install \
    && cd /root \
    && rm -rf /root/dtc \
    && git clone https://github.com/coredevices/qemu.git \
    && cd qemu \
    && git checkout 606b793bbb79fa4105dc2be6a8d43939bb2d342e \
    && git apply /root/patches/qemu.patch \
    && ./configure --target-list=arm-softmmu --enable-gtk --disable-werror \
    && make -j$(nproc) install \
    && cd /root \
    && rm -rf /root/qemu \
    && chmod +x /root/docker-entrypoint.sh /usr/local/bin/qemu-pebble \
    && sed -i "3i from pathlib import Path\nPath('/tmp/pebble_flag').touch()" `which pebble` \
    && apt-get purge -y \
        build-essential \
        pkg-config \
        zlib1g-dev \
        libglib2.0-dev \
        libpixman-1-dev \
        device-tree-compiler \
        libgtk-3-dev \
        libgdk-pixbuf2.0-dev \
        libx11-dev \
        libgettextpo-dev \
        ninja \
        meson \
        cmake \
        flex \
        bison \
        git \
        python \
        python3-dev \
        python3-pip \
        zip \
        qemu-user-static \
        binfmt-support \
        libc6-armhf-cross \
        libc6-dev-armhf-cross \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pebble sdk install 4.9.77

ENTRYPOINT ["tini", "--", "/root/docker-entrypoint.sh"]
