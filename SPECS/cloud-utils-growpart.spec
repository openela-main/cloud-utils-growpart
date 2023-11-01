Name:		cloud-utils-growpart
Version:	0.33
Release:	0%{?dist}
License:	GPLv3
Group:		System Environment/Base
Source0:	cloud-utils-0.33.tar.gz
URL:		https://github.com/canonical/cloud-utils/
Source1:	LICENSE


BuildArch:	noarch

Summary:	Script for growing a partition

Requires:	gawk
Requires:	util-linux
# gdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
#Requires:	gdisk

%description
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.

%prep
%autosetup -n cloud-utils-%{version} -p1

%build

%install
cp %{SOURCE1} LICENSE

# Create the target directories
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1

# Install the growpart binary and man page
cp bin/growpart $RPM_BUILD_ROOT/%{_bindir}/
cp man/growpart.* $RPM_BUILD_ROOT/%{_mandir}/man1/

%files
%doc ChangeLog LICENSE
%{_bindir}/growpart
%doc %{_mandir}/man1/growpart.*

%changelog
* Thu Nov 17 2022 Jon Maloy <jmaloy@redhat.com> - 0.33-0
- Rebased to cloud-utils-growpart-0.33-0.el8
- Resolves: bz#2122575
  ([RHEL-8] Add redhat build support for cloud-utils rebase 0.33 for RHEL8.8

* Mon Jun 14 2021 Miroslav Rezanina <mrezanin@redhat.com> - 0.31-3
- cu-Fix-issue-LP-1928167-growpart-doesn-t-work-when-LANG.patch [bz#1885992]
- Resolves: bz#1885992
  ([RHEL-8] growpart doesn't work when LANG=cs_CZ.UTF-8)

* Wed Jun 02 2021 Miroslav Rezanina <mrezanin@redhat.com> - 0.31-2
- cu-growpart-Use-LANG-C-to-parse-sfdisk-output.patch [bz#1933768]
- Resolves: bz#1933768
  (cloud-utils-growpart: Wrong parsing of sfdisk output in french locale)

* Tue Jun 23 2020 Miroslav Rezanina <mrezanin@redhat.com> - 0.31-1
- Rebase to 0.31 [bz#1846246]
- Resolves: #bz#1846246
  (cloud-util-growpart rebase to 0.31)

* Wed Sep 04 2019 Miroslav Rezanina <mrezanin@redhat.com> - 0.29-3
- Fix growpart error when partition size matches partition offset
- Resolves: rhbz#1666854
  (growpart fails when partition start sector is the same as partition size)

* Wed Apr 19 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.29-2
- Import to RHEL 7
Resolves: rhbz#1308711

* Mon Dec 05 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.29-1
- update to 0.29
- resolves rhbz#1321373

* Tue May 10 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.28-1
- fix locale related problems in growpart script (rhbz#1327620)
  w/ rebase to 0.28

* Tue May 10 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.27-14

* Tue Mar 18 2014 Lars Kellogg-Stedman <lars@redhat.com> - 0.27-13
- suppress partx usage error

* Tue Jan 14 2014 Lars Kellogg-Stedman <lars@redhat.com> - 0.27-11
- import into RHEL

