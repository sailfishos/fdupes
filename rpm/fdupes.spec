#
# based on SUSE spec file for package fdupes
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           fdupes
URL:            https://github.com/adrianlopezroche/fdupes
Summary:        Tool to identify or delete duplicate files
Version:        2.3.0
Release:        1
License:        MIT
Source0:        %{name}-%{version}.tar.bz2
Source1:        macros.%{name}
Source2:        fdupes_wrapper.cpp
Patch0:         0001-Add-license-file.patch

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
autoreconf -fiv
%configure --without-ncurses --without-sqlite
%make_build
g++ $RPM_OPT_FLAGS %{S:2} -o fdupes_wrapper

%install
%make_install
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.fdupes
install -D -m755 fdupes_wrapper %{buildroot}/usr/lib/rpm/fdupes_wrapper

%files
%license LICENSE
%doc CHANGES
%{_bindir}/fdupes
%{_mandir}/*/*
%{_rpmmacrodir}/macros.fdupes
/usr/lib/rpm/fdupes_wrapper
