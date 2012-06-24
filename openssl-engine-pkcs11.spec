Summary:	PKCS#11 engine for OpenSSL
Summary(pl):	Silnik PKCS#11 dla OpenSSL-a
Name:		openssl-engine-pkcs11
Version:	0.1.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.opensc-project.org/files/engine_pkcs11/engine_pkcs11-%{version}.tar.gz
# Source0-md5:	26eb84950a10b7d869e41a50620ebf09
URL:		http://www.opensc-project.org/engine_pkcs11/
BuildRequires:	libp11-devel >= 0.2.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
Requires:	libp11 >= 0.2.1
Requires:	openssl >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
engine_pkcs11 is an implementation of an engine for OpenSSL. It can be
loaded using code, config file or command line and will pass any
function call by openssl to a PKCS#11 module. Engine_pkcs11 is meant
to be used with smart cards and software for using smart cards in
PKCS#11 format, such as OpenSC.

%description -l pl
engine_pkcs11 to implementacja silnika dla OpenSSL-a. Mo�e by�
wczytany przy u�yciu kodu, pliku konfiguracyjnego i linii polece�;
przekazuje wszystkie wywo�ania funkcji openssl-a do modu�u PKCS#11.
engine_pkcs11 jest przeznaczony do u�ywania z kartami procesorowymi i
oprogramowaniem do u�ywania kart procesorowych w formacie PKCS#11,
takim jak OpenSC.

%prep
%setup -q -n engine_pkcs11-%{version}

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/engines/engine_pkcs11.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{ChangeLog,*.{html,css}}
%dir %{_libdir}/engines
%attr(755,root,root) %{_libdir}/engines/engine_pkcs11.so
