%include	/usr/lib/rpm/macros.perl
Summary:	HyperWave-CSP perl module
Summary(pl):	Modu³ perla HyperWave-CSP
Name:		perl-HyperWave-CSP
Version:	0.03.1
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HyperWave/HyperWave-CSP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Locale-Codes
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HyperWave-CSP is a class implementing a simple HyperWave client in Perl.

%description -l pl
HyperWave-CSP jest implementacj± prostego klienta HyperWave dla perla.

%prep
%setup -q -n HyperWave-CSP-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HyperWave/CSP
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitelib}/HyperWave/CSP.pm
%{perl_sitelib}/HyperWave/CSP
%{perl_sitearch}/auto/HyperWave/CSP

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
