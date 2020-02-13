

include ../../../GDALmake.opt

OBJ	=	ogrogdidriver.o ogrogdidatasource.o ogrogdilayer.o

CPPFLAGS	:=	 $(OGDI_INCLUDE) $(PROJ_CFLAGS) $(CPPFLAGS)

default:	$(O_OBJ:.o=.$(OBJ_EXT))

$(O_OBJ):		ogrogdi.h

clean:
	rm -f *.o $(O_OBJ)
