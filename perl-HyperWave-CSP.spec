%include	/usr/lib/rpm/macros.perl
Summary:	HyperWave-CSP perl module
Summary(pl):	Modu� perla HyperWave-CSP
Name:		perl-HyperWave-CSP
Version:	0.03.1
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HyperWave/HyperWave-CSP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Locale-Codes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HyperWave-CSP is a class implementing a simple HyperWave client in
Perl.

%description -l pl
HyperWave-CSP jest implementacj� prostego klienta HyperWave dla perla.

%prep
%setup -q -n HyperWave-CSP-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HyperWave/CSP.pm
%{perl_sitelib}/HyperWave/CSP
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
