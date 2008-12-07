Summary:	RSS reader
Summary(pl.UTF-8):	Czytnik RSS
Name:		rsstail
Version:	1.4
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://www.vanheusden.com/rsstail/%{name}-%{version}.tgz
# Source0-md5:	b48341a469049e0c339be519999b7a4b
URL:		http://www.vanheusden.com/rsstail/
BuildRequires:	libmrss-devel
Requires:	libmrss
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSSTail is more or less an rss reader: it monitors an rss-feed and if
it detects a new entry it'll emit only that new entry.

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
