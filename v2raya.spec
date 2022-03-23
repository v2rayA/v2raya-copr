Name:           v2raya
Version:        1.5.6.2
Release:        2
Summary:        A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel
License:        AGPL-3.0
Group:          Productivity/Networking/Web/Proxy
Url:            https://github.com/v2rayA/v2rayA
Source0:        https://github.com/v2rayA/v2rayA/archive/refs/tags/v%{version}.tar.gz
Patch0:         v2raya-1.5.6-build-with-golang-1.16.patch
BuildRequires:  golang
BuildRequires:  nodejs
BuildRequires:  npm
Recommends:     v2ray-core
Recommends:     v2ray-rules-dat
Obsoletes:      v2rayA <= 1.5.5

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel

%prep
%setup -q -n v2rayA-%{version}
%patch0 -p1
%define BUILD_DIR %{_builddir}/v2rayA-%{version}

%build
# build gui
cd %{BUILD_DIR}/gui
npm install yarn
./node_modules/yarn/bin/yarn --check-files
OUTPUT_DIR=%{BUILD_DIR}/service/server/router/web ./node_modules/yarn/bin/yarn build
# build core
cd %{BUILD_DIR}/service
export GO111MODULE=on
export GOPROXY=https://goproxy.io
go build -ldflags '-X github.com/v2rayA/v2rayA/conf.Version='%{version}' -s -w' -o v2raya

%install
cd "%{BUILD_DIR}"
install -Dm 755 service/v2raya -t %{buildroot}/usr/bin/
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


