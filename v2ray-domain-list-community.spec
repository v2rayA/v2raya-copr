Name: v2ray-domain-list-community
Version: 20250302153845
Release: 1%{?dist}
Summary: A list of domains to be used as geosites for routing purpose in Project V
License: MIT
URL: https://github.com/v2fly/domain-list-community
Source0: %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires: golang
BuildRequires: git
BuildArch: noarch

%description
%{summary}

%prep
%autosetup -n domain-list-community-%{version}

ARCH=$(uname -m)
if [ "$ARCH" == "x86_64" ]; then
    ARCH="amd64"
elif [ "$ARCH" == "aarch64" ]; then
    ARCH="arm64"
fi
LATEST_GO_VERSION="$(curl --silent https://go.dev/VERSION?m=text | head -n 1)";
LATEST_GO_DOWNLOAD_URL="https://go.dev/dl/${LATEST_GO_VERSION}.linux-${ARCH}.tar.gz"
cd $HOME
curl -OJ -L --progress-bar $LATEST_GO_DOWNLOAD_URL
tar -xf ${LATEST_GO_VERSION}.linux-${ARCH}.tar.gz

%build
export GOROOT="$HOME/go"
export GOPATH="$HOME/go/packages"
export PATH="$GOROOT/bin:$GOPATH/bin:$PATH"
go run main.go

%install
install -Dm 644 dlc.dat %{buildroot}%{_datadir}/v2ray/geosite.dat
install -Dm 644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%license LICENSE
%{_datadir}/v2ray/geosite.dat

%changelog
* Mon Mar 03 2025 zhullyb <zhullyb@outlook.com> - 20250302153845-1
- new version

* Fri Feb 28 2025 zhullyb <zhullyb@outlook.com> - 20250227085631-1
- new version

* Thu Feb 27 2025 zhullyb <zhullyb@outlook.com> - 20250226161858-1
- new version

* Mon Feb 24 2025 zhullyb <zhullyb@outlook.com> - 20250223232811-1
- new version

* Sat Feb 22 2025 zhullyb <zhullyb@outlook.com> - 20250221152129-1
- new version

* Thu Feb 20 2025 zhullyb <zhullyb@outlook.com> - 20250219031756-1
- new version

* Mon Feb 17 2025 zhullyb <zhullyb@outlook.com> - 20250216152937-1
- new version

* Sun Feb 16 2025 zhullyb <zhullyb@outlook.com> - 20250215051417-1
- new version

* Sat Feb 15 2025 zhullyb <zhullyb@outlook.com> - 20250214013716-1
- new version

* Thu Feb 13 2025 zhullyb <zhullyb@outlook.com> - 20250212030559-1
- new version

* Mon Feb 10 2025 zhullyb <zhullyb@outlook.com> - 20250209081110-1
- new version

* Sat Feb 08 2025 zhullyb <zhullyb@outlook.com> - 20250207120917-1
- new version

* Fri Feb 07 2025 zhullyb <zhullyb@outlook.com> - 20250206143205-1
- new version

* Sat Jan 25 2025 zhullyb <zhullyb@outlook.com> - 20250124154827-1
- new version

* Sun Dec 22 2024 zhullyb <zhullyb@outlook.com> - 20241221105938-1
- new version

* Tue Dec 10 2024 zhullyb <zhullyb@outlook.com> - 20241210004721-1
- new version

* Wed Nov 13 2024 zhullyb <zhullyb@outlook.com> - 20241112092643-1
- new version

* Tue Nov 12 2024 zhullyb <zhullyb@outlook.com> - 20241111125054-1
- new version

* Tue Nov 05 2024 zhullyb <zhullyb@outlook.com> - 20241104071109-1
- new version

* Sun Oct 20 2024 zhullyb <zhullyb@outlook.com> - 20241013063848-1
- new version

* Sat Oct 19 2024 zhullyb <zhullyb@outlook.com> - null-1
- new version

