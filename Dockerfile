FROM public.ecr.aws/lambda/python:3.11

RUN yum -y update && yum install -y pango curl
RUN curl https://raw.githubusercontent.com/googlefonts/morisawa-biz-ud-gothic/main/fonts/ttf/BIZUDGothic-Bold.ttf -o /usr/share/fonts/BIZUDGothic-Bold.ttf \
  & curl https://raw.githubusercontent.com/googlefonts/morisawa-biz-ud-gothic/main/fonts/ttf/BIZUDGothic-Regular.ttf -o /usr/share/fonts/BIZUDGothic-Regular.ttf \
  & curl https://raw.githubusercontent.com/googlefonts/morisawa-biz-ud-gothic/main/fonts/ttf/BIZUDPGothic-Bold.ttf -o /usr/share/fonts/BIZUDPGothic-Bold.ttf \
  & curl https://raw.githubusercontent.com/googlefonts/morisawa-biz-ud-gothic/main/fonts/ttf/BIZUDPGothic-Regular.ttf -o /usr/share/fonts/BIZUDPGothic-Regular.ttf
COPY src $LAMBDA_TASK_ROOT/
WORKDIR $LAMBDA_TASK_ROOT
RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]