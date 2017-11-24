# NOTE: versions >= 0.4 included in libp11.spec
Summary:	PKCS#11 engine for OpenSSL
Summary(pl.UTF-8):	Silnik PKCS#11 dla OpenSSL-a
Name:		openssl-engine-pkcs11
Version:	0.2.2
Release:	1.1
License:	BSD-like
Group:		Libraries
#Source0Download: https://github.com/OpenSC/engine_pkcs11/releases
Source0:	https://github.com/OpenSC/engine_pkcs11/releases/download/engine_pkcs11-%{version}/engine_pkcs11-%{version}.tar.gz
# Source0-md5:	ccf0105c7625eba203674bd4764b86e8
URL:		https://github.com/OpenSC/engine_pkcs11
BuildRequires:	libp11-devel >= 0.3.1
BuildRequires:	openssl-devel >= 0.9.8l-2
# for proxy_module detection
BuildRequires:	p11-kit-devel
BuildRequires:	pkgconfig
Requires:	libp11 >= 0.3.1
Requires:	openssl >= 0.9.8l-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
engine_pkcs11 is an implementation of an engine for OpenSSL. It can be
loaded using code, config file or command line and will pass any
function call by openssl to a PKCS#11 module. Engine_pkcs11 is meant
to be used with smart cards and software for using smart cards in
PKCS#11 format, such as OpenSC.

%description -l pl.UTF-8
engine_pkcs11 to implementacja silnika dla OpenSSL-a. Może być
wczytany przy użyciu kodu, pliku konfiguracyjnego i linii poleceń;
przekazuje wszystkie wywołania funkcji openssl-a do modułu PKCS#11.
engine_pkcs11 jest przeznaczony do używania z kartami procesorowymi i
oprogramowaniem do używania kart procesorowych w formacie PKCS#11,
takim jak OpenSC.

%prep
%setup -q -n engine_pkcs11-%{version}

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-enginesdir=/%{_lib}/engines
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_lib}/engines/libpkcs11.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/engine_pkcs11

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) /%{_lib}/engines/libpkcs11.so
