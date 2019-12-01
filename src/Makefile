CC=gcc
CFLAGS=-g -Wall -pedantic -fstack-protector -D_FORTIFY_SOURCE=2 -Wextra -Wno-unused-parameter -fPIE -pie
LDFLAGS=-leXosip2 -losip2 -lrt -lm -lpthread -losipparser2 -lortp -zrelro -znow
SOURCES=main.c sdp.c sip.c log.c law.c filter.c \
		call.c spawn.c cmds.c config.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=sipbot

all:
	$(CC) $(SOURCES) $(CFLAGS) -o $(EXECUTABLE) $(LDFLAGS)

clean:
	rm -f $(EXECUTABLE)
