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
%define _lein_jar leiningen-%{_ver}-standalone.jar

%description
Leiningen Build Tool (Box UK)

%prep
%setup 

%build
curl -o %{_lein_jar} \
        https://leiningen.s3.amazonaws.com/downloads/%{_lein_jar}

curl https://raw.github.com/technomancy/leiningen/master/bin/lein \
     | sed s/^LEIN_JAR/#LEIN_JAR/ \
     > lein

chmod 755 lein

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{name}/bin
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{name}/lib

cp lein $RPM_BUILD_ROOT%{_prefix}/%{name}/bin
cp %{_lein_jar} $RPM_BUILD_ROOT%{_prefix}/%{name}/lib

mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cat <<EOF >$RPM_BUILD_ROOT/etc/profile.d/%{name}.sh
PATH=%{_prefix}/%{name}/bin:$PATH
export PATH
LEIN_JAR=%{_prefix}/%{name}/lib/%{_lein_jar}
export LEIN_JAR
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

