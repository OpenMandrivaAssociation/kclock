%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200823
#define commit 8c52fe3f8cc1fbc9b47fd6c32890bc91db69b28a

Name:		kclock
Version:	23.08.2
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma-mobile/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary:	Clock applet for Plasma Mobile
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5KirigamiAddons)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)

%description
Clock applet for Plasma Mobile

%prep
%if 0%{?git}
%autosetup -p1 -n %{name}-master-%{commit}
%else
%autosetup -p1
%endif
%cmake_kde5 -G Ninja

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
%{_datadir}/knotifications5/kclockd.notifyrc
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_kclock_1x2.so
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.*.xml
%{_datadir}/dbus-1/services/org.kde.kclockd.service
%{_datadir}/icons/*/scalable/apps/kclock_plasmoid_1x2.svg
