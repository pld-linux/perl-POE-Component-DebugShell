#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	POE
%define		pnam	Component-DebugShell
Summary:	POE::Component::DebugShell - interactive peeking into a running POE application
Summary(pl.UTF-8):	POE::Component::DebugShell - interaktywne podglądanie działających aplikacji POE
Name:		perl-POE-Component-DebugShell
Version:	1.412
Release:	1
License:	MIT-like (see LICENSE)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	25f238d20719aba410fdfaf8efdcabff
URL:		http://poe.perl.org/
BuildRequires:	perl-POE
BuildRequires:	perl-POE-API-Peek
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component allows for interactive peeking into a running POE
application.

%description -l pl.UTF-8
Ten komponent umożliwia interaktywne podglądanie działających
aplikacji POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{perl_vendorlib}/POE/Component/DebugShell.pm
%{_mandir}/man3/*
