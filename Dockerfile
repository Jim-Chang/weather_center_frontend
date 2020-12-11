FROM python:3.8.5-slim
EXPOSE 8080

RUN groupadd -r chatbot
RUN useradd -r -u 1010 -g chatbot chatbot

WORKDIR /app
COPY app/requirements.txt /app/requirements.txt 

RUN apt-get update && \
	apt-get upgrade -yqq && \
	apt-get install -y build-essential libpq-dev python3-dev rclone ffmpeg && \
	# Install python lib
	pip install --trusted-host pypi.python.org -r requirements.txt && \
	# Cleanup
	apt-get purge --yes build-essential libpq-dev python3-dev && \
	apt-get autoclean -yqq && \
	apt-get autoremove -yqq && \
	apt-get clean -yqq && \
	rm -rf /var/cache/apt/archives/* /var/cache/apt/*.bin /var/lib/apt/lists/*

RUN mkdir -p /home/chatbot/.config/rclone && \
	chown -R chatbot /home/chatbot && \
	mkdir /download && \
	chown -R chatbot /download

COPY app /app
RUN chown -R chatbot /app

USER chatbot
ENTRYPOINT ["sh", "entrypoint.sh"]