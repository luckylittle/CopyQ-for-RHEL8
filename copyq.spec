Name:           CopyQ
Version:        6.2.0
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
* Sat Jul 06 00:00:00 AEDT 2022 Hulk
  Added
    Tabs can now load at least some items from a partially corrupted data file
    dropping the rest of the items.

    Simpler and safer data saving uses Qt framework (QSaveFile).

    New Settings class in scripts can be used to manage INI configuration
    files (#1964).

  Changed
    Obscure untested Save button has been removed from Action dialog.

  Fixed
    Fixes restoring window geometry in a loop (#1946).

    Fixes converting internal byte array representation in scripts in some rare
    cases.

    Fixes tray menu appearance to follow the configuration (#1896).

    The search history popup menu for will be closed if mouse wheel scrolls and
    mouse pointer is outside the menu (#1980).

    macOS: Fixes pasting (#2012).

    Windows: Fixes exiting the app on logout (#1249).

    Windows: Workaround to treat native path separators properly and not as
    special escape characters.
