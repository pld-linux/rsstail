Summary:	RSS reader
Summary(hu.UTF-8):	RSS olvasó
Summary(pl.UTF-8):	Czytnik RSS
Name:		rsstail
Version:	1.6
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.vanheusden.com/rsstail/%{name}-%{version}.tgz
# Source0-md5:	b408fad1b8ae894e0f95ba660a5c4b8b
URL:		http://www.vanheusden.com/rsstail/
BuildRequires:	libmrss-devel
BuildRequires:	pkgconfig
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
%{__make} \
	CC="%{__cc}" \
	CFLAGS='%{rpmcppflags} %{rpmcflags} -DVERSION=\"%{version}\"' \
	LDFLAGS="%{rpmcflags} %{rpmldflags} $(pkg-config --libs mrss)"

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
