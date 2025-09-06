Name:           btop
Version:        1.4.4
Release:        1
Summary:        A monitor of resources
License:        Apache-2.0
Vendor:         Test-Only
URL:            https://github.com/aristocratos/btop
Source0:        source.tar.gz
BuildRequires:  sed
BuildRequires:  coreutils
BuildRequires:  make

# The main compiler on leap 15.6 is version 7
%if 0%{?suse_version} < 1550 && 0%{?suse_version} != 0
BuildRequires:  gcc13-c++
%define cxxopt CXX="g++-13" CC=gcc-13

%else
BuildRequires:  gcc-c++ >= 11
%endif

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
C++ version and continuation of bashtop and bpytop.

%prep
%setup -q

%build
%make_build GPU_SUPPORT=false %{?cxxopt}

%install
%make_install PREFIX=%{_prefix} %{?cxxopt}

%files
%{_bindir}/btop

%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%{_datadir}/%{name}/themes/*.theme
%{_datadir}/%{name}/README.md

%license LICENSE
