FROM public.ecr.aws/lambda/python:3.11

RUN yum -y update && yum install -y pango curl
RUN curl https://fonts.gstatic.com/s/notosansjp/v52/-F62fjtqLzI2JPCgQBnw7HFoxgIO2lZ9hg.ttf -o /usr/share/fonts/NotoSansJP-Regular.ttf
COPY src $LAMBDA_TASK_ROOT/
WORKDIR $LAMBDA_TASK_ROOT
RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]1