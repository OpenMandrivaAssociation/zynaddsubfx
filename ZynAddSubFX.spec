%define docver 1.4.3

Name: ZynAddSubFX
Version: 2.2.1
Release: %mkrel 6
Summary: Real-time MIDI software synthesizer
Source0: http://prdownloads.sourceforge.net/zynaddsubfx/%{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/zynaddsubfx/%name-doc-%docver.tar.gz
Source3: mandriva-controller.desktop
Source4: mandriva-spliter.desktop
Source5: mandriva-zynaddsubfx.desktop
Patch: ZynAddSubFX-2.2.0-makefile.patch
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://sourceforge.net/projects/zynaddsubfx
BuildRequires: libalsa-devel
BuildRequires: fltk-devel
BuildRequires: fftw3-devel
BuildRequires: libjack-devel
BuildRequires: mxml-devel

%description
A real-time software synthesizer for Linux with many features,
including polyphony, multi-timbral and microtonal capabilities.  It
includes randomness of some parameters,which makes warm sounds, like
analogue synthesizers.  The program has system/insertion effects, too.

%files
%defattr(-,root,root)
%doc examples html *.txt ZynAddSubFX.lsm 
%doc  ExternalPrograms/Spliter/readme.txt
%_bindir/zynaddsubfx
%_bindir/spliter
%_bindir/controller
%{_datadir}/applications/*
%{_datadir}/zynaddsubfx/*

#----------------------------------------------------------------------------

%prep
%setup -q -a 1 -n %name-%{version}
%patch -p1 -b .makefile

chmod 644 *.txt
mv %name-doc-%docver html

%build
cd src
make OPTFLAGS="%optflags"
cd ../ExternalPrograms/Spliter
export PATH=$PATH:.
./compile.sh
cd ../Controller/
./compile.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir %buildroot/%_datadir/applications %buildroot/%_datadir/zynaddsubfx
install -m 755 src/zynaddsubfx %buildroot/%_bindir
install -m 755 ExternalPrograms/Spliter/spliter %buildroot/%_bindir
install -m 755 ExternalPrograms/Controller/controller %buildroot/%_bindir
install -m 644 %SOURCE3 %SOURCE4 %SOURCE5 %buildroot/%_datadir/applications
cp -a banks %buildroot/%_datadir/zynaddsubfx
cp -a presets %buildroot/%_datadir/zynaddsubfx


%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

