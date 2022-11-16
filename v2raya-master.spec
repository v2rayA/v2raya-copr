%global debug_package %{nil}
%global forgeurl https://github.com/v2rayA/v2raya
%global branch master
%global timenow %(echo $(TZ='Asia/Shanghai' date +%Y%m%d.%H%M))
%global commit_id %(api_result=$(curl -s https://api.github.com/repos/v2rayA/v2rayA/branches/master | head -n 4 | tail -n 1); echo ${api_result:12:7})
%forgemeta

Name:    v2raya-master
Version: %{timenow}.%{commit_id}
Release: 0.gitmaster
Summary: A web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel
License: AGPL-3.0
Group:   Productivity/Networking/Web/Proxy
URL:	 %{forgeurl}
Source:  %{forgesource}
BuildRequires:  golang >= 1.18
BuildRequires:  nodejs
BuildRequires:	yarnpkg
BuildRequires:  systemd
Recommends:     v2ray-core
Conflicts:      v2raya
Conflicts:      v2rayA

%description
A web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel

%prep
%setup -n v2rayA-feat_v5 -q
%define BUILD_DIR %{_builddir}/v2rayA-feat_v5

%build
# build gui
cd %{BUILD_DIR}/gui
export NODE_OPTIONS=--openssl-legacy-provider
yarn --check-files
OUTPUT_DIR=%{BUILD_DIR}/service/server/router/web yarn build

# build core
cd %{BUILD_DIR}/service
export GO111MODULE=on
export GOPROXY=https://goproxy.io
go build -ldflags '-X github.com/v2rayA/v2rayA/conf.Version=unstable-'%{version}' -s -w' -o v2raya

%install
cd "%{BUILD_DIR}"
install -Dm 755 service/v2raya -t %{buildroot}%{_bindir}/
install -dm 750 %{buildroot}/etc/v2raya/
install -Dm 644 install/universal/v2raya.desktop -t %{buildroot}%{_datadir}/applications/
install -Dm 644 install/universal/v2raya.service -t %{buildroot}%{_unitdir}/
install -Dm 644 install/universal/v2raya-lite.service -t %{buildroot}%{_userunitdir}/
install -Dm 644 gui/public/img/icons/android-chrome-512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/v2raya.png

%files
%license LICENSE
%{_sysconfdir}/v2raya/
%{_bindir}/v2raya
%{_unitdir}/v2raya.service
%{_userunitdir}/v2raya-lite.service
%{_datadir}/applications/v2raya.desktop
%{_datadir}/icons/hicolor/512x512/apps/v2raya.png

%changelog
* Wed Jul 20 2022 zhullyb <zhullyb@outlook.com> - 20220720.2200.288cd62-0.gitmaster
- rebuilt with go 1.18.4

* Wed Apr 20 2022 zhullyb <zhullyb@outlook.com> - 1.5.6.2-4
- v2raya@.sercive -> v2raya-lite.service

* Wed Mar 23 2022 zhullyb <zhullyb@outlook.com> - 1.5.6.2-3
- Add v2ray-rules-dat as Recommends.

