#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aesara
Version  : 2.8.7
Release  : 41
URL      : https://files.pythonhosted.org/packages/93/f9/147e7aa2faf062f8b444947f009f6b20a3d8c4037232558ef8b5e9848cdc/aesara-2.8.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/f9/147e7aa2faf062f8b444947f009f6b20a3d8c4037232558ef8b5e9848cdc/aesara-2.8.7.tar.gz
Summary  : Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: aesara-bin = %{version}-%{release}
Requires: aesara-license = %{version}-%{release}
Requires: aesara-python = %{version}-%{release}
Requires: aesara-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(black)
BuildRequires : pypi(cons)
BuildRequires : pypi(coverage)
BuildRequires : pypi(cython)
BuildRequires : pypi(diff_cover)
BuildRequires : pypi(etuples)
BuildRequires : pypi(filelock)
BuildRequires : pypi(flake8)
BuildRequires : pypi(isort)
BuildRequires : pypi(jax)
BuildRequires : pypi(logical_unification)
BuildRequires : pypi(minikanren)
BuildRequires : pypi(numpy)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pep8)
BuildRequires : pypi(pre_commit)
BuildRequires : pypi(pyflakes)
BuildRequires : pypi(scipy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sympy)
BuildRequires : pypi(typing_extensions)

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
Requires: pypi(black)
Requires: pypi(cons)
Requires: pypi(coverage)
Requires: pypi(cython)
Requires: pypi(diff_cover)
Requires: pypi(etuples)
Requires: pypi(filelock)
Requires: pypi(flake8)
Requires: pypi(isort)
Requires: pypi(jax)
Requires: pypi(logical_unification)
Requires: pypi(minikanren)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(pep8)
Requires: pypi(pre_commit)
Requires: pypi(pyflakes)
Requires: pypi(scipy)
Requires: pypi(setuptools)
Requires: pypi(sympy)
Requires: pypi(typing_extensions)

%description python3
python3 components for the aesara package.


%prep
%setup -q -n aesara-2.8.7
cd %{_builddir}/aesara-2.8.7
pushd ..
cp -a aesara-2.8.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664978031
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aesara
cp %{_builddir}/aesara-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/aesara/6bd1ba47b8f18885eec96c7b3e851a77323ace0e || :
cp %{_builddir}/aesara-%{version}/doc/LICENSE.txt %{buildroot}/usr/share/package-licenses/aesara/6bd1ba47b8f18885eec96c7b3e851a77323ace0e || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python*/site-packages/bin/__init__.py
rm -f %{buildroot}*/usr/lib/python*0/site-packages/bin/__pycache__/__init__.cpython-*.pyc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
