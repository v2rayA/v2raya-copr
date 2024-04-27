Name: v2ray-geoip
Version: 202404250042
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
* Sat Apr 27 2024 zhullyb <zhullyb@outlook.com> - 202404250042-1
- new version

* Fri Dec 1 2023 zhullyb <zhullyb@outlook.com> - 202311300040-1
- Update to 202311300040

* Sun Mar 19 2023 zhullyb <zhullyb@outlook.com> - 202303160048-1
- First Version

