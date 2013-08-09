Name: boxuk-leiningen
Version: %{_ver}
Release: 3%{?dist}
Summary: Leiningen Build Tool
Group: Development/Tools
License: Propriatory
BuildArch: noarch
URL: https://github.com/boxuk/leiningen-rpm
Source: %{name}-%{version}.tar.gz
AutoReqProv: no

%define _gitrepository .
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
     | sed 's#LEIN_JAR=".*"#LEIN_JAR="%{_usr}/share/java/%{_lein_jar}"#' \
     > lein

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_usr}/{bin,share/java}

cp lein $RPM_BUILD_ROOT%{_usr}/bin
cp %{_lein_jar} $RPM_BUILD_ROOT%{_usr}/share/java

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_usr}/bin/lein
%attr(644, root, root) %{_usr}/share/java/%{_lein_jar}

