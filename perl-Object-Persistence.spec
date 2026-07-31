%define real_name Object-Persistence

Summary:	Object-Persistence module for perl
Name:	perl-%{real_name}
Version:	0.92
Release:	1
License:	GPL+ or Artistic
Group:	Development/Perl
URL:	https://metacpan.org/dist/Object-Persistence
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Object-Persistence-0.92.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides persistence functionality to its objects. Object
definitions are stored as stringified perl data structures, generated with
Data::Dumper, that are amenable to manual editing and external processing from
outside the class interface.

%prep
%setup -q -n Object-Persistence-0.92

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test || :

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
