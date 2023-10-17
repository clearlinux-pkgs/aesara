#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v2
# autospec commit: f032afc
#
Name     : aesara
Version  : 2.9.2
Release  : 50
URL      : https://files.pythonhosted.org/packages/3d/8b/430c44b7d939903d175b86aa241156beae8b53a8440bd445e517aa4793c2/aesara-2.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/8b/430c44b7d939903d175b86aa241156beae8b53a8440bd445e517aa4793c2/aesara-2.9.2.tar.gz
Summary  : A library for defining, optimizing, and efficiently evaluating mathematical expressions involving multi-dimensional arrays.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: aesara-bin = %{version}-%{release}
Requires: aesara-license = %{version}-%{release}
Requires: aesara-python = %{version}-%{release}
Requires: aesara-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(black)
BuildRequires : pypi(coverage)
BuildRequires : pypi(cython)
BuildRequires : pypi(diff_cover)
BuildRequires : pypi(filelock)
BuildRequires : pypi(flake8)
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi(isort)
BuildRequires : pypi(jax)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pep8)
BuildRequires : pypi(pre_commit)
BuildRequires : pypi(pyflakes)
BuildRequires : pypi(sympy)
BuildRequires : pypi(typing_extensions)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<div align="center">
<img src="./doc/images/aesara_logo_2400.png" alt="logo"></img>

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
%setup -q -n aesara-2.9.2
cd %{_builddir}/aesara-2.9.2
pushd ..
cp -a aesara-2.9.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697571484
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aesara
cp %{_builddir}/aesara-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/aesara/ea5c9ac477dae597636ac35bd89b6d1aba99565b || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
/usr/share/package-licenses/aesara/ea5c9ac477dae597636ac35bd89b6d1aba99565b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
