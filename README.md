# CopyQ-3.13.0-1.el8

## Installation

`sudo dnf install -y https://github.com/luckylittle/CopyQ-for-RHEL8/raw/master/CopyQ-3.13.0-1.el8.x86_64.rpm`

|Table                |               |
|---------------------|---------------|
|Installed packages:  | 45            |
|Total size:          | 18 M          |
|Total download size: | 16 M          |
|Installed size:      | 56 M          |

## Checksums

```text
067cb632d6f550352ca81ee83d412e58 *CopyQ-3.13.0-1.el8.src.rpm
d9240db2bfd9f9c568bf2195d4751a23 *CopyQ-3.13.0-1.el8.x86_64.rpm
```

## RPM Specfile used to build these packages

```text
Name:           CopyQ
Version:        3.13.0
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
/usr/local/share/applications/com.github.hluk.copyq.desktop
/usr/local/share/icons/hicolor/16x16/apps/copyq.png
/usr/local/share/icons/hicolor/22x22/apps/copyq.png
/usr/local/share/icons/hicolor/24x24/apps/copyq.png
/usr/local/share/icons/hicolor/32x32/apps/copyq.png
/usr/local/share/icons/hicolor/48x48/apps/copyq.png
/usr/local/share/icons/hicolor/64x64/apps/copyq.png
/usr/local/share/icons/hicolor/128x128/apps/copyq.png
/usr/local/share/copyq/themes/items.css
/usr/local/share/copyq/themes/main_window.css
/usr/local/share/copyq/themes/menu.css
/usr/local/share/copyq/themes/notification.css
/usr/local/share/copyq/themes/scrollbar.css
/usr/local/share/copyq/themes/tooltip.css
/usr/local/share/copyq/themes/dark.ini
/usr/local/share/copyq/themes/forest.ini
/usr/local/share/copyq/themes/light.ini
/usr/local/share/copyq/themes/paper.ini
/usr/local/share/copyq/themes/simple.ini
/usr/local/share/copyq/themes/solarized-dark.ini
/usr/local/share/copyq/themes/solarized-light.ini
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
/usr/local/share/copyq/translations/copyq_es.qm
/usr/local/share/copyq/translations/copyq_fa.qm
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
* Sat Oct 17 00:00:00 AEDT 2020 Hulk

	* Newly, if a global shortcut is triggered when the main window is active, the
command will be executed with item selection and item data available (#1435).

	* New focusPrevious() script function to activate window that was focused
before the main window.

	* Export now write data to a temporary file before saving.

	* Display command are now also applied on item preview (e.g. to enable syntax
highlighting in the preview).

	* New command line option "tray_menu_open_on_left_click" to check default mouse
button behavior for tray icon (copyq config tray_menu_open_on_left_click true).

	* New command line option "activate_item_with_single_click" to activate items
with single click (copyq config activate_item_with_single_click true).

	* New command line options "filter_regular_expression" and
"filter_case_insensitive" to change the item search behavior.

	* New command line option "native_menu_bar" to disable native/global menu bar
(copyq config native_menu_bar false).

	* Updated icons (Font Awesome 5.15.1)

	* Improved performance of loading the icon font.

	* Fix crash when exporting large amount of data (#1462).

	* Fix entering vi search mode (#1458).

	* Fix size of scrollable text area in item preview (#1472).

	* OSX: Broken native/global menu bar was replaced by default with application
menu bar (#1444). This can be changed with copyq config native_menu_bar true.

	* OSX: Mouse click on tray icon is now handled similarly to other platforms.
This can be changed with copyq config tray_menu_open_on_left_click true.
```

## Packager

lmaly@redhat.com

---

_Last update: Wed Dec 16 02:43:02 UTC 2020_
