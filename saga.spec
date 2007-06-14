
%define name saga
%define libname %{mklibname %name}
%define version 0.6
%define release %mkrel 1

Name:		%name
Version:	%version
Release:	%release
Summary:	The SAGA C++ Framework is an implementation of the SAGA (Simple API for Grid Computing) API specification.
URL:		http://saga.cct.lsu.edu/
License:	BSD style
BuildRoot:	%{_tmppath}/%{name}-root
Group:		Development/Other
Source:		http://saga.cct.lsu.edu/downloads/libsaga++-src-%{version}.tar.gz
BuildRequires:	libboost-devel, libsqlite3_0-devel, postgresql-devel
BuildRequires:	libxmlrpc-c-devel, doxygen
BuildRequires:	libsoci-sqlite3-devel, libsoci-postgresql-devel, libsoci-mysql-devel, libsoci-firebird-devel
Requires:	%{mklibname boost 1}
Patch0:		saga_show_compile_cmd.patch

%description
The SAGA C++ Framework is the first implementation of the SAGA (Simple
API for Grid Computing) API specification. The SAGA specification has
been defined by the SAGA Research Group at OGF as a high-level API that
directly addresses the needs of Grid application developers.

The purpose of the open source SAGA C++ Framework is to enable an
application programmer to easily create Grid applications without getting
involved with any specific Grid middleware. This does not only greatly
reduce the implementation complexity of an application but also makes
it portable between various Grid ecosystems.

%package -n %{libname}
Summary:	The SAGA C++ Framework is an implementation of the SAGA (Simple API for Grid Computing) API specification.
Group:		Development/Other
Provides:	libsaga = %{version}-%{release}

%package -n %{libname}-devel
Summary:	The SAGA C++ Framework is an implementation of the SAGA (Simple API for Grid Computing) API specification.
Group:		Development/Other
Provides:	saga-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{libname}
The SAGA C++ Framework is the first implementation of the SAGA (Simple
API for Grid Computing) API specification. The SAGA specification has
been defined by the SAGA Research Group at OGF as a high-level API that
directly addresses the needs of Grid application developers.

The purpose of the open source SAGA C++ Framework is to enable an
application programmer to easily create Grid applications without getting
involved with any specific Grid middleware. This does not only greatly
reduce the implementation complexity of an application but also makes
it portable between various Grid ecosystems.

%description -n %{libname}-devel
The SAGA C++ Framework is the first implementation of the SAGA (Simple
API for Grid Computing) API specification. The SAGA specification has
been defined by the SAGA Research Group at OGF as a high-level API that
directly addresses the needs of Grid application developers.

The purpose of the open source SAGA C++ Framework is to enable an
application programmer to easily create Grid applications without getting
involved with any specific Grid middleware. This does not only greatly
reduce the implementation complexity of an application but also makes
it portable between various Grid ecosystems.

This package contains the developement files to compile applications
using saga.

%prep
%setup -q -n libsaga++-src-%{version}
%patch0 -p1

%build
%configure --with-backend=sqlite3,postgresql,mysql,firebird
cd src/impl/engine
make SAGA_LOCATION=%{_prefix}
cd ../../..
make SAGA_LOCATION=%{_prefix}

%install
make SAGA_LOCATION=$RPM_BUILD_ROOT%{_prefix} install

%clean
%{__rm} -Rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc CHANGES INSTALL LICENSE README
%{_libdir}
%{_datadir}/%{name}/*.ini

%files -n %{libname}-devel
%defattr(-,root,root)
%doc examples
%{_libdir}
%{_includedir}/%{name}
%{_includedir}/%{name}.hpp
%{_includedir}/boost
%{_datadir}/%{name}/make

