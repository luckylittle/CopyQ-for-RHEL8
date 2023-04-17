Name:           CopyQ
Version:        7.0.0
Release:        1%{?dist}
Summary:        CopyQ monitors system clipboard and saves its content in customized tabs.
Group:          Applications/Multimedia
License:        GPL
URL:            https://hluk.github.io/CopyQ/
Vendor:         Hluk
Source:         https://github.com/hluk/%{name}/archive/v%{version}.tar.gz
Prefix:         %{_prefix}
Packager:       lmaly@redhat.com
BuildRoot:      %{_tmppath}/%{name}-root

%description
CopyQ monitors system clipboard and saves its content in customized tabs. Saved clipboard can be later copied and pasted directly into any application.

%global debug_package %{nil}

%prep

%setup -q -n %{name}-%{version}

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local .
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/*

%changelog
* Sun Apr 2 17:49:00 GMT+10 2023 Hulk
  Added
    * Windows installer has an option to install for current user or all users (#1912).

  Changed
    * The preferred format to edit is now "text/plain;charset=utf-8" with "text/plain" as fallback. Additionally, if no such format is available, "text/uri-list" is used.
    * Toggle Clipboard Storing menu item uses static text and icon instead of changing these dynamically after each use (#2255).
    * Settings integrity is now handled solely by Qt. Previously, additional *.bak files where created for configuration files.
    * Commands are no longer migrated to the new format on start. The old command configuration file has been last used in version 3.9.0 (released on 2019-06-27).
    * Native notification text length is limited now to avoid slow downs when showing notifications in some desktop environments. The limit is about 100,000 characters and 100 lines.

  Fixed
    * Fixes Sort/Reverse Selected Items menu actions (#2267).
    * Fixes moving items to a tab in tab bar using drag'n'drop (#1246).
    * Fixes possibly buggy window manager frame geometry (#2247).
