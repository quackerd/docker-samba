
FROM alpine:latest

COPY ./run.sh /opt/run.sh
COPY ./add-user-group.py /opt/add-user-group.py


RUN set -xe \
    && apk add --no-cache samba python3 \ 
    && mkdir /samba \
    && chmod +x /opt/run.sh \
    && chmod +x /opt/add-user-group.py

CMD ["/opt/run.sh"]

EXPOSE 137/udp
EXPOSE 138/udp
EXPOSE 139/tcp
EXPOSE 445/tcp
