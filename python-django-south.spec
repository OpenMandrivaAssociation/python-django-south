%define tarname    South

Summary:        Migrations for Django

Name:		    python-django-south
Version:	    1.0
Release:	    1
Source:         https://pypi.python.org/packages/source/S/South/South-%{version}.tar.gz
Group:          Development/Python
License:        ASL 2.0
URL:            http://south.aeracode.org/
BuildArch:      noarch
Requires:       python-django
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
South is an intelligent database migrations library for the Django web
framework. It is database-independent and DVCS-friendly, as well as a
whole host of other features.

%prep
%setup -q -n %{tarname}-%{version}

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc README
