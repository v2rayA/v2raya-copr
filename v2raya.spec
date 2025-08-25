Name:           v2raya
Version:        2.2.7
Release:        1%{?dist}
Summary:        A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel
License:        AGPL-3.0
Group:          Productivity/Networking/Web/Proxy
Url:            https://github.com/v2rayA/v2rayA
Source0:        https://github.com/v2rayA/v2rayA/archive/refs/tags/v%{version}.tar.gz
Source1:        v2raya.conf
Source2:        dl-core.sh
BuildRequires:  wget
Recommends:     v2ray >= 5
Obsoletes:      v2rayA <= 1.5.5

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
A Linux web GUI client of Project V which supports V2Ray, Xray, SS, SSR, Trojan and Pingtunnel

%prep
%setup -q -n v2rayA-%{version}
%define BUILD_DIR %{_builddir}/v2rayA-%{version}

%build
cd %{_sourcedir}
chmod +x ./dl-core.sh
./dl-core.sh %{version}

%install
cd "%{BUILD_DIR}"
install -Dm 755 %{_sourcedir}/v2raya_linux_* %{buildroot}/usr/bin/v2raya
install -dm 750 %{buildroot}/etc/v2raya/
install -Dm 644 install/universal/v2raya.desktop -t %{buildroot}/usr/share/applications/
install -Dm 644 install/universal/v2raya.service -t %{buildroot}/usr/lib/systemd/system/
install -Dm 644 install/universal/v2raya-lite.service -t %{buildroot}/usr/lib/systemd/user/
install -Dm 644 gui/public/img/icons/android-chrome-512x512.png %{buildroot}/usr/share/icons/hicolor/512x512/apps/v2raya.png
install -Dm 644 %{S:1} %{buildroot}%{_sysconfdir}/default/v2raya

%files
%config(noreplace) %{_sysconfdir}/default/v2raya
%license LICENSE
%{_sysconfdir}/v2raya/
%{_bindir}/v2raya
%{_prefix}/lib/systemd/system/v2raya.service
%{_prefix}/lib/systemd/user/v2raya-lite.service
%{_datadir}/applications/v2raya.desktop
%{_datadir}/icons/hicolor/512x512/apps/v2raya.png

%changelog
* Mon Aug 25 2025 zhullyb <zhullyb@outlook.com> - 2.2.7-1
- new version

* Fri Mar 28 2025 zhullyb <zhullyb@outlook.com> - 2.2.6.7-1
- new version

* Mon Feb 10 2025 zhullyb <zhullyb@outlook.com> - 2.2.6.6-1
- new version

* Mon Nov 25 2024 zhullyb <zhullyb@outlook.com> - 2.2.6.3-1
- new version

* Sun Oct 27 2024 zhullyb <zhullyb@outlook.com> - 2.2.6.2-1
- new version

* Sat Oct 26 2024 zhullyb <zhullyb@outlook.com> - 2.2.6.1-1
- new version

* Fri Oct 11 2024 zhullyb <zhullyb@outlook.com> - 2.2.6-1
- new version

* Thu Aug 15 2024 zhullyb <zhullyb@outlook.com> - 2.2.5.8-1
- new version

* Wed Aug 14 2024 zhullyb <zhullyb@outlook.com> - null-1
- new version

* Wed Jul 17 2024 zhullyb <zhullyb@outlook.com> - 2.2.5.8-1
- new version

* Mon Jul 15 2024 zhullyb <zhullyb@outlook.com> - 2.2.5.7-1
- new version

* Sat Jun 22 2024 zhullyb <zhullyb@outlook.com> - 2.2.5.6-1
- new version

* Wed Jun 19 2024 zhullyb <zhullyb@outlook.com> - 2.2.5.5-1
- new version

* Wed Jun 19 2024 zhullyb <zhullyb@outlook.com> - 2.2.5.2-1
- new version

* Sun Apr 28 2024 zhullyb <zhullyb@outlook.com> - 2.2.5.1-1
- new version

* Sat Nov 18 2023 zhullyb <zhullyb@outlook.com> - 2.2.4.3-2
- fix v2raya directory

* Wed Nov 15 2023 zhullyb <zhullyb@outlook.com> - 2.2.4.3-1
- new version

* Tue Apr 11 2023 zhullyb <zhullyb@outlook.com> - 2.0.5-1
- new version

* Mon Mar 20 2023 zhullyb <zhullyb@outlook.com> - 2.0.4-2
- depend on v2ray now

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


