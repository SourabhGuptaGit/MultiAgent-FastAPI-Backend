FROM python:latest

WORKDIR /app

COPY ./src .
# RUN echo "Hello to the world !" > index.html

# docker run -it -p 3000:8000 sourabhguptadockerhub/test_demo:2.0
CMD ["python", "-m", "http.server", "8000"]


# docker push sourabhguptadockerhub/agentic_backend:tagname
# docker build -f DokerFile -t sourabhguptadockerhub/agentic_backend:tagname
# docker build -f DokerFile -t sourabhguptadockerhub/test_demo:1.0