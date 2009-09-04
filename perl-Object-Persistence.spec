%define real_name Object-Persistence

Summary:	Object-Persistence module for perl 
Name:		perl-%{real_name}
Version:	0.92
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides persistence functionality to its objects.  Object
definitions are stored as stringified perl data structures, generated with
Data::Dumper, that are amenable to manual editing and external processing from
outside the class interface.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/Persistence/Database.pm
%{perl_vendorlib}/Persistence/Object
%{_mandir}/*/*


