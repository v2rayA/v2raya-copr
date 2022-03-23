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
Patch0:  v2raya-1.5.6-build-with-golang-1.16.patch
BuildRequires:  golang
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:	yarnpkg
Recommends:     v2ray-core
Recommends:	v2ray-rules-dat
Conflicts:      v2raya
Conflicts:      v2rayA

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
A web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel

%prep
%setup -n v2rayA-master -q
%patch0 -p1
%define BUILD_DIR %{_builddir}/v2rayA-master

%build
# build gui
cd %{BUILD_DIR}/gui
yarn --check-files
OUTPUT_DIR=%{BUILD_DIR}/service/server/router/web yarn build

#get commit id
api_result=`curl -s https://api.github.com/repos/v2rayA/v2rayA/branches/master | head -n 4 | tail -n 1`

# build core
cd %{BUILD_DIR}/service
export GO111MODULE=on
export GOPROXY=https://goproxy.io
go build -ldflags '-X github.com/v2rayA/v2rayA/conf.Version=unstable-'%{version}' -s -w' -o v2raya

%install
cd "%{BUILD_DIR}"
install -Dm 755 service/v2raya -t %{buildroot}/usr/bin/
#find web -type d -exec install -vd %{buildroot}/etc/v2raya/{} \;
#find web -type f -exec install -vm 644 {} %{buildroot}/etc/v2raya/{} \;
install -dm 750 %{buildroot}/etc/v2raya/
install -Dm 644 install/universal/v2raya.desktop -t %{buildroot}/usr/share/applications/
install -Dm 644 install/universal/v2raya.service -t %{buildroot}/usr/lib/systemd/system/
install -Dm 644 install/universal/v2raya@.service -t %{buildroot}/usr/lib/systemd/system/
install -Dm 644 gui/public/img/icons/android-chrome-512x512.png %{buildroot}/usr/share/icons/hicolor/512x512/apps/v2raya.png

%post
%postun

%files
%license LICENSE
%{_sysconfdir}/v2raya/
%{_bindir}/v2raya
%{_prefix}/lib/systemd/system/v2raya.service
%{_prefix}/lib/systemd/system/v2raya@.service
%{_datadir}/applications/v2raya.desktop
%{_datadir}/icons/hicolor/512x512/apps/v2raya.png

%changelog
* Wed Mar 23 2022 zhullyb <zhullyb@outlook.com> - 1.5.6.2-2
- Add v2ray-rules-dat as Recommends.

