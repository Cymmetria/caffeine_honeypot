FROM ubuntu

ADD ./config /etc/teapot-decoy/config
ADD build-temp/app /etc/teapot-decoy/app

RUN apt-get update
RUN apt-get install -y supervisor nginx uwsgi uwsgi-plugin-python python-pip redis-server

# Build venv
RUN pip install virtualenv
RUN virtualenv /etc/teapot-decoy/.teapot-venv
RUN /etc/teapot-decoy/.teapot-venv/bin/pip install -r /etc/teapot-decoy/config/requirements.txt

# Config nginx
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/teapot-decoy/config/nginx.conf /etc/nginx/sites-enabled/nginx.conf

ENTRYPOINT ["supervisord", "-c", "/etc/teapot-decoy/config/supervisor.conf"]
