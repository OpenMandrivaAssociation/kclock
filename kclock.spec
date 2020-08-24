%define snapshot 20200823
%define commit 8c52fe3f8cc1fbc9b47fd6c32890bc91db69b28a

Name:		kclock
Version:	0.0
Release:	0.%{snapshot}.1
Summary:	Clock applet for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/kclock/-/archive/master/kclock-%{snapshot}.tar.bz2
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
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)

%description
Clock applet for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-master-%{commit}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kclock
%{_datadir}/applications/org.kde.kclock.desktop
%{_datadir}/icons/hicolor/scalable/apps/kclock.svg
%{_datadir}/metainfo/org.kde.kclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kclock.appdata.xml
%{_sysconfdir}/xdg/autostart/org.kde.kclock-autostart.desktop
%{_datadir}/knotifications5/kclock.notifyrc
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_kclock.so
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kclock.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock
