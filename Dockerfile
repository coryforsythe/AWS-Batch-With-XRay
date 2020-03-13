#Pushed as awscory/xraysample:latest
FROM amazonlinux

RUN yum install -y python3

RUN mkdir -p /var/exampleCode
WORKDIR /var/exampleCode

ADD requirements.txt /var/exampleCode/requirements.txt
ADD example.py /var/exampleCode/example.py

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]