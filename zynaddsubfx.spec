%define _disable_ld_no_undefined	1

%define docver	1.4.3
%define oname	ZynAddSubFX

Name:		zynaddsubfx
Version:	2.4.3
Release:	1
Summary:	Real-time MIDI software synthesizer
Source0:	http://downloads.sourceforge.net/%{name}/%{oname}-%{version}.tar.bz2
Source1:	http://downloads.sourceforge.net/%{name}/%{oname}-doc-%{docver}.tar.gz
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
%setup -q -a 1 -n %{oname}-%{version}

chmod 644 *.txt
mv %{oname}-doc-%{docver} html

%build
%cmake
%make

%install
cd build/
%makeinstall_std

%files
%doc html *.txt ZynAddSubFX.lsm 
%doc  ExternalPrograms/Spliter/readme.txt
%{_bindir}/zynaddsubfx

%files dssi
%{_libdir}/dssi/libzynaddsubfx_dssi.so
