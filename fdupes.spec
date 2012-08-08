#
# spec file for package fdupes (Version 1.40)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           fdupes
URL:            http://premium.caribe.net/~adrian2/fdupes.html
Group:          Productivity/Archiving/Compression
Summary:        Identifying or deleting duplicate files
Version:        1.40
Release:        42.66
License:        X11/MIT
Source0:        %{name}-%{version}.tar.bz2
Source1:        macros.%{name}
Patch0:         %{name}.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories



Authors:
--------
    Adrian Lopez <adrian2@caribe.net>

%prep
%setup -q
%patch0

%build
make

%install
install -D -m755 fdupes $RPM_BUILD_ROOT/usr/bin/fdupes
install -D -m644 fdupes.1 $RPM_BUILD_ROOT/usr/share/man/man1/fdupes.1
install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/etc/rpm/macros.fdupes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc CHANGES
%{_prefix}/bin/fdupes
%{_mandir}/*/*
/etc/rpm

