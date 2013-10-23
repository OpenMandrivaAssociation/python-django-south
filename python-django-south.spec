%define tarname    South

Summary:        Migrations for Django
Name:		    python-django-south
Version:	    0.8.2
Release:	    1
Source:         http://www.aeracode.org/releases/south/south-%{version}.tar.gz
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
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc README




%changelog
* Mon Dec 12 2011 Lev Givon <lev@mandriva.org> 0.7.3-1
+ Revision: 740576
- Update to 0.7.3.

* Mon Nov 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7.2-1mdv2011.0
+ Revision: 591685
- import python-django-south


