#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	DHCPLeases
Summary:	-
Summary(pl.UTF-8):	-
Name:		perl-Text-DHCPLeases
Version:	0.8
Release:	0.1
# note if it is "same as perl"
#License:	GPL v1+ or Artistic
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	
#Patch0:		%{name}-foo.patch
# most of CPAN modules have generic URL (substitute pdir and pnam here)
URL:		http://search.cpan.org/dist/Text-DHCPLeases/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#BuildRequires:	-
%if %{with autodeps} || %{with tests}
#BuildRequires:	perl-
#BuildRequires:	perl-
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
This module provides an object-oriented interface to ISC DHCPD leases files.
The goal is to objectify all declarations, as defined by the ISC dhcpd package
man pages.

This interface is useful for analyzing, reporting, converting lease files, or
as a tool for other applications that need to import dhcpd lease data
structures.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/DHCPLeases.pm
%dir %{perl_vendorlib}/Text/DHCPLeases
%{perl_vendorlib}/Text/DHCPLeases/*.pm
%dir %{perl_vendorlib}/Text/DHCPLeases/Object
%{perl_vendorlib}/Text/DHCPLeases/Object/*.pm
%{_mandir}/man3/*
