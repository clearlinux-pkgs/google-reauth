#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-reauth
Version  : 0.1.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/88/a9/68e764f071560fc947ce23944b10b2d7e8dc4ae0cf853565ef4e1e47f69e/google-reauth-0.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/a9/68e764f071560fc947ce23944b10b2d7e8dc4ae0cf853565ef4e1e47f69e/google-reauth-0.1.0.tar.gz
Summary  : Google Reauth Library
Group    : Development/Tools
License  : Apache-2.0
Requires: google-reauth-license = %{version}-%{release}
Requires: google-reauth-python = %{version}-%{release}
Requires: google-reauth-python3 = %{version}-%{release}
Requires: oauth2client
Requires: pyu2f
BuildRequires : buildreq-distutils3

%description
============================
        
        |build| |docs| |pypi|
        
        This library provides Reauth support to Google's authentication libraries for
        Python. Reauth allows using two-factor authentication for end-user credentials.

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

%description python3
python3 components for the google-reauth package.


%prep
%setup -q -n google-reauth-0.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546109112
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-reauth
cp LICENSE %{buildroot}/usr/share/package-licenses/google-reauth/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-reauth/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
