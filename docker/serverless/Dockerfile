FROM python:3.8

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG SERVERLESS_VERSION=2.15.0

# update apt-get
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y docker.io

# Install Nodejs 12
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

# install yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | sh
ENV PATH /root/.yarn/bin:$PATH

# install aws-cli
RUN pip install --upgrade pip && pip install awscli

# install pip3
ADD ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# install serverless framework
RUN npm install -g serverless@$SERVERLESS_VERSION

# set aws key
RUN sls config credentials --provider aws --key $AWS_ACCESS_KEY_ID --secret $AWS_SECRET_ACCESS_KEY

# settings for runtime emulator
ENV HOST 0.0.0.0
EXPOSE 8000