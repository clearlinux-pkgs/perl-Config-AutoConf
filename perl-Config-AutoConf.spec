#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Config-AutoConf
Version  : 0.319
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Config-AutoConf-0.319.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Config-AutoConf-0.319.tar.gz
Summary  : 'A module to implement some of AutoConf macros in pure perl.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Config-AutoConf-license = %{version}-%{release}
Requires: perl-Config-AutoConf-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)

%description
# NAME
Config::AutoConf - A module to implement some of AutoConf macros in pure perl.

%package dev
Summary: dev components for the perl-Config-AutoConf package.
Group: Development
Provides: perl-Config-AutoConf-devel = %{version}-%{release}
Requires: perl-Config-AutoConf = %{version}-%{release}

%description dev
dev components for the perl-Config-AutoConf package.


%package license
Summary: license components for the perl-Config-AutoConf package.
Group: Default

%description license
license components for the perl-Config-AutoConf package.


%package perl
Summary: perl components for the perl-Config-AutoConf package.
Group: Default
Requires: perl-Config-AutoConf = %{version}-%{release}

%description perl
perl components for the perl-Config-AutoConf package.


%prep
%setup -q -n Config-AutoConf-0.319
cd %{_builddir}/Config-AutoConf-0.319

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-AutoConf
cp %{_builddir}/Config-AutoConf-0.319/LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-AutoConf/27a14e34d2e75b1794c713418c26874bfc78d4c5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::AutoConf.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-AutoConf/27a14e34d2e75b1794c713418c26874bfc78d4c5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Config/AutoConf.pm
