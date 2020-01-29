Name:		gdal
Version:	3.0.3
Release:	3
Summary:	GIS file format library
License:	MIT
URL:		http://www.gdal.org

Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	geos-devel >= 3.8.0
BuildRequires:	libjson-c-devel
BuildRequires:	libgeotiff-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	proj-devel >= 6.2.1
BuildRequires:	zlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	doxygen

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
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for GDAL.


%package libs
Summary:	GDAL file format library
Requires:	geos
Requires:	libjson-c2
Requires:	libgeotiff
Requires:	proj >= 6.2.1
Requires:	zlib
Requires:	libjpeg-devel
Requires:	libpng

%description libs
This package contains the GDAL file format library.

%package doc
Summary:	Documentation for GDAL
BuildArch:	noarch

%description doc
This package contains HTML and PDF documentation for GDAL.

%prep
%setup -q -n %{name}-%{version}
pushd gdal
autoreconf -fi
./configure \
	--sysconfdir=%{_sysconfdir}	\
	--prefix=%{_prefix}		\
	--libdir=%{_libdir}		\
	--mandir=%{_mandir}		\
	--bindir=%{_bindir}		\
	--without-pg			\
	--with-geos			\
	--with-geotiff			\
	--without-gif			\
	--without-gta			\
	--with-jpeg			\
	--with-libjson-c		\
	--without-jpeg12		\
	--without-liblzma		\
	--with-libtiff			\
	--with-libz			\
	--without-mdb			\
	--without-odbc			\
	--without-msg			\
	--without-pcraster		\
	--with-png			\
	--with-proj			\
	--without-sqlite3		\
	--with-threads			\
	--without-webp			\
	--without-xerces		\
	--enable-shared
popd

%build
pushd gdal
%{__make} -j4
%{__make} -j4 man
%{__make} -j4 docs
popd

%install
pushd gdal
make DESTDIR=%{buildroot}	\
	install	\
	install-man
popd

%check

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

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

%files libs
%doc gdal/LICENSE.TXT gdal/NEWS gdal/PROVENANCE.TXT gdal/COMMITTERS
%{_libdir}/libgdal.so.*
%{_datadir}/
%dir %{_libdir}/gdalplugins

%files devel
%{_bindir}/gdal-config*
%{_mandir}/man1/gdal-config.1*
%dir %{_includedir}/
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a

%files doc
%doc README.md

%changelog
* Wed Feb 5 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 3.0.3-3
- Specfile for SLES12
