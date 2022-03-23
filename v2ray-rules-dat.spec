%global debug_package %{nil}

Version: %(api_result=$(curl -s https://api.github.com/repos/v2rayA/dist-v2ray-rules-dat/tags | head -n 3 | tail -n 1); echo ${api_result:13:12})

Name:    v2ray-rules-dat
Release: 1%{?dist}
License: GPL-3.0
Summary: Dist of Loyalsoldier/v2ray-rules-dat
Url:	 https://github.com/v2rayA/dist-v2ray-rules-dat
Source0: %{url}/archive/refs/tags/%{version}.tar.gz
Source1: https://www.gnu.org/licenses/gpl-3.0.txt
BuildArch: noarch

%description
%{summary}

%prep
%autosetup -n dist-%{name}-%{version}

%build
cp %{S:1} ./LICENSE

%install
install -Dm644 geoip.dat -t %{buildroot}%{_prefix}/local/share/v2ray
install -Dm644 geosite.dat -t %{buildroot}%{_prefix}/local/share/v2ray
ln -s /usr/local/share/v2ray/geosite.dat %{buildroot}%{_prefix}/local/share/v2ray/LoyalsoldierSite.dat

%files
%license LICENSE
%{_prefix}/local/share/v2ray/geoip.dat
%{_prefix}/local/share/v2ray/geosite.dat
%{_prefix}/local/share/v2ray/LoyalsoldierSite.dat


%changelog
