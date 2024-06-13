Name: v2ray-geoip
Version: 202406130042
Release: 1%{?dist}
Summary: GeoIP List for V2Ray
License: CCPL:by-sa
URL: https://github.com/v2fly/geoip
Source0: https://github.com/v2fly/geoip/releases/download/%{version}/geoip.dat
BuildArch: noarch

%description
GeoIP List for V2Ray.


%install
install -Dm644 %{SOURCE0} %{buildroot}%{_datadir}/v2ray/geoip.dat

%files
%{_datadir}/v2ray/geoip.dat

%changelog
* Thu Jun 13 2024 zhullyb <zhullyb@outlook.com> - 202406130042-1
- new version

* Thu Jun 06 2024 zhullyb <zhullyb@outlook.com> - 202406060042-1
- new version

* Wed Jun 05 2024 zhullyb <zhullyb@outlook.com> - 202406042148-1
- new version

* Thu May 30 2024 zhullyb <zhullyb@outlook.com> - 202405300042-1
- new version

* Thu May 23 2024 zhullyb <zhullyb@outlook.com> - 202405230041-1
- new version

* Thu May 16 2024 zhullyb <zhullyb@outlook.com> - 202405160040-1
- new version

* Thu May 09 2024 zhullyb <zhullyb@outlook.com> - 202405090040-1
- new version

* Thu May 02 2024 zhullyb <zhullyb@outlook.com> - 202405020039-1
- new version

* Sat Apr 27 2024 zhullyb <zhullyb@outlook.com> - 202404250042-1
- new version

* Fri Dec 1 2023 zhullyb <zhullyb@outlook.com> - 202311300040-1
- Update to 202311300040

* Sun Mar 19 2023 zhullyb <zhullyb@outlook.com> - 202303160048-1
- First Version

