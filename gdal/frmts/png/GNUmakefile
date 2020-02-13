# $Id$
#
# Makefile to build libpng using GNU Make and GCC.
#

include ../../GDALmake.opt

OBJ	=	pngdataset.o

CPPFLAGS	:=	$(CPPFLAGS)
# Enable this to compile with -Wextra -Werror and get around the jump complaint.
# CPPFLAGS += -Wno-clobbered

default:	$(OBJ:.o=.$(OBJ_EXT))

clean:
	rm -f *.o $(O_OBJ)

all:	$(OBJ:.o=.$(OBJ_EXT))

install-obj:	$(O_OBJ:.o=.$(OBJ_EXT))
