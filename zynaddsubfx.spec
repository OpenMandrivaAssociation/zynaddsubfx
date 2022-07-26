%define _disable_ld_no_undefined	1

%define docver	1.4.3
%define oname	ZynAddSubFX

Name:		zynaddsubfx
Version:	3.0.6
Release:	1
Summary:	Real-time MIDI software synthesizer
Source0:	https://sourceforge.net/projects/zynaddsubfx/files/zynaddsubfx/%{version}/zynaddsubfx-%{version}.tar.bz2
License:	GPLv2+
Group:		Sound
URL:		http://sourceforge.net/projects/zynaddsubfx
BuildRequires:	libalsa-devel
BuildRequires:	fltk-devel
BuildRequires:	fftw3-devel
BuildRequires:	cmake
BuildRequires:	pkgconfig(jack)
BuildRequires:	mxml-devel
BuildRequires:	dssi-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(liblo)
BuildRequires:	doxygen
BuildRequires:	pkgconfig(bash-completion)

%description
A real-time software synthesizer for Linux with many features,
including polyphony, multi-timbral and microtonal capabilities.  It
includes randomness of some parameters,which makes warm sounds, like
analogue synthesizers. The program has system/insertion effects, too.

%package dssi
Summary:	DSSI synthesizer plugin
Group:		Sound
License:	GPLv2+
Requires:	%{name} = %{version}-%{release}

%description dssi
This is the DSSI synthesizer plugin of zynaddsubfx, which can be used
with DSSI hosts like qtractor, ghostess, rosegarden and others.


%prep
%setup -q

chmod 644 *.txt

%build
%cmake -DPluginLibDir=%{_libdir}
%make_build

%install
%make_install -C build

%files
%doc AUTHORS.txt COPYING README.adoc
%{_bindir}/zynaddsubfx
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/banks
%{_libdir}/lv2/Zyn*
%{_libdir}/vst/Zyn*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.svg

%files dssi
%{_libdir}/dssi/libzynaddsubfx_dssi.so
