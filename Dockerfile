FROM debian:buster-slim
WORKDIR /
RUN apt update
RUN apt -y install make gcc libexosip2-dev libortp-dev libexosip2-11 libortp13 curl python3
COPY src /src/
RUN make -C /src 
RUN apt -y remove make gcc libexosip2-dev libortp-dev
RUN apt -y autoremove
RUN apt -y clean
RUN cp /src/sipbot /
RUN rm -r /src
COPY sipbot.py entrypoint.sh /
CMD ["/entrypoint.sh"]
