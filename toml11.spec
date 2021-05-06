%global debug_package %{nil}

Name:               toml11
Version:            3.6.1
Release:            1%{?dist}
Summary:            Toml parser/encoder C++11 header-only library
License:            MIT

URL:                https://github.com/ToruNiina/%{name}/
Source0:            https://github.com/ToruNiina/%{name}/archive/v%{version}.tar.gz

BuildRequires:      cmake
BuildRequires:      make
BuildRequires:      gcc-c++

%description
A C++11 header-only toml parser/encoder. Compliant with TOML v1.0.0.

%package devel
Summary:            Toml parser/encoder C++11 header-only library
Provides:           %{name}-static = %{version}-%{release}
Provides:           %{name} = %{version}-%{release}
Requires:           libstdc++-devel

%description devel
A C++11 header-only toml parser/encoder. Compliant with TOML v1.0.0.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir $RPM_BUILD_ROOT/%{_includedir}/toml11
mv $RPM_BUILD_ROOT%{_includedir}/toml $RPM_BUILD_ROOT%{_includedir}/toml.hpp $RPM_BUILD_ROOT%{_includedir}/toml11

%check
%ctest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/toml11
%{_libdir}/cmake

%changelog
