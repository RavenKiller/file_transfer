FROM ubuntu:20.04
RUN apt-get update \
    && apt-get install -y apt-utils python3-pip \
    && pip install --upgrade pip --no-cache-dir \
    && pip install --upgrade setuptools tornado --no-cache-dir \
    && apt-get clean 
EXPOSE 5555
COPY . file_transfer
WORKDIR file_transfer
ENTRYPOINT ["python3","main.py"]