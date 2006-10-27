#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-DebugShell
Summary:	POE::Component::DebugShell - interactive peeking into a running POE application
Summary(pl):	POE::Component::DebugShell - interaktywne podgl±danie dzia³aj±cych aplikacji POE
Name:		perl-POE-Component-DebugShell
Version:	1.0411
Release:	1
License:	MIT-like (see LICENSE)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68aa0496f6ded9e221100c22351a05e5
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

%description -l pl
Ten komponent umo¿liwia interaktywne podgl±danie dzia³aj±cych
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
%doc Changes LICENSE
%{perl_vendorlib}/POE/Component/DebugShell.pm
%{_mandir}/man3/*