* Mon Oct 14 2024 zhullyb <zhullyb@outlook.com> - 20241013063848-1
- new version

* Tue Oct 08 2024 zhullyb <zhullyb@outlook.com> - 20241007202930-1
- new version

* Sat Sep 21 2024 zhullyb <zhullyb@outlook.com> - 20240920063125-1
- new version

* Sun Sep 15 2024 zhullyb <zhullyb@outlook.com> - 20240914091803-1
- new version

* Sun Sep 08 2024 zhullyb <zhullyb@outlook.com> - 20240907043125-1
- new version

* Fri Sep 06 2024 zhullyb <zhullyb@outlook.com> - 20240905162746-1
- new version

* Wed Sep 04 2024 zhullyb <zhullyb@outlook.com> - 20240903080831-1
- new version

* Sun Sep 01 2024 zhullyb <zhullyb@outlook.com> - 20240831202649-1
- new version

* Fri Aug 30 2024 zhullyb <zhullyb@outlook.com> - 20240829063032-1
- new version

* Tue Aug 27 2024 zhullyb <zhullyb@outlook.com> - 20240826041130-1
- new version

* Sat Aug 24 2024 zhullyb <zhullyb@outlook.com> - 20240823035651-1
- new version

* Sun Aug 18 2024 zhullyb <zhullyb@outlook.com> - 20240817092737-1
- new version

* Thu Aug 15 2024 zhullyb <zhullyb@outlook.com> - 20240814034058-1
- new version

* Sun Aug 11 2024 zhullyb <zhullyb@outlook.com> - 20240810010807-1
- new version

* Fri Aug 09 2024 zhullyb <zhullyb@outlook.com> - 20240808133326-1
- new version

* Thu Aug 08 2024 zhullyb <zhullyb@outlook.com> - 20240807074444-1
- new version

* Sat Jul 27 2024 zhullyb <zhullyb@outlook.com> - 20240726161926-1
- new version

* Sun Jul 21 2024 zhullyb <zhullyb@outlook.com> - 20240720181558-1
- new version

* Sun Jul 14 2024 zhullyb <zhullyb@outlook.com> - 20240713050854-1
- new version

* Thu Jul 11 2024 zhullyb <zhullyb@outlook.com> - 20240710044910-1
- new version

* Wed Jul 10 2024 zhullyb <zhullyb@outlook.com> - 20240709143535-1
- new version

* Tue Jul 09 2024 zhullyb <zhullyb@outlook.com> - 20240708041141-1
- new version

* Mon Jul 08 2024 zhullyb <zhullyb@outlook.com> - 20240707162925-1
- new version

* Tue Jun 25 2024 zhullyb <zhullyb@outlook.com> - 20240624143214-1
- new version

* Sat Jun 22 2024 zhullyb <zhullyb@outlook.com> - 20240621160143-1
- new version

* Sat Jun 15 2024 zhullyb <zhullyb@outlook.com> - 20240614093027-1
- new version

* Thu Jun 13 2024 zhullyb <zhullyb@outlook.com> - 20240612095513-1
- new version

* Wed Jun 05 2024 zhullyb <zhullyb@outlook.com> - 20240604215500-1
- new version

* Thu May 09 2024 zhullyb <zhullyb@outlook.com> - 20240508170917-1
- new version

* Mon May 06 2024 zhullyb <zhullyb@outlook.com> - 20240505132300-1
- new version

* Sun May 05 2024 zhullyb <zhullyb@outlook.com> - 20240504141043-1
- new version

* Sat Apr 27 2024 zhullyb <zhullyb@outlook.com> - 20240426060244-1
- new version

* Fri Dec 01 2023 zhullyb <zhullyb@outlook.com> - 20231128180936-1
- new version

* Sun Mar 19 2023 zhullyb <zhullyb@outlook.com> - 20230318081709-1
- First Version

