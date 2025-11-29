FROM debian:bookworm

WORKDIR /app

ENV STOP_AFTER=30
ENV BROWSER="browser-wrapper.sh"
ENV DEBIAN_FRONTEND=noninteractive

COPY stpyv8_arm_package /root/stpyv8_arm_package
COPY patches /root/patches
COPY content/decode_url.py /usr/bin/decode_url
COPY content/browser-wrapper.sh /usr/bin/browser-wrapper.sh
COPY content/docker-entrypoint.sh /root/docker-entrypoint.sh
COPY content/qemu-pebble /usr/local/bin/qemu-pebble

# Add Debian Stretch repository for python2 and configure package priorities
RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list.d/stretch.list && \
    printf "Package: *\nPin: release n=stretch\nPin-Priority: 100\n" > /etc/apt/preferences.d/stretch && \
    printf "Package: python\nPin: release n=stretch\nPin-Priority: 500\n" >> /etc/apt/preferences.d/stretch && \
    printf "Package: python2*\nPin: release n=stretch\nPin-Priority: 500\n" >> /etc/apt/preferences.d/stretch

# Install only basic tools needed for install.sh
RUN apt-get update && apt-get install -y --no-install-recommends \
    tini \
    curl \
    wget \
    ca-certificates \
    gcc-arm-none-eabi \
    binutils-arm-none-eabi \
    libnewlib-arm-none-eabi \
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
    gettext \
    meson \
    cmake \
    flex \
    bison \
    gnupg \
    git \
    python \
    python3 \
    python3-pip \
    python3-venv \
    python3-sh \
    npm \
    zip \
    chromium
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

RUN cd /root/stpyv8_arm_package && pip3 install . --break-system-packages \
    && cd /root \
    && git clone https://github.com/coredevices/pebble-tool.git --branch=v5.0.16 \
    && cd /root/pebble-tool \
    && git apply /root/patches/pebble-tool.patch \
    && pip3 install . --break-system-packages \
    && cd /root \
    && rm -rf /root/pebble-tool \
    && pebble sdk install latest \
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
    && chmod +x /usr/bin/browser-wrapper.sh /usr/bin/decode_url /root/docker-entrypoint.sh /usr/local/bin/qemu-pebble \
    && sed -i "3i from pathlib import Path\nPath('/tmp/pebble_flag').touch()" `which pebble`

ENTRYPOINT ["tini", "--", "/root/docker-entrypoint.sh"]
