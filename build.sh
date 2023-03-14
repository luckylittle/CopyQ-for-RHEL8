#!/bin/zsh
# Mon Mar 13 23:53:58 UTC 2023
COPYQ_VER=6.4.0
ARCH=x86_64
RELEASEVER=8
# Run the build
podman build -t copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH} -f Containerfile .
podman run --name copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH} copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}
# Copy the artifacts from inside the container
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/RPMS/${ARCH}/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}.rpm .
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/RPMS/${ARCH}/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}.md5 .
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.src.rpm .
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.src.md5 .
# Cleanup container & image
podman rm copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}
podman rmi copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}
# Cleanup UBI8
# podman images --format "{{.ID}} {{.Repository}}" | grep registry.access.redhat.com/ubi8 | cut -d ' ' -f 1 | xargs podman rmi
