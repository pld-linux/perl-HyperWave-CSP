%include	/usr/lib/rpm/macros.perl
%define		pdir	HyperWave
%define		pnam	CSP
Summary:	HyperWave::CSP Perl module
Summary(cs):	Modul HyperWave::CSP pro Perl
Summary(da):	Perlmodul HyperWave::CSP
Summary(de):	HyperWave::CSP Perl Modul
Summary(es):	M�dulo de Perl HyperWave::CSP
Summary(fr):	Module Perl HyperWave::CSP
Summary(it):	Modulo di Perl HyperWave::CSP
Summary(ja):	HyperWave::CSP Perl �⥸�塼��
Summary(ko):	HyperWave::CSP �� ����
Summary(no):	Perlmodul HyperWave::CSP
Summary(pl):	Modu� Perla HyperWave::CSP
Summary(pt):	M�dulo de Perl HyperWave::CSP
Summary(pt_BR):	M�dulo Perl HyperWave::CSP
Summary(ru):	������ ��� Perl HyperWave::CSP
Summary(sv):	HyperWave::CSP Perlmodul
Summary(uk):	������ ��� Perl HyperWave::CSP
Summary(zh_CN):	HyperWave::CSP Perl ģ��
Name:		perl-HyperWave-CSP
Version:	0.03.1
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a596136b7b87e7db9396a0c2aa3d26a4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Locale-Codes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HyperWave::CSP is a class implementing a simple HyperWave client in
Perl.

%description -l pl
HyperWave::CSP jest implementacj� prostego klienta HyperWave dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/HyperWave
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
