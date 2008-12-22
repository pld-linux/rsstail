Summary:	RSS reader
Summary(hu.UTF-8):	RSS olvasó
Summary(pl.UTF-8):	Czytnik RSS
Name:		rsstail
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.vanheusden.com/rsstail/%{name}-%{version}.tgz
# Source0-md5:	1558fc8b0c9a8cb79e421f783f1ffc40
URL:		http://www.vanheusden.com/rsstail/
BuildRequires:	libmrss-devel
Requires:	libmrss
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSSTail is more or less an rss reader: it monitors an rss-feed and if
it detects a new entry it'll emit only that new entry.

%description -l hu.UTF-8
RSSTail több vagy kevesebb, mint egy rss olvasó: ellenőriz egy
rss-forrást és ha új bejegyzést talál, csak az új bejegyzést jeleníti
meg.

%description -l pl.UTF-8
RSSTail jest czytnikiem RSS. Monitoruje zadany kanał RSS i jeśli
pojawia się nowa pozycja, wyświetla tylko tę nową pozycję.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/rsstail
%{_mandir}/man1/rsstail.1*
