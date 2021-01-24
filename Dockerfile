FROM  python3.8-alpine3.10

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip

ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./urmart ./urmart

RUN chmod a+x wait-for-it.sh
RUN chown -R someone:someone ./
USER someone

EXPOSE 8000
CMD [ "python", "manage.py", "runserver," "0.0.0.0:8000" ]