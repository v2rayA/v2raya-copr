%global debug_package %{nil}

Name: v2ray
Version: 5.19.0
Release: 1%{?dist}
Summary: A platform for building proxies to bypass network restrictions
License: MIT
URL: https://github.com/v2fly/v2ray-core
Source0: https://github.com/v2fly/v2ray-core/archive/refs/tags/v%{version}.tar.gz
Obsoletes: v2ray-core <= 5.3.0

# Dependencies
Requires: glibc
Requires: v2ray-domain-list-community
Requires: v2ray-geoip

# Build dependencies
BuildRequires: golang
BuildRequires: git
BuildRequires: systemd

%description
V2Ray is a platform for building proxies to bypass network restrictions.

%prep
%autosetup -n %name-core-%{version}
sed -i 's|/usr/local/bin|/usr/bin|;s|/usr/local/etc|/etc|' release/config/systemd/system/*.service

%build
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external"
export CGO_LDFLAGS="${LDFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CPPFLAGS="${CPPFLAGS}"
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
go build -o v2ray ./main

#check
#go test -p 1 -tags json -v -timeout 30m ./...

%install
install -Dm644 release/config/systemd/system/v2ray.service -t %{buildroot}%{_unitdir}/
install -Dm644 release/config/systemd/system/v2ray@.service -t %{buildroot}%{_unitdir}/
install -Dm644 release/config/*.json -t %{buildroot}%{_sysconfdir}/v2ray/
install -Dm755 v2ray -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%config(noreplace) /etc/v2ray/*.json
%{_unitdir}/v2ray.service
%{_unitdir}/v2ray@.service
%{_bindir}/v2ray

%changelog
* Mon Sep 16 2024 zhullyb <zhullyb@outlook.com> - 5.19.0-1
- new version

* Mon Sep 09 2024 zhullyb <zhullyb@outlook.com> - 5.18.0-1
- new version

* Sun Aug 25 2024 zhullyb <zhullyb@outlook.com> - 5.17.1-1
- new version

* Sat Aug 24 2024 zhullyb <zhullyb@outlook.com> - 5.17.0-1
- new version

* Fri Aug 09 2024 zhullyb <zhullyb@outlook.com> - 5.16.1-1
- new version

* Thu Aug 08 2024 zhullyb <zhullyb@outlook.com> - null-1
- new version

* Fri Jun 07 2024 zhullyb <zhullyb@outlook.com> - 5.16.1-1
- new version

* Thu Jun 06 2024 zhullyb <zhullyb@outlook.com> - null-1
- new version

* Fri May 03 2024 zhullyb <zhullyb@outlook.com> - 5.16.1-1
- new version

* Sun Apr 28 2024 zhullyb <zhullyb@outlook.com> - 5.15.3-1
- new version

* Wed Nov 15 2023 zhullyb <zhullyb@outlook.com> - 5.10.1-1
- new version

* Thu Mar 30 2023 zhullyb <zhullyb@outlook.com> - 5.4.1-2
- mark /etc/v2ray/*.json as noreplace, thanks to github@liusen373 .

* Mon Mar 20 2023 zhullyb <zhullyb@outlook.com> - 5.4.1-1
- new version

* Sun Mar 19 2023 zhullyb <zhullyb@outlook.com> - 5.3.0-1
- First Version

