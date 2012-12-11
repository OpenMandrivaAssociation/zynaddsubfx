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
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pixman-1)

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


%changelog
* Mon Jun 25 2012 Frank Kober <emuse@mandriva.org> 2.4.3-1
+ Revision: 806816
- missing dssi-devel BR added
- new version 2.4.3

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 2.4.2

* Tue Aug 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.4.1-1mdv2011.0
+ Revision: 572671
- rediff p0
- update to 2.4.1

* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 2.4.0-2mdv2010.1
+ Revision: 493143
- rebuild for new fltk

* Thu Jul 16 2009 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2010.0
+ Revision: 396665
- new version
- rediff the patch
- fix build and installation

* Sun Dec 07 2008 Adam Williamson <awilliamson@mandriva.org> 2.2.1-7mdv2009.1
+ Revision: 311514
- rebuild for new fltk
- some quick fixes for build with latest fltk
- update .desktop files not to include MDV menu categories
- new license policy
- disable no_undefined (breaks build, no shared lib here)
- clean spec
- rename to lower-case per MDV policy
- rename per policy

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 2.2.1-6mdv2009.0
+ Revision: 263231
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 2.2.1-5mdv2009.0
+ Revision: 262918
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 14 2007 Helio Chissini de Castro <helio@mandriva.com> 2.2.1-3mdv2008.0
+ Revision: 26726
- Moved .desktop files outside spec
- Added banks and presets ( already included in package but not installed )
- Removed old menudir ( not used on 2008 )
- import ZynAddSubFX-2.2.1-2mdv2007.0

