%bcond_without python2

Summary:	Database migration library for Django

Name:		python-django-south
Version:	1.0.2
Release:	1
Source0:	https://pypi.python.org/packages/e3/11/10a986f30ce1a1d5209b192c68adcc3eaf312f9caba70b35c0ac6e354a6b/South-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/django-south
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
Requires:	python-django

%description
Database migration library for Django

%if %{with python2}
%package -n python2-django-south
Summary:	Database migration library for Django
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
Requires:	python2-django

%description -n python2-django-south
Database migration library for Django
%endif

%prep
%setup -qc
mv South-%{version} python3

%if %{with python2}
cp -r python3 python2
%endif

%build
%if %{with python2}
cd python2
python2 setup.py build
cd ..
%endif

cd python3
python setup.py build
cd ..

%install
%if %{with python2}
cd python2
python2 setup.py install --skip-build --root %{buildroot}
cd ..
%endif

cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%files
%{py_puresitedir}/*

%if %{with python2}
%files -n python2-django-south
%{py2_puresitedir}/*
%endif
