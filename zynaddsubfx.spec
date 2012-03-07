%define _disable_ld_no_undefined	1

%define docver	1.4.3
%define oname	ZynAddSubFX

Name:		zynaddsubfx
Version:	2.4.2
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
Provides:	ZynAddSubFX = %{version}-%{release}
Obsoletes:	ZynAddSubFX < %{version}-%{release}

%description
A real-time software synthesizer for Linux with many features,
including polyphony, multi-timbral and microtonal capabilities.  It
includes randomness of some parameters,which makes warm sounds, like
analogue synthesizers.  The program has system/insertion effects, too.

%prep
%setup -q -a 1 -n %{oname}-%{version}

# fix a header name - AdamW 2008/12
sed -i -e 's,Fl_Box.h,Fl_Box.H,g' ExternalPrograms/Controller/ControllerUI.fl

chmod 644 *.txt
mv %{oname}-doc-%{docver} html

%build
%cmake
%make

%install
cd build/
%makeinstall_std

%files
%doc examples html *.txt ZynAddSubFX.lsm 
%doc  ExternalPrograms/Spliter/readme.txt
%{_bindir}/zynaddsubfx
