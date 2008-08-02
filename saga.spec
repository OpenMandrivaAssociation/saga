%define name saga
%define major 0
%define libname %mklibname %name %major
%define develname %mklibname %name
%define version 0.7
%define release %mkrel 5

Name:		%name
Version:	%version
Release:	%release
Summary:	The SAGA C++ Framework (Simple API for Grid Computing)
URL:		http://saga.cct.lsu.edu/
License:	BSD like
BuildRoot:	%{_tmppath}/%{name}-root
Group:		System/Cluster
Source:		http://saga.cct.lsu.edu/downloads/saga-c++-%{version}-src.tar.gz
BuildRequires:	libboost-devel, libsqlite3-devel, postgresql-devel
BuildRequires:	xmlrpc-c-devel
BuildRequires:	libsoci-sqlite3-devel, libsoci-postgresql-devel, libsoci-mysql-devel, libsoci-firebird-devel
ExclusiveArch:	%{ix86}
Requires:	%{mklibname boost 1}

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
Summary:	The SAGA C++ Framework (Simple API for Grid Computing)
Group:		System/Cluster
Provides:	libsaga = %{version}-%{release}

%package -n %{develname}
Summary:	The SAGA C++ Framework (Simple API for Grid Computing)
Group:		System/Cluster
Provides:	saga-devel = %{version}-%{release}
Provides:	libsaga-devel = %{version}-%{release}
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

%description -n %{develname}
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
%setup -q -n saga-c++-%{version}-src

%build
%configure --with-backend=sqlite3,postgresql,mysql,firebird
cd src/impl/engine
make SAGA_LOCATION=%{_prefix}
cd ../../..
make SAGA_LOCATION=%{_prefix}

%install
%{__rm} -Rf %{buildroot}
make SAGA_LOCATION=$RPM_BUILD_ROOT%{_prefix} install

# remove unwanted files
%{__rm} -Rf %{buildroot}%{_includedir}/soci %{buildroot}%{_includedir}/soci-sqlite3.h
%{__rm} -Rf %{buildroot}%{_bindir}/net_cat %{buildroot}%{_bindir}/shell

%clean
%{__rm} -Rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc CHANGES INSTALL LICENSE README
%{_libdir}/libsaga*
%{_datadir}/%{name}/*.ini

%files -n %{develname}
%defattr(-,root,root)
%doc examples
%{_libdir}
%{_includedir}/%{name}
%{_includedir}/%{name}.hpp
%{_includedir}/boost
%{_datadir}/%{name}/make

