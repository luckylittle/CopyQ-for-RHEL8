Name:           CopyQ
Version:        6.1.0
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
/usr/local/share/icons/hicolor/scalable/apps/copyq.svg
/usr/local/share/icons/hicolor/scalable/apps/copyq_mask.svg
/usr/local/share/metainfo/com.github.hluk.copyq.appdata.xml
/usr/local/share/man/man1/copyq.1
/usr/local/share/bash-completion/completions/copyq
/usr/local/share/applications/com.github.hluk.copyq.desktop
/usr/local/share/icons/hicolor/16x16/apps/copyq.png
/usr/local/share/icons/hicolor/22x22/apps/copyq.png
/usr/local/share/icons/hicolor/24x24/apps/copyq.png
/usr/local/share/icons/hicolor/32x32/apps/copyq.png
/usr/local/share/icons/hicolor/48x48/apps/copyq.png
/usr/local/share/icons/hicolor/64x64/apps/copyq.png
/usr/local/share/icons/hicolor/128x128/apps/copyq.png
/usr/local/share/copyq/themes/dark.ini
/usr/local/share/copyq/themes/forest.ini
/usr/local/share/copyq/themes/items.css
/usr/local/share/copyq/themes/light.ini
/usr/local/share/copyq/themes/main_window.css
/usr/local/share/copyq/themes/main_window_simple.css
/usr/local/share/copyq/themes/menu.css
/usr/local/share/copyq/themes/notification.css
/usr/local/share/copyq/themes/paper.ini
/usr/local/share/copyq/themes/simple.ini
/usr/local/share/copyq/themes/solarized-dark.ini
/usr/local/share/copyq/themes/solarized-light.ini
/usr/local/share/copyq/themes/tooltip.css
/usr/local/share/copyq/themes/wine.ini
/usr/local/lib/copyq/plugins/libitemencrypted.so
/usr/local/lib/copyq/plugins/libitemfakevim.so
/usr/local/lib/copyq/plugins/libitemimage.so
/usr/local/lib/copyq/plugins/libitemnotes.so
/usr/local/lib/copyq/plugins/libitempinned.so
/usr/local/lib/copyq/plugins/libitemtags.so
/usr/local/lib/copyq/plugins/libitemtext.so
/usr/local/lib/copyq/plugins/libitemsync.so
/usr/local/bin/copyq
/usr/local/share/copyq/translations/copyq_ar.qm
/usr/local/share/copyq/translations/copyq_cs.qm
/usr/local/share/copyq/translations/copyq_da.qm
/usr/local/share/copyq/translations/copyq_de.qm
/usr/local/share/copyq/translations/copyq_el.qm
/usr/local/share/copyq/translations/copyq_es.qm
/usr/local/share/copyq/translations/copyq_fa.qm
/usr/local/share/copyq/translations/copyq_fi.qm
/usr/local/share/copyq/translations/copyq_fr.qm
/usr/local/share/copyq/translations/copyq_hr.qm
/usr/local/share/copyq/translations/copyq_hu.qm
/usr/local/share/copyq/translations/copyq_id.qm
/usr/local/share/copyq/translations/copyq_it.qm
/usr/local/share/copyq/translations/copyq_ja.qm
/usr/local/share/copyq/translations/copyq_ko.qm
/usr/local/share/copyq/translations/copyq_lt.qm
/usr/local/share/copyq/translations/copyq_nb.qm
/usr/local/share/copyq/translations/copyq_nl.qm
/usr/local/share/copyq/translations/copyq_pl.qm
/usr/local/share/copyq/translations/copyq_pt_BR.qm
/usr/local/share/copyq/translations/copyq_pt_PT.qm
/usr/local/share/copyq/translations/copyq_ru.qm
/usr/local/share/copyq/translations/copyq_sk.qm
/usr/local/share/copyq/translations/copyq_sv.qm
/usr/local/share/copyq/translations/copyq_tr.qm
/usr/local/share/copyq/translations/copyq_uk.qm
/usr/local/share/copyq/translations/copyq_zh_CN.qm
/usr/local/share/copyq/translations/copyq_zh_TW.qm


%changelog
* Sat Mar 05 00:00:00 AEDT 2022 Hulk
  Added
  - Users can now customize shortcuts for the built-in editor (#708).
  - Users can now set default style sheet for HTML items to override for example
    color for hyperlinks with `a { color: lightblue }` (#1859). The new settings
    can be found under Item configuration tab under Text sub-tab.
  Changed
  - Window geometry (size and position) restoring is now simpler: The app sets
    geometry only initially and when the current screen/monitor changes.

    The mouse cursor position indicates the current screen. In case the app
    cannot inspect the mouse pointer position (for example on some Wayland
    compositors), it is left up to the window manager to decide to move the
    window to another screen.

    Users can still disable the automatic geometry by running the following
    command (in Action dialog or terminal) and restarting the app:
    copyq config restore_geometry false
  Fixed
  - Fixes moving items in synchronized tabs after activating them from the
    context menu (#1897).
  - Windows: Fixes tray icon tooltip (#1864).
  - Windows: External editor command now treats native path separators properly
    (#1894, #1868).
  - macOS: Fixes crash when pasting from the main window or menu (#1847).
  - macOS: Older versions of macOS (down to 10.15) are now supported again
    (#1866).
  - Wayland: Fixes using correct window title icon (#1910).
  - Wayland: Fixes retrieving UTF-8 encoded text from selection in environments
    which supports it.
  - Wayland: Fixes restoring window size without breaking window position (window
    position cannot be set in most or all Wayland compositors).

