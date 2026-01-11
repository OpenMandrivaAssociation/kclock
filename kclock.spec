%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		kclock
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kclock/-/archive/%{gitbranch}/kclock-%{gitbranchd}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kclock-%{version}.tar.xz
%endif
Summary:	Clock applet for Plasma Mobile
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QmlAssetDownloader)
BuildRequires:	cmake(Qt6ExamplesAssetDownloaderPrivate)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: qt6-qtmultimedia-gstreamer

%rename plasma6-kclock

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Clock applet for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/kclock
%{_bindir}/kclockd
%{_datadir}/applications/org.kde.kclock.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kclock.svg
%{_datadir}/metainfo/org.kde.kclock.appdata.xml
%{_sysconfdir}/xdg/autostart/org.kde.kclockd-autostart.desktop
%{_datadir}/knotifications6/kclockd.notifyrc
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.*.xml
%{_datadir}/dbus-1/services/org.kde.kclockd.service
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.kclock_1x2.so
%{_datadir}/icons/hicolor/scalable/apps/kclock_plasmoid.svg
%{_datadir}/krunner/dbusplugins/kclock-runner.desktop
