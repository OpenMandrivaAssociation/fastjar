Name:		fastjar
Version:	0.98
Release:	9
Epoch:		0
Summary:	Archive tool for Java archives
License:	GPLv2+
Group:		Development/Java
URL:		http://savannah.nongnu.org/projects/fastjar
Source0:	http://download.savannah.nongnu.org/releases/fastjar/fastjar-%{version}.tar.gz
Source1:	http://download.savannah.nongnu.org/releases/fastjar/fastjar-%{version}.tar.gz.sig
Patch0: fastjar-0.98-CVE-2010-0831,2322.diff
BuildRequires:	zlib-devel

%description
fastjar is an implementation of Sun's jar utility that comes with
the JDK, written entirely in C, and runs in a fraction of the time
while being feature compatible.

Also included in this package is the grepjar program which can be
used to search files in a jar file for a pattern.

%prep
%setup -q
%patch0 -p0 -b .CVE-2010-0831,2322

%build
%configure2_5x
%make

%install
%{makeinstall_std}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%attr(0755,root,root) %{_bindir}/fastjar
%attr(0755,root,root) %{_bindir}/grepjar
%{_infodir}/fastjar.info*
%{_mandir}/man1/fastjar.1*
%{_mandir}/man1/grepjar.1*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0:0.98-6mdv2011.0
+ Revision: 664283
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.98-5mdv2011.0
+ Revision: 605117
- rebuild

* Tue Jun 22 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.98-4mdv2010.1
+ Revision: 548630
- P0: security fix for CVE-2010-0831 (ubuntu)

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.98-3mdv2010.1
+ Revision: 522599
- rebuilt for 2010.1

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Clean spec file
    - use %%make and %%configure2_5x

* Wed Sep 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0:0.98-1mdv2010.0
+ Revision: 435991
- update to new version 0.98

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:0.97-2mdv2010.0
+ Revision: 424426
- rebuild

* Mon Nov 24 2008 David Walluck <walluck@mandriva.org> 0:0.97-1mdv2009.1
+ Revision: 306120
- 0.97

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0:0.95-3mdv2009.0
+ Revision: 220742
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0:0.95-2mdv2008.1
+ Revision: 149713
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 14 2007 David Walluck <walluck@mandriva.org> 0:0.95-1mdv2008.0
+ Revision: 63435
- BuildRequires: zlib-devel
- Import fastjar



* Tue Aug 14 2007 David Walluck <walluck@mandriva.org> 0:0.95-1mdv2008.0
- release
