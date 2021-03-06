# base image (stripped down ubuntu for Docker)
FROM continuumio/miniconda3

# metadata
LABEL base.image="miniconda3"
LABEL version="1"
LABEL software="RGI"
LABEL software.version="5.1.0"
LABEL description="Tool to identify resistance genes using the CARD database"
LABEL website="https://card.mcmaster.ca/"
LABEL documentation="https://github.com/arpcard/rgi/blob/master/README.rst"
LABEL license="https://github.com/arpcard/rgi/blob/master/LICENSE"
LABEL tags="Genomics"

# maintainer
MAINTAINER Finlay Maguire <finlaymaguire@gmail.com>

# get some system essentials
RUN apt-get update && apt-get install -y wget && conda init bash

# install rgi and system dependencies
RUN conda create --name rgi --channel conda-forge --channel bioconda rgi 

# download latest card database
RUN mkdir -p /card_data
WORKDIR /card_data
RUN wget -O data.tar.bz2 https://card.mcmaster.ca/latest/data && \
        tar xvf data.tar.bz2 && pwd && ls
# install database
SHELL ["conda", "run", "-n", "rgi", "rgi", "load", "-i", "/card_data/card.json"]

WORKDIR /data
# set rgi executable as cmd to allow overriding
ENTRYPOINT ["conda", "run", "-n", "rgi", "rgi"]
