FROM ubuntu:kinetic

LABEL MAINTAINER="Eduardo Rojas"

ENV DEBIAN_FRONTEND nointeractive

#necesario para las tools
RUN apt update -y && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt install -y \
    net-tools \
    iputils-ping \
    git \
    curl \ 
    wget \
    zip \
    python3 python3-pip \
    libcurl4-openssl-dev \
    make \
    zlib1g-dev  \
    gawk \
    g++ \
    gcc \
    libreadline6-dev \
    libssl-dev \
    libyaml-dev \
    libsqlite3-dev \
    sqlite3 \
    autoconf \
    libgdbm-dev \
    libncurses5-dev \
    automake \ 
    libtool \
    bison \
    pkg-config \ 
    ruby \
    ruby-bundler \ 
    ruby-dev \
    golang

WORKDIR /root

RUN mkdir ${HOME}/arsenal && \
    mkdir ${HOME}/wordlists

#tools
RUN apt install -y \
    sqlmap \
    wfuzz \
    nmap \
    dirb \
    dnsrecon

#dirsearch
RUN git clone https://github.com/maurosoria/dirsearch.git ${HOME}/arsenal/dirsearch/ && \
        ln -sf ${HOME}/arsenal/dirsearch/dirsearch.py /usr/local/bin/dirsearch
#searchploit
RUN	git clone https://github.com/offensive-security/exploitdb.git ${HOME}/arsenal/exploitdb && \
		sed 's|path_array+=(.*)|path_array+=("${HOME}/arsenal/exploitdb")|g' ${HOME}/arsenal/exploitdb/.searchsploit_rc > ~/.searchsploit_rc && \
		ln -sf ${HOME}/arsenal/exploitdb/searchsploit /usr/local/bin/searchsploit

#sublister
RUN git clone https://github.com/aboul3la/Sublist3r.git ${HOME}/arsenal/Sublist3r/ && \
    pip3 install -r ${HOME}/arsenal/Sublist3r/requirements.txt && \
    ln -s ${HOME}/arsenal/Sublist3r/sublist3r.py /usr/local/bin/sublist3r

#wafw00f
RUN git clone https://github.com/EnableSecurity/wafw00f.git ${HOME}/arsenal/wafw00f/ && \
    cd ${HOME}/arsenal/wafw00f/ && \
    python3 setup.py install && cd ${HOME}

#wordpress wpscan
RUN gem install wpscan

# theHarvester
RUN git clone https://github.com/AlexisAhmed/theHarvester.git ${HOME}/arsenal/theHarvester && \
    pip3 install -r ${HOME}/arsenal/theHarvester/requirements.txt && \
    ln -sf ${HOME}/arsenal/theHarvester/theHarvester.py /usr/local/bin/theHarvester

#webshell weevely
RUN git clone https://github.com/epinna/weevely3.git ${HOME}/arsenal/weevely/ && \
    pip3 install -r ${HOME}/arsenal/weevely/requirements.txt && \
    ln -sf ${HOME}/arsenal/weevely/weevely.py /usr/local/bin/weevely

#wss subdomain scanner
RUN git clone https://github.com/WHK102/wss.git ${HOME}/arsenal/wss/ && \
    pip3 install -r ${HOME}/arsenal/wss/requirements.txt && \
    ln -sf ${HOME}/arsenal/wss/wss.py /usr/local/bin/wss

#joomscan
RUN git clone https://github.com/OWASP/joomscan.git ${HOME}/arsenal/joomscan/ && \
    ln -sf ${HOME}/arsenal/joomscan/joomscan.pl /usr/local/bin/joomscan


# subfinder
RUN GO111MODULE=on go get -u -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder && \
    ln -sf ${HOME}/go/bin/subfinder /usr/local/bin/subfinder

#gobuster
RUN GO111MODULE=on go get -v github.com/OJ/gobuster && \
    ln -sf ${HOME}/go/bin/gobuster /usr/local/bin/gobuster

#ffuf
RUN   GO111MODULE=on go get -v github.com/ffuf/ffuf && \
    ln -sf ${HOME}/go/bin/ffuf /usr/local/bin/ffuf
#httprobe
RUN   GO111MODULE=on go get -v github.com/tomnomnom/httprobe && \
    ln -sf ${HOME}/go/bin/httprobe /usr/local/bin/httprobe

RUN wget -q https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/apache-user-enum-1.0.txt -P ${HOME}/wordlists/ && \
	wget -q https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/apache-user-enum-2.0.txt  -P ${HOME}/wordlists/ && \
	wget -q https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-1.0.txt -P ${HOME}/wordlists/  && \
	wget -q https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-2.3-big.txt -P ${HOME}/wordlists/  && \
	wget -q https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-2.3-medium.txt -P ${HOME}/wordlists/  && \
	wget -q https://github.com/praetorian-code/Hob0Rules/raw/master/wordlists/rockyou.txt.gz  -P ${HOME}/wordlists/