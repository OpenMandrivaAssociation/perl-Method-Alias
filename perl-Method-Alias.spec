%define module   Method-Alias

Name:		perl-%{module}
Version:	1.03
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Create method aliases (and do it safely)
Source:		http://www.cpan.org/modules/by-module/Method/%{module}-%{version}.tar.gz
Url:		https://search.cpan.org/dist/%{module}

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
For a very long time, whenever I wanted to have a method alias (provide an
alternate name for a method) I would simple do a GLOB alias. That is,

  # My method
  sub foo {
      ...
  }
  
  # Alias the method
  *bar = *foo;

While this works fine for functions, it does *not* work for methods.

%prep
%setup -q -n %{module}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Method

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.03-3mdv2010.0
+ Revision: 430503
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.03-2mdv2009.0
+ Revision: 268615
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.0
+ Revision: 213799
- import perl-Method-Alias


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.0
- first mdv release
