Summary:	PKCS#11 engine for OpenSSL
Summary(pl.UTF-8):	Silnik PKCS#11 dla OpenSSL-a
Name:		openssl-engine-pkcs11
Version:	0.1.5
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.opensc-project.org/files/engine_pkcs11/engine_pkcs11-%{version}.tar.gz
# Source0-md5:	840af6e54dc21445c54f74e15005ba4d
URL:		http://www.opensc-project.org/engine_pkcs11/
BuildRequires:	libp11-devel >= 0.2.4
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
Requires:	libp11 >= 0.2.4
Requires:	openssl >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%doc NEWS doc/{README,nonpersistent/{ChangeLog,wiki.out/*}}
%attr(755,root,root) %{_libdir}/engines/engine_pkcs11.so
