Summary:	PKCS#11 engine for OpenSSL
Summary(pl):	Silnik PKCS#11 dla OpenSSL-a
Name:		openssl-engine-pkcs11
Version:	0.1.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.opensc.org/files/engine_pkcs11-%{version}.tar.gz
# Source0-md5:	5be3d186a486e5696f1508f539567851
URL:		http://www.opensc.org/engine_pkcs11/
BuildRequires:	libp11-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
Requires:	openssl >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
engine_pkcs11 is an implementation of an engine for OpenSSL. It can be
loaded using code, config file or command line and will pass any
function call by openssl to a PKCS#11 module. Engine_pkcs11 is meant
to be used with smart cards and software for using smart cards in
PKCS#11 format, such as OpenSC.

%description -l pl
engine_pkcs11 to implementacja silnika dla OpenSSL-a. Mo¿e byæ
wczytany przy u¿yciu kodu, pliku konfiguracyjnego i linii poleceñ;
przekazuje wszystkie wywo³ania funkcji openssl-a do modu³u PKCS#11.
engine_pkcs11 jest przeznaczony do u¿ywania z kartami procesorowymi i
oprogramowaniem do u¿ywania kart procesorowych w formacie PKCS#11,
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
