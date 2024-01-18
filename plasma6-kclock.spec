%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200823
#define commit 8c62fe3f8cc1fbc9b47fd6c32890bc91db69b28a

Name:		plasma6-kclock
Version:	24.01.90
Release:	%{?git:0.%{git}.}3
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma-mobile/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kclock-%{version}.tar.xz
%endif
Summary:	Clock applet for Plasma Mobile
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: qt6-qtmultimedia-gstreamer

%description
Clock applet for Plasma Mobile

%prep
%if 0%{?git}
%autosetup -p1 -n kclock-master-%{commit}
%else
%autosetup -p1 -n kclock-%{?git:master}%{!?git:%{version}}
%endif
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kclock --all-name

%files -f kclock.lang
%{_bindir}/kclock
%{_bindir}/kclockd
%{_datadir}/applications/org.kde.kclock.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kclock.svg
%{_datadir}/metainfo/org.kde.kclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kclock_1x2.appdata.xml
%{_sysconfdir}/xdg/autostart/org.kde.kclockd-autostart.desktop
%{_datadir}/knotifications6/kclockd.notifyrc
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.*.xml
%{_datadir}/dbus-1/services/org.kde.kclockd.service
%{_datadir}/icons/*/scalable/apps/kclock_plasmoid_1x2.svg
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.kclock_1x2.so
