%include	/usr/lib/rpm/macros.perl
%define		pdir	HyperWave
%define		pnam	CSP
Summary:	HyperWave::CSP Perl module
Summary(cs):	Modul HyperWave::CSP pro Perl
Summary(da):	Perlmodul HyperWave::CSP
Summary(de):	HyperWave::CSP Perl Modul
Summary(es):	Módulo de Perl HyperWave::CSP
Summary(fr):	Module Perl HyperWave::CSP
Summary(it):	Modulo di Perl HyperWave::CSP
Summary(ja):	HyperWave::CSP Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	HyperWave::CSP ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul HyperWave::CSP
Summary(pl):	Modu³ Perla HyperWave::CSP
Summary(pt):	Módulo de Perl HyperWave::CSP
Summary(pt_BR):	Módulo Perl HyperWave::CSP
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl HyperWave::CSP
Summary(sv):	HyperWave::CSP Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl HyperWave::CSP
Summary(zh_CN):	HyperWave::CSP Perl Ä£¿é
Name:		perl-HyperWave-CSP
Version:	0.03.1
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Locale-Codes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HyperWave::CSP is a class implementing a simple HyperWave client in
Perl.

%description -l pl
HyperWave::CSP jest implementacj± prostego klienta HyperWave dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_sitelib}/HyperWave
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
