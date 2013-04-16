Summary:	Archive tool for Java archives
Name:		fastjar
Version:	0.98
Release:	9
License:	GPLv2+
Group:		Development/Java
Url:		http://savannah.nongnu.org/projects/fastjar
Source0:	http://download.savannah.nongnu.org/releases/fastjar/fastjar-%{version}.tar.gz
Source1:	http://download.savannah.nongnu.org/releases/fastjar/fastjar-%{version}.tar.gz.sig
Patch0: fastjar-0.98-CVE-2010-0831,2322.diff
BuildRequires:	pkgconfig(zlib)

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
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/fastjar
%{_bindir}/grepjar
%{_infodir}/fastjar.info*
%{_mandir}/man1/fastjar.1*
%{_mandir}/man1/grepjar.1*

