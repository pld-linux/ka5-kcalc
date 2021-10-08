%define		kdeappsver	21.08.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kcalc
Summary:	Kcalc
Name:		ka5-%{kaname}
Version:	21.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3a40f1c41cf733b4da74f6deea157e6c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kinit-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCalc is a calculator which offers many more mathematical functions
than meet the eye on a first glance.. Features. The usual
functionality offered by most scientific calculators; Trigonometric
functions, logic operations, and statistical calculations.

%description -l pl.UTF-8
KCalc jest kalkulatorem, które oferuje wiele więcej funkcji
matematycznych niż widać na pierwszy rzut oka.
Właściwości: zwyczajna funkcjonalność oferowana przez większość
kalkulatorów naukowych; funkcje trygonometryczne, operacje logiczne,
obliczania statystyczne.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{lt,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%{_desktopdir}/org.kde.kcalc.desktop
%{_datadir}/config.kcfg/kcalc.kcfg
%{_datadir}/kcalc
%{_datadir}/kconf_update/kcalcrc.upd
%{_datadir}/metainfo/org.kde.kcalc.appdata.xml
