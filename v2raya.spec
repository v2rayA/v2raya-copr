Name:           v2raya
Version:        2.0.4
Release:        1%{?dist}
Summary:        A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel
License:        AGPL-3.0
Group:          Productivity/Networking/Web/Proxy
Url:            https://github.com/v2rayA/v2rayA
Source0:        https://github.com/v2rayA/v2rayA/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang >= 1.17
BuildRequires:  nodejs >= 17
BuildRequires:  yarn
Recommends:     v2ray-core >= 5
Obsoletes:      v2rayA <= 1.5.5

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel

%prep
%setup -q -n v2rayA-%{version}
%define BUILD_DIR %{_builddir}/v2rayA-%{version}

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
go build -ldflags '-X github.com/v2rayA/v2rayA/conf.Version='%{version}' -s -w' -o v2raya

%install
cd "%{BUILD_DIR}"
install -Dm 755 service/v2raya -t %{buildroot}/usr/bin/
install -dm 750 %{buildroot}/etc/v2raya/
install -Dm 644 install/universal/v2raya.desktop -t %{buildroot}/usr/share/applications/
install -Dm 644 install/universal/v2raya.service -t %{buildroot}/usr/lib/systemd/system/
install -Dm 644 install/universal/v2raya-lite.service -t %{buildroot}/usr/lib/systemd/user/
install -Dm 644 gui/public/img/icons/android-chrome-512x512.png %{buildroot}/usr/share/icons/hicolor/512x512/apps/v2raya.png

%files
%license LICENSE
%{_sysconfdir}/v2raya/
%{_bindir}/v2raya
%{_prefix}/lib/systemd/system/v2raya.service
%{_prefix}/lib/systemd/user/v2raya-lite.service
%{_datadir}/applications/v2raya.desktop
%{_datadir}/icons/hicolor/512x512/apps/v2raya.png

%changelog
* Mon Mar 20 2023 zhullyb <zhullyb@outlook.com> - 2.0.4-1
- new version

* Wed Dec 14 2022 zhullyb <zhullyb@outlook.com> - 2.0.1-1
- new version

* Sat Dec 10 2022 zhullyb <zhullyb@outlook.com> - 2.0.0-1
- new version

* Thu Aug 04 2022 zhullyb <zhullyb@outlook.com> - 1.5.9.1698.1-1
- new version

* Sun Jun 19 2022 zhullyb <zhullyb@outlook.com> - 1.5.8.1-1
- new version

* Tue May 24 2022 zhullyb <zhullyb@outlook.com> - 1.5.7-2
- Backport
  https://github.com/v2rayA/v2rayA/commit/b47214108188d5c2772848db1c96c422493f2051

* Thu Apr 21 2022 zhullyb <zhullyb@outlook.com> - 1.5.7-1
- new version
- v2raya@.sercive -> v2raya-lite.service

* Wed Mar 23 2022 zhullyb <zhullyb@outlook.com> - 1.5.6.2-2
- Add v2ray-rules-dat as Recommends.


