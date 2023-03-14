Name:           CopyQ
Version:        6.4.0
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
* Thu Jan 19 21:14:00 GMT+11 2023 Hulk
  Added
    * Items in menu can be additionally filtered using the item notes (#2170).
    * Items can be sorted with a custom order via scripting.

  Changed
    * More shortcuts and even sequences of shortcuts can be now captured and assigned. This uses new QKeySequenceEdit UI widget from Qt framework.
    * UI uses the preferred sans-serif system font in the dark theme.

  Fixed
    * Fixes copying items in order they were selected (#2124).
    * Fixes re-selecting the edited item after external editor closes.
    * Fixes menu theme (#2139).
    * Avoids duplicating items from clipboard in synchronized tabs (#2236).
    * macOS: Fixes compatibility with macOS 10.15 (#2103).
    * Linux: Fixes synchronizing UTF-encoded text to/from primary selection (#2195)
    * Wayland: Avoids showing window after a screen is turned on.
    * Wayland: Avoids a rare crash while accessing clipboard data.
    * Wayland: Fixes pasting to some XWayland apps (#2234)
    * X11: Avoids app freeze when entering search mode (#2171).
    * X11: Fixes capturing quickly changing clipboard text (ignores unchanged TIMESTAMP).
