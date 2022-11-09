FROM adoptopenjdk/openjdk11:latest

#
# Download the JDK 11 for Alpine Linux distribution
#

#ARG OPENJDK11_ALPINE_URL=https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_linux-x64_bin.tar.gz
#RUN apk update \
#  && apk add ca-certificates wget \
#  && mkdir -p /usr/lib/jvm \
#  && wget $OPENJDK11_ALPINE_URL \
#    | tar -zxC /usr/lib/jvm


#ENV LANG C.UTF-8
#ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
#ENV PATH=$PATH:$JAVA_HOME/bin

WORKDIR /app
RUN mkdir -p /app/src
COPY ./src /app/src

#
# Compile the Java source code to class files
#
RUN mkdir -p build/classes/main
RUN javac -d build/classes/main \
    src/main/java/module-info.java \
    src/main/java/fi/linuxbox/http/Main.java


CMD java --module-path build/classes/main -m http.server/fi.linuxbox.http.Main