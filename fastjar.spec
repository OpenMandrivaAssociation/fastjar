Name:           fastjar
Version:        0.97
Release:        %mkrel 1
Epoch:          0
Summary:        Archive tool for Java archives
License:        GPLv2+
Group:          Development/Java
URL:            http://savannah.nongnu.org/projects/fastjar
Source0:        http://download.savannah.nongnu.org/releases/fastjar/fastjar-%{version}.tar.gz
Source1:        http://download.savannah.nongnu.org/releases/fastjar/fastjar-%{version}.tar.gz.sig
Requires(post): info-install
Requires(preun): info-install
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
fastjar is an implementation of Sun's jar utility that comes with
the JDK, written entirely in C, and runs in a fraction of the time
while being feature compatible.

Also included in this package is the grepjar program which can be
used to search files in a jar file for a pattern.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%post
%_install_info fastjar.info

%preun
%_remove_install_info fastjar.info

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%attr(0755,root,root) %{_bindir}/fastjar
%attr(0755,root,root) %{_bindir}/grepjar
%{_infodir}/fastjar.info*
%{_mandir}/man1/fastjar.1*
%{_mandir}/man1/grepjar.1*
