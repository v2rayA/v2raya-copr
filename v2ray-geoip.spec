Name: v2ray-geoip
Version: 202511210201
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
* Sat Nov 22 2025 zhullyb <zhullyb@outlook.com> - 202511210201-1
- new version

* Thu Nov 06 2025 zhullyb <zhullyb@outlook.com> - 202511050144-1
- new version

* Mon Oct 06 2025 zhullyb <zhullyb@outlook.com> - 202510050144-1
- new version

* Sat Sep 06 2025 zhullyb <zhullyb@outlook.com> - 202509050142-1
- new version

* Thu Aug 14 2025 zhullyb <zhullyb@outlook.com> - 202508140022-1
- new version

* Sun Aug 10 2025 zhullyb <zhullyb@outlook.com> - 202508091008-1
- new version

* Wed Aug 06 2025 zhullyb <zhullyb@outlook.com> - 202508050201-1
- new version

* Sun Jul 06 2025 zhullyb <zhullyb@outlook.com> - 202507050144-1
- new version

* Fri Jun 06 2025 zhullyb <zhullyb@outlook.com> - 202506050146-1
- new version

* Tue May 06 2025 zhullyb <zhullyb@outlook.com> - 202505050146-1
- new version

* Sun Apr 06 2025 zhullyb <zhullyb@outlook.com> - 202504050136-1
- new version

* Sat Mar 29 2025 zhullyb <zhullyb@outlook.com> - 202503281421-1
- new version

* Thu Mar 06 2025 zhullyb <zhullyb@outlook.com> - 202503050126-1
- new version

* Thu Feb 06 2025 zhullyb <zhullyb@outlook.com> - 202502050123-1
- new version

* Sun Jan 19 2025 zhullyb <zhullyb@outlook.com> - 202501190004-1
- new version

* Thu Jan 16 2025 zhullyb <zhullyb@outlook.com> - 202501160051-1
- new version

* Thu Jan 09 2025 zhullyb <zhullyb@outlook.com> - 202501090053-1
- new version

* Thu Jan 02 2025 zhullyb <zhullyb@outlook.com> - 202501020052-1
- new version

* Thu Dec 26 2024 zhullyb <zhullyb@outlook.com> - 202412260052-1
- new version

* Sat Dec 21 2024 zhullyb <zhullyb@outlook.com> - 202412201411-1
- new version

* Thu Dec 19 2024 zhullyb <zhullyb@outlook.com> - 202412190056-1
- new version

* Thu Dec 12 2024 zhullyb <zhullyb@outlook.com> - 202412120057-1
- new version

* Thu Dec 05 2024 zhullyb <zhullyb@outlook.com> - 202412050058-1
- new version

* Thu Nov 28 2024 zhullyb <zhullyb@outlook.com> - 202411280056-1
- new version

* Thu Nov 21 2024 zhullyb <zhullyb@outlook.com> - 202411210054-1
- new version

* Thu Nov 14 2024 zhullyb <zhullyb@outlook.com> - 202411140052-1
- new version

* Thu Nov 07 2024 zhullyb <zhullyb@outlook.com> - 202411070052-1
- new version

* Wed Nov 06 2024 zhullyb <zhullyb@outlook.com> - 202411051341-1
- new version

* Thu Oct 31 2024 zhullyb <zhullyb@outlook.com> - 202410310053-1
- new version

* Thu Oct 24 2024 zhullyb <zhullyb@outlook.com> - 202410240052-1
- new version

* Thu Oct 17 2024 zhullyb <zhullyb@outlook.com> - 202410170052-1
- new version

* Thu Oct 10 2024 zhullyb <zhullyb@outlook.com> - 202410100052-1
- new version

* Wed Oct 09 2024 zhullyb <zhullyb@outlook.com> - 202410090012-1
- new version

* Thu Oct 03 2024 zhullyb <zhullyb@outlook.com> - 202410030052-1
- new version

* Thu Sep 26 2024 zhullyb <zhullyb@outlook.com> - 202409260052-1
- new version

* Thu Sep 19 2024 zhullyb <zhullyb@outlook.com> - 202409190051-1
- new version

* Thu Sep 12 2024 zhullyb <zhullyb@outlook.com> - 202409120050-1
- new version

* Thu Sep 05 2024 zhullyb <zhullyb@outlook.com> - 202409050049-1
- new version

* Sun Sep 01 2024 zhullyb <zhullyb@outlook.com> - 202408310351-1
- new version

* Thu Aug 29 2024 zhullyb <zhullyb@outlook.com> - 202408290048-1
- new version

* Thu Aug 22 2024 zhullyb <zhullyb@outlook.com> - 202408220047-1
- new version

* Fri Aug 16 2024 zhullyb <zhullyb@outlook.com> - 202408150441-1
- new version

* Thu Aug 15 2024 zhullyb <zhullyb@outlook.com> - 202408150044-1
- new version

* Sun Aug 11 2024 zhullyb <zhullyb@outlook.com> - 202408101831-1
- new version

* Thu Aug 08 2024 zhullyb <zhullyb@outlook.com> - 202408080046-1
- new version

* Sun Aug 04 2024 zhullyb <zhullyb@outlook.com> - 202408032148-1
- new version

* Thu Aug 01 2024 zhullyb <zhullyb@outlook.com> - 202408010050-1
- new version

* Thu Jul 25 2024 zhullyb <zhullyb@outlook.com> - 202407250045-1
- new version

* Sat Jul 20 2024 zhullyb <zhullyb@outlook.com> - 202407192357-1
- new version

* Thu Jul 18 2024 zhullyb <zhullyb@outlook.com> - 202407180044-1
- new version

* Thu Jul 11 2024 zhullyb <zhullyb@outlook.com> - 202407110044-1
- new version

* Thu Jul 04 2024 zhullyb <zhullyb@outlook.com> - 202407040043-1
- new version

* Thu Jun 27 2024 zhullyb <zhullyb@outlook.com> - 202406270043-1
- new version

* Thu Jun 20 2024 zhullyb <zhullyb@outlook.com> - 202406200042-1
- new version

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

