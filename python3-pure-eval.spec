Summary:	Safely evaluate AST nodes without side effects
Name:		python3-pure-eval
Version:	0.2.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pure-eval/
Source0:	https://files.pythonhosted.org/packages/source/p/pure_eval/pure_eval-%{version}.tar.gz
# Source0-md5:	d545186f2c899d9dd273c03d71b7ffb7
URL:		http://github.com/alexmojaki/pure_eval
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:41
BuildRequires:	python3-setuptools_scm >= 3.4.3
BuildRequires:	python3-wheel
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Safely evaluate AST nodes without side effects.

%prep
%setup -q -n pure_eval-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%dir %{py3_sitescriptdir}/pure_eval
%{py3_sitescriptdir}/pure_eval/*.py
%{py3_sitescriptdir}/pure_eval/__pycache__
%{py3_sitescriptdir}/pure_eval/py.typed
%{py3_sitescriptdir}/pure_eval-%{version}.dist-info
