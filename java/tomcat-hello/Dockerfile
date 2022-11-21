FROM tomcat:8.0-alpine
LABEL maintainer="deepak@softwareyoga.com"

ADD tomcat-hello.war /usr/local/tomcat/webapps/
ADD hello.jsp /usr/local/tomcat/webapps/ROOT/
ADD test.jsp /usr/local/tomcat/webapps/ROOT/

EXPOSE 8080
CMD ["catalina.sh", "run"]