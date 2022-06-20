# Mon Jun 20 03:18:58 UTC 2022
FROM registry.access.redhat.com/ubi8/ubi@sha256:1f89aefa39dbc96a47ae451d64f200a0013637cdbe048d1b9ef56c99976bb8c0
MAINTAINER lmaly@redhat.com
RUN dnf install -y --disableplugin=subscription-manager https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN dnf install -y https://vault.centos.org/centos/8/PowerTools/x86_64/os/Packages/qt5-qtwayland-devel-5.15.2-2.el8.x86_64.rpm
RUN dnf install -y --enablerepo=rhel-8-for-x86_64-appstream-rpms \
  cmake \
  extra-cmake-modules \
  gcc-c++ \
  git \
  kf5-knotifications-devel \
  libSM-devel \
  libXfixes-devel \
  libXtst-devel \
  qt5-qtbase-devel \
  qt5-qtbase-private-devel \
  qt5-qtdeclarative-devel \
  qt5-qtsvg-devel \
  qt5-qttools-devel \
  qt5-qtwayland-devel \
  qt5-qtx11extras-devel \
  rpmdevtools \
  wayland-devel \
  wget
RUN rpmdev-setuptree
COPY copyq.spec /root/rpmbuild/SPECS/
RUN cd /root/rpmbuild/SOURCES/ && wget https://github.com/hluk/CopyQ/archive/refs/tags/v6.1.0.tar.gz
RUN rpmbuild -ba /root/rpmbuild/SPECS/copyq.spec
RUN md5sum /root/rpmbuild/RPMS/x86_64/CopyQ-6.1.0-1.el8.x86_64.rpm > /root/rpmbuild/RPMS/x86_64/CopyQ-6.1.0-1.el8.x86_64.md5
RUN md5sum /root/rpmbuild/SRPMS/CopyQ-6.1.0-1.el8.src.rpm > /root/rpmbuild/SRPMS/CopyQ-6.1.0-1.el8.src.md5
