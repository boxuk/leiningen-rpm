Name: boxuk-leiningen
Version: %{_ver}
Release: 1%{?dist}
Summary: Leiningen Build Tool
Group: Development/Tools
License: Propriatory
BuildArch: noarch
URL: https://github.com/boxuk/leiningen-rpm
Source: %{name}-%{version}.tar.gz
AutoReqProv: no

%define _gitrepository .
%define _prefix /usr/share
%define _lein_version 2.1.3
%define _lein_jar leiningen-%{_lein_version}-standalone.jar
%define _lein_downloads https://leiningen.s3.amazonaws.com/downloads
%define _lein_repo https://raw.github.com/technomancy/leiningen

%description
Leiningen Build Tool (Box UK Package)

%prep
%setup 

%build
curl -o %{_lein_jar} \
        %{_lein_downloads}/%{_lein_jar}

curl %{_lein_repo}/%{_lein_version}/bin/lein \
     | sed 's#LEIN_JAR=".*"#LEIN_JAR="%{_prefix}/%{name}/lib/%{_lein_jar}"#' \
     > lein

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{name}/bin
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{name}/lib

cp lein $RPM_BUILD_ROOT%{_prefix}/%{name}/bin
cp %{_lein_jar} $RPM_BUILD_ROOT%{_prefix}/%{name}/lib

mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cat <<EOF >$RPM_BUILD_ROOT/etc/profile.d/%{name}.sh
PATH=%{_prefix}/%{name}/bin:\$PATH
export PATH
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/%{name}
%attr(0755, root, root) /etc/profile.d/%{name}.sh

%post
chmod 755 %{_prefix}/%{name}/bin/lein
exit 0

