Name: v2ray-domain-list-community
Version: 20240707162925
Release: 1%{?dist}
Summary: A list of domains to be used as geosites for routing purpose in Project V
License: MIT
URL: https://github.com/v2fly/domain-list-community
Source0: %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires: golang
BuildRequires: git
BuildArch: noarch

%description
%{summary}

%prep
%autosetup -n domain-list-community-%{version}

%build
go run main.go

%install
install -Dm 644 dlc.dat %{buildroot}%{_datadir}/v2ray/geosite.dat
install -Dm 644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%license LICENSE
%{_datadir}/v2ray/geosite.dat

%changelog
* Mon Jul 08 2024 zhullyb <zhullyb@outlook.com> - 20240707162925-1
- new version

* Tue Jun 25 2024 zhullyb <zhullyb@outlook.com> - 20240624143214-1
- new version

* Sat Jun 22 2024 zhullyb <zhullyb@outlook.com> - 20240621160143-1
- new version

* Sat Jun 15 2024 zhullyb <zhullyb@outlook.com> - 20240614093027-1
- new version

* Thu Jun 13 2024 zhullyb <zhullyb@outlook.com> - 20240612095513-1
- new version

* Wed Jun 05 2024 zhullyb <zhullyb@outlook.com> - 20240604215500-1
- new version

* Thu May 09 2024 zhullyb <zhullyb@outlook.com> - 20240508170917-1
- new version

* Mon May 06 2024 zhullyb <zhullyb@outlook.com> - 20240505132300-1
- new version

* Sun May 05 2024 zhullyb <zhullyb@outlook.com> - 20240504141043-1
- new version

* Sat Apr 27 2024 zhullyb <zhullyb@outlook.com> - 20240426060244-1
- new version

* Fri Dec 01 2023 zhullyb <zhullyb@outlook.com> - 20231128180936-1
- new version

* Sun Mar 19 2023 zhullyb <zhullyb@outlook.com> - 20230318081709-1
- First Version

