# Get the latest ubuntu image
FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

# Create a directory for the development environment
WORKDIR /pyansys

# Install the required packages
RUN apt-get update && apt-get install -y python3 
RUN apt-get install -y pip
RUN apt-get install -y git

COPY /requirements/requirements_doc.txt .
RUN pip install --no-cache-dir -r requirements_doc.txt

RUN apt-get update -y
RUN apt-get install -y make
RUN apt-get install -y latexmk texlive-fonts-extra
RUN apt install graphicsmagick-imagemagick-compat -y

# Clone the pyansys-cheat-sheet repository
RUN git clone https://github.com/ansys/pyansys-cheat-sheet.git