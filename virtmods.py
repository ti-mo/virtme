#!/usr/bin/python3
# -*- mode: python -*-
# virtmods: Default module configuration
# Copyright © 2014 Andy Lutomirski
# Licensed under the GPLv2, which is available in the virtme distribution
# as a file called LICENSE with SHA-256 hash:
# 8177f97513213526df2cf6184d8ff986c675afb514d4e68a404010521b880643

MODALIASES = [
    # These are most likely portable across all architectures.
    'fs-9p',
    'virtio:d00000009v00001AF4',  # 9pnet_virtio
    'virtio:d00000003v00001AF4',  # virtio_console

    # For virtio_pci architectures (which are, hopefully, all that we care
    # about), there's really only one required driver, virtio_pci.
    # For completeness, here are both of the instances we care about
    # for basic functionality.
    'pci:v00001AF4d00001009sv00001AF4sd00000009bc00sc02i00',  # 9pnet
    'pci:v00001AF4d00001003sv00001AF4sd00000003bc07sc80i00',  # virtconsole
]


# This is a heuristic to allow virtme to work even if depmod hasn't
# been run.
MODPATHS = [
    'kernel/fs/fscache/fscache.ko',
    'kernel/net/9p/9pnet.ko',
    'kernel/fs/9p/9p.ko',
    'kernel/drivers/virtio/virtio.ko',
    'kernel/drivers/virtio/virtio_ring.ko',
    'kernel/net/9p/9pnet_virtio.ko',
    'kernel/drivers/char/virtio_console.ko',
    'kernel/drivers/virtio/virtio_pci.ko',
]
