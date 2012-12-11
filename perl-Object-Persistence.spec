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




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.92-6mdv2010.0
+ Revision: 430517
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.92-5mdv2009.0
+ Revision: 258145
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.92-4mdv2009.0
+ Revision: 246258
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.92-2mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Andreas Hasenack <andreas@mandriva.com> 0.92-2mdv2007.0
+ Revision: 107888
- rebuilt
- using mkrel
- Import perl-Object-Persistence

* Fri Jul 15 2005 Andreas Hasenack <andreas@mandriva.com> 0.92-1mdk
- initial Mandriva package

