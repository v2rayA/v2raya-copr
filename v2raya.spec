Name:           v2rayA
Version:        1.4.4
Release:        1
Summary:        A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel
License:        GPL-3.0-only
Group:          Productivity/Networking/Web/Proxy
Url:            https://github.com/v2rayA/v2rayA
Source0:        https://github.com/v2rayA/v2rayA/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang
BuildRequires:  nodejs
BuildRequires:  python2
BuildRequires:  yarnpkg
Recommends:     v2ray-core

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel

%prep
%setup -q
%define BUILD_DIR %{_builddir}/v2rayA-%{version}

%build
# build gui
cd %{BUILD_DIR}/gui
yarn --check-files
OUTPUT_DIR=%{BUILD_DIR}/service/server/router/web yarn build
# build core
cd %{BUILD_DIR}/service
export GO111MODULE=on
export GOPROXY=https://goproxy.io
go build -ldflags '-X github.com/v2rayA/v2rayA/global.Version=unstable -s -w' -o v2raya

%install
cd "%{BUILD_DIR}"
install -Dm 755 service/v2raya -t %{buildroot}/usr/bin/
install -dm 750 %{buildroot}/etc/v2raya/
install -Dm 644 install/universal/v2raya.desktop -t %{buildroot}/usr/share/applications/
install -Dm 644 install/universal/v2raya.service -t %{buildroot}/usr/lib/systemd/system/
#install -Dm 644 install/universal/v2raya@.service -t %{buildroot}/usr/lib/systemd/system/
install -Dm 644 gui/public/img/icons/android-chrome-512x512.png %{buildroot}/usr/share/icons/hicolor/512x512/apps/v2raya.png

%post
%postun

%files
/etc/v2raya/
/usr/bin/v2raya
/usr/lib/systemd/system/v2raya.service
#/usr/lib/systemd/system/v2raya@.service
/usr/share/applications/v2raya.desktop
/usr/share/icons/hicolor/512x512/apps/v2raya.png

%changelog

