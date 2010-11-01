%define realname    south
%define name   python-django-south
%define version 0.7.2
%define release %mkrel 1
%define vcstag rc1

Name: %{name}
Version: %{version}
Release: %{release}
Summary:        Intelligent schema migrations for Django apps
Group:          Development/Python
License:        ASL 2.0
URL:            http://south.aeracode.org
Source:         %{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
South brings migrations to Django applications. Its main objectives are to
provide a simple, stable and database-independent migration layer to prevent
all the hassle schema changes over time bring to your Django applications.

%files
%defattr(-,root,root,-)
%doc docs/
%{py_puresitedir}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{realname}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

