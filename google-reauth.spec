#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-reauth
Version  : 0.1.1
Release  : 20
URL      : https://files.pythonhosted.org/packages/7d/86/74242e08d24ec4c436b8325dabbd7c60422b4829dfb1ad6ec117bdebea76/google-reauth-0.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/86/74242e08d24ec4c436b8325dabbd7c60422b4829dfb1ad6ec117bdebea76/google-reauth-0.1.1.tar.gz
Summary  : Google Reauth Library
Group    : Development/Tools
License  : Apache-2.0
Requires: google-reauth-license = %{version}-%{release}
Requires: google-reauth-python = %{version}-%{release}
Requires: google-reauth-python3 = %{version}-%{release}
Requires: oauth2client
Requires: pyu2f
BuildRequires : buildreq-distutils3
BuildRequires : oauth2client
BuildRequires : pyu2f

%description
============================
        
        |build| |pypi|
        
        This library provides Reauth support to Google's authentication libraries for
        Python. Reauth allows using two-factor authentication for end-user credentials.
        
        Other than for reference purposes, this library is of little use to non-Google
        developers.

%package license
Summary: license components for the google-reauth package.
Group: Default

%description license
license components for the google-reauth package.


%package python
Summary: python components for the google-reauth package.
Group: Default
Requires: google-reauth-python3 = %{version}-%{release}

%description python
python components for the google-reauth package.


%package python3
Summary: python3 components for the google-reauth package.
Group: Default
Requires: python3-core
Provides: pypi(google_reauth)
Requires: pypi(pyu2f)

%description python3
python3 components for the google-reauth package.


%prep
%setup -q -n google-reauth-0.1.1
cd %{_builddir}/google-reauth-0.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606847949
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-reauth
cp %{_builddir}/google-reauth-0.1.1/LICENSE %{buildroot}/usr/share/package-licenses/google-reauth/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-reauth/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
