
OBJ	=	ozidataset.o

include ../../GDALmake.opt

CPPFLAGS	:=	 $(CPPFLAGS)

default:	$(OBJ:.o=.$(OBJ_EXT))

clean:
	rm -f *.o $(O_OBJ)

install-obj:	$(O_OBJ:.o=.$(OBJ_EXT))
