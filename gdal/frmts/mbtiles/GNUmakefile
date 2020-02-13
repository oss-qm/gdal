
include ../../GDALmake.opt

OBJ	=	mbtilesdataset.o

CPPFLAGS	:=	-I../../ogr/ogrsf_frmts/geojson -I../../ogr/ogrsf_frmts/mvt $(JSON_INCLUDE) $(CPPFLAGS) -I../../ogr -I../../ogr/ogrsf_frmts/gpkg -I../../ogr/ogrsf_frmts/sqlite $(SQLITE_INC) -DHAVE_SQLITE

ifeq ($(HAVE_GEOS),yes)
CPPFLAGS 	:=	-DHAVE_GEOS=1 $(CPPFLAGS)
endif

default:	$(OBJ:.o=.$(OBJ_EXT))

clean:
	rm -f *.o $(O_OBJ)

install-obj:	$(O_OBJ:.o=.$(OBJ_EXT))

$(O_OBJ): ../../ogr/ogrsf_frmts/gpkg/gpkgmbtilescommon.h
