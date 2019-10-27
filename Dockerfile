FROM ubuntu:18.04

RUN apt-get -qy dist-upgrade \
    && apt-get update \
    && apt-get -qy install \
        sudo build-essential curl file git software-properties-common

# setup timezone
RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
    && apt-get install -y tzdata \
    && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get install -yq \
    fish

RUN useradd --user-group --create-home --no-log-init --shell /bin/bash ian
USER ian
WORKDIR /home/ian

CMD ["/usr/bin/fish"]