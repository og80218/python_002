#load default image
FROM python:3.6

#add project
COPY ./web /app/
WORKDIR /app

#install flask
RUN pip install -r requirements.txt

#run flask
ENTRYPOINT ["python"]
CMD ["app.py"]

