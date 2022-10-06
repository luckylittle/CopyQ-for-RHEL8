# Thu Oct  6 09:37:48 UTC 2022
FROM registry.access.redhat.com/ubi8@sha256:8515a6e8a783b41249a7885c8f2c36380d58eb15dd3a377ea76ed3e932e3766d
MAINTAINER lmaly@redhat.com
ENV COPYQ_VER=6.3.2
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
  qt5-qtx11extras-devel \
  rpmdevtools \
  wayland-devel \
  wget
RUN rpmdev-setuptree
COPY copyq.spec /root/rpmbuild/SPECS/
RUN cd /root/rpmbuild/SOURCES/ && wget https://github.com/hluk/CopyQ/archive/refs/tags/v${COPYQ_VER}.tar.gz
RUN rpmbuild -ba /root/rpmbuild/SPECS/copyq.spec
RUN md5sum /root/rpmbuild/RPMS/x86_64/CopyQ-${COPYQ_VER}-1.el8.x86_64.rpm > /root/rpmbuild/RPMS/x86_64/CopyQ-${COPYQ_VER}-1.el8.x86_64.md5
RUN md5sum /root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el8.src.rpm > /root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el8.src.md5
