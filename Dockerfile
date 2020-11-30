FROM python:3.8.5-slim
EXPOSE 8080

RUN groupadd -r chatbot
RUN useradd -r -u 1010 -g chatbot chatbot

RUN apt-get update && \
	apt-get upgrade -yqq && \
	apt-get install -y build-essential libpq-dev python3-dev rclone ffmpeg && \
	apt-get clean -yqq && \
	apt-get autoclean -yqq && \
	apt-get autoremove -yqq && \
	rm -rf /var/cache/apt/archives/* /var/cache/apt/*.bin /var/lib/apt/lists/*

WORKDIR /app
COPY app/requirements.txt /app/requirements.txt 
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY app /app

RUN chown -R chatbot /app
RUN mkdir -p /home/chatbot/.config/rclone && chown -R chatbot /home/chatbot
USER chatbot
ENTRYPOINT ["sh", "entrypoint.sh"]