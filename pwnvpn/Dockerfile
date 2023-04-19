FROM ubuntu:22.10
LABEL MAINTAINER="Eduardo Rojas"

ENV DEBIAN_FRONTEND nointeractive

RUN apt update -y && apt upgrade -y && apt autoremove -y && \
	apt install -y net-tools git curl wget iputils-ping zip openvpn && \
	mkdir vpn

WORKDIR /root/vpn

COPY auth auth

COPY torguard torguard