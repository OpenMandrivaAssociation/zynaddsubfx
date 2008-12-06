%define _disable_ld_no_undefined	1

%define docver	1.4.3
%define oname	ZynAddSubFX

Name:		zynaddsubfx
Version:	2.2.1
Release:	%{mkrel 7}
Summary:	Real-time MIDI software synthesizer
Source0:	http://downloads.sourceforge.net/%{name}/%{oname}-%{version}.tar.bz2
Source1:	http://downloads.sourceforge.net/%{name}/%{oname}-doc-%{docver}.tar.gz
Source3:	mandriva-controller.desktop
Source4:	mandriva-spliter.desktop
Source5:	mandriva-zynaddsubfx.desktop
Patch:		ZynAddSubFX-2.2.0-makefile.patch
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://sourceforge.net/projects/zynaddsubfx
BuildRequires:	libalsa-devel
BuildRequires:	fltk-devel
BuildRequires:	fftw3-devel
BuildRequires:	libjack-devel
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
%patch -p1 -b .makefile

# Fix up for fltk-config not existing any more - AdamW 2008/12
sed -i -e 's,`fltk-config --ldflags`,-lfltk,g' ExternalPrograms/Spliter/compile.sh ExternalPrograms/Controller/compile.sh src/Makefile
sed -i -e 's,`fltk-config --cflags`,,g' ExternalPrograms/Spliter/compile.sh ExternalPrograms/Controller/compile.sh src/Makefile

# fix a header name - AdamW 2008/12
sed -i -e 's,Fl_Box.h,Fl_Box.H,g' ExternalPrograms/Controller/ControllerUI.fl

chmod 644 *.txt
mv %{oname}-doc-%{docver} html

%build
cd src
make OPTFLAGS="%{optflags}"
cd ../ExternalPrograms/Spliter
export PATH=$PATH:.
./compile.sh
cd ../Controller/
./compile.sh

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/applications %{buildroot}/%{_datadir}/zynaddsubfx
install -m 755 src/zynaddsubfx %{buildroot}/%{_bindir}
install -m 755 ExternalPrograms/Spliter/spliter %{buildroot}/%{_bindir}
install -m 755 ExternalPrograms/Controller/controller %{buildroot}/%{_bindir}
install -m 644 %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}/%{_datadir}/applications
cp -a banks %{buildroot}/%{_datadir}/zynaddsubfx
cp -a presets %{buildroot}/%{_datadir}/zynaddsubfx

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc examples html *.txt ZynAddSubFX.lsm 
%doc  ExternalPrograms/Spliter/readme.txt
%{_bindir}/zynaddsubfx
%{_bindir}/spliter
%{_bindir}/controller
%{_datadir}/applications/*
%{_datadir}/zynaddsubfx/*
