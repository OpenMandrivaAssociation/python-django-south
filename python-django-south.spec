%define tarname    South
%define name	   python-django-south
%define version	   0.7.3
%define release	   %mkrel 1

Summary:        Migrations for Django
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:         http://pypi.python.org/packages/source/S/%{tarname}/%{tarname}-%{version}.tar.gz
Group:          Development/Python
License:        ASL 2.0
URL:            http://south.aeracode.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       python-django
BuildRequires:  python-devel, python-setuptools

%description
South is an intelligent database migrations library for the Django web
framework. It is database-independent and DVCS-friendly, as well as a
whole host of other features.

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc README


