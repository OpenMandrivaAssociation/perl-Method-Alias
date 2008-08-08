%define module   Method-Alias
%define version    1.03
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Create method aliases (and do it safely)
Source:     http://www.cpan.org/modules/by-module/Method/%{module}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{module}
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Method

