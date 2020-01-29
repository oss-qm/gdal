
## breaks when off
%{!?enable_jpeg:      %global enable_jpeg      on}
%{!?enable_jpeg12:    %global enable_jpeg12    on}
%{!?enable_png:       %global enable_png       on}

## was default on
%{!?enable_geos:      %global enable_geos      off}

%{!?enable_pg:        %global enable_pg        off}
%{!?enable_gif:       %global enable_gif       off}
%{!?enable_gta:       %global enable_gta       off}
%{!?enable_liblzma:   %global enable_liblzma   off}
%{!?enable_mdb:       %global enable_mdb       off}
%{!?enable_odbc:      %global enable_odbc      off}
%{!?enable_msg:       %global enable_msg       off}
%{!?enable_pcraster:  %global enable_pcraster  off}
%{!?enable_sqlite3:   %global enable_sqlite3   off}
%{!?enable_threads:   %global enable_threads   on}
%{!?enable_webp:      %global enable_webp      off}
%{!?enable_xerces:    %global enable_xerces    off}

%global pkg_libs	libgdal26

%global opt_build_req() %if "%1" == "on" \
%if %# > 2 \
BuildRequires: %2 >= %3 \
%else \
BuildRequires: %2\
%endif \
%endif

%global opt_with(flag,opt) %if "%1" == "on" \
        --with-%2 \\\
%else \
        --without-%2 \\\
%endif

Name:		gdal
Version:	3.0.3
Release:	mtx.26
Summary:	GIS file format library
License:	MIT
URL:		http://www.gdal.org

Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	geos-devel >= 3.8.0
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	doxygen
BuildRequires:	proj-devel >= 6.2.1
BuildRequires:	libtiff-devel
BuildRequires:	libgeotiff-devel
BuildRequires:	libjson-c-devel
BuildRequires:	zlib-devel
%{opt_build_req %enable_png libpng-devel}
%{opt_build_req %enable_jpeg libjpeg-devel}

%description
Geospatial Data Abstraction Library (GDAL/OGR) is a cross platform
C++ translator library for raster and vector geospatial data formats.
As a library, it presents a single abstract data model to the calling
application for all supported formats. It also comes with a variety of
useful commandline utilities for data translation and processing.

It provides the primary data access engine for many applications.
GDAL/OGR is the most widely used geospatial data access library.


%package devel
Summary:	Development files for the GDAL file format library
Requires:	%pkg_libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for GDAL.

%files devel
%{_bindir}/gdal-config*
%{_mandir}/man1/gdal-config.1*
%dir %{_includedir}/
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a

%package -n %pkg_libs
Summary:	GDAL file format library

%description -n %pkg_libs
This package contains the GDAL file format library.

%files -n %pkg_libs
%doc gdal/LICENSE.TXT gdal/NEWS gdal/PROVENANCE.TXT gdal/COMMITTERS
%{_libdir}/libgdal.so.*
%{_datadir}/
%dir %{_libdir}/gdalplugins

%post -n %pkg_libs -p /sbin/ldconfig

%postun -n %pkg_libs -p /sbin/ldconfig

%package docs
Summary:	Documentation for GDAL
BuildArch:	noarch

%description docs
This package contains HTML and PDF documentation for GDAL.

%files docs
%doc README.md

%prep
%setup -q -n %{name}-%{version}
pushd gdal
autoreconf -fi
./configure \
	--sysconfdir=%{_sysconfdir}		\
	--prefix=%{_prefix}			\
	--libdir=%{_libdir}			\
	--mandir=%{_mandir}			\
	--bindir=%{_bindir}			\
	--enable-shared				\
	%{opt_with %enable_geos		geos}
	%{opt_with %enable_pg		pg}
	%{opt_with %enable_gif		gif}
	%{opt_with %enable_gta		gta}
	%{opt_with %enable_liblzma	liblzma}
	%{opt_with %enable_mdb		mdb}
	%{opt_with %enable_odbc		odbc}
	%{opt_with %enable_msg		msg}
	%{opt_with %enable_pcraster	pcraster}
	%{opt_with %enable_png		png}
	%{opt_with %enable_threads	threads}
	%{opt_with %enable_webp		webp}
	%{opt_with %enable_xerces	xerces}
	%{opt_with %enable_jpeg		jpeg}
	%{opt_with %enable_jpeg12	jpeg12}

popd

%build
pushd gdal
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} man
%{__make} %{?_smp_mflags} docs
popd

%install
pushd gdal
make DESTDIR=%{buildroot}	\
	install	\
	install-man
popd

%check

%files
%{_bindir}/gdallocationinfo
%{_bindir}/gdal_contour
%{_bindir}/gdal_rasterize
%{_bindir}/gdal_translate
%{_bindir}/gdaladdo
%{_bindir}/gdalinfo
%{_bindir}/gdaldem
%{_bindir}/gdalbuildvrt
%{_bindir}/gdaltindex
%{_bindir}/gdalwarp
%{_bindir}/gdal_grid
%{_bindir}/gdalenhance
%{_bindir}/gdalmanage
%{_bindir}/gdalserver
%{_bindir}/gdalsrsinfo
%{_bindir}/gdaltransform
%{_bindir}/nearblack
%{_bindir}/ogr*
%{_bindir}/testepsg
%{_bindir}/gnmanalyse
%{_bindir}/gnmmanage
%{_mandir}/man1/*.1*
%exclude %{_libdir}/*.la
%exclude %{_prefix}/etc/bash_completion.d/gdal-bash-completion.sh

%changelog
* Wed Feb 5 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 3.0.3-3
- Specfile for SLES12
