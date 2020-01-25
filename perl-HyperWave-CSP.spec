#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require server connection

%define		pdir	HyperWave
%define		pnam	CSP
Summary:	HyperWave::CSP - communicate with a HyperWave server
Summary(pl.UTF-8):	HyperWave::CSP - łączenie z serwerem HyperWave
Name:		perl-HyperWave-CSP
Version:	0.03.1
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a596136b7b87e7db9396a0c2aa3d26a4
URL:		http://search.cpan.org/dist/HyperWave-CSP/
BuildRequires:	perl-Locale-Codes
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HyperWave::CSP is a class implementing a simple HyperWave client in
Perl.

%description -l pl.UTF-8
Klasa HyperWave::CSP jest implementacją w Perlu prostego klienta
HyperWave.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/HyperWave
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
