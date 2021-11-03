#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aesara
Version  : 2.2.6
Release  : 1
URL      : https://files.pythonhosted.org/packages/9d/be/c6c9284b71a88e1b7b9f0f949e844ac5237283faf367a14031b9c131f9d5/aesara-2.2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/be/c6c9284b71a88e1b7b9f0f949e844ac5237283faf367a14031b9c131f9d5/aesara-2.2.6.tar.gz
Summary  : Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: aesara-bin = %{version}-%{release}
Requires: aesara-license = %{version}-%{release}
Requires: aesara-python = %{version}-%{release}
Requires: aesara-python3 = %{version}-%{release}
Requires: Cython
Requires: black
Requires: coverage
Requires: dataclasses
Requires: filelock
Requires: flake8
Requires: isort
Requires: numpy
Requires: packaging
Requires: pep8
Requires: pyflakes
Requires: scipy
Requires: sympy
BuildRequires : Cython
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : dataclasses
BuildRequires : filelock
BuildRequires : flake8
BuildRequires : isort
BuildRequires : numpy
BuildRequires : packaging
BuildRequires : pep8
BuildRequires : pyflakes
BuildRequires : scipy
BuildRequires : sympy

%description
|Tests Status| |Coverage| |Gitter|
.. raw:: html
<div align="center">
<img src="./doc/images/aesara_logo_2400.png" alt="logo"></img>
</div>

%package bin
Summary: bin components for the aesara package.
Group: Binaries
Requires: aesara-license = %{version}-%{release}

%description bin
bin components for the aesara package.


%package license
Summary: license components for the aesara package.
Group: Default

%description license
license components for the aesara package.


%package python
Summary: python components for the aesara package.
Group: Default
Requires: aesara-python3 = %{version}-%{release}

%description python
python components for the aesara package.


%package python3
Summary: python3 components for the aesara package.
Group: Default
Requires: python3-core
Provides: pypi(aesara)
Requires: pypi(filelock)
Requires: pypi(numpy)
Requires: pypi(scipy)

%description python3
python3 components for the aesara package.


%prep
%setup -q -n aesara-2.2.6
cd %{_builddir}/aesara-2.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635979452
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aesara
cp %{_builddir}/aesara-2.2.6/LICENSE.txt %{buildroot}/usr/share/package-licenses/aesara/6bd1ba47b8f18885eec96c7b3e851a77323ace0e
cp %{_builddir}/aesara-2.2.6/doc/LICENSE.txt %{buildroot}/usr/share/package-licenses/aesara/6bd1ba47b8f18885eec96c7b3e851a77323ace0e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aesara-cache

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aesara/6bd1ba47b8f18885eec96c7b3e851a77323ace0e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
