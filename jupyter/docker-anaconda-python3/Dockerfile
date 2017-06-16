# Dockerfile - crh runs Jupyter notebook.
#
# ( keep this directory mostly empty )
#
# Pulling the continuumio image for
#  Python3 and anaconda install of Jupyter
#  to use for METIS prework for pandas which 
#  wants a Jupyter notebook.
#
# 1/ BUILD:
#   docker build -t supercrh/anaconda3-juptyer-for-pandas1 .
# 2/ as crh 
#   mkdir /home/crh/notebooks
# 3/ RUN:
#  Match up the host port of 8888 to the exported container port 8888.
#  Bind host volume /home/crh/notebooks inside docker container to /opt/notebooks.
#  docker run -it -p 8888:8888 -v /home/crh/git/dsp/jupyter/notebooks:/opt/notebooks supercrh/anaconda3-juptyer-for-pandas1
#

FROM continuumio/anaconda3
USER root
RUN /opt/conda/bin/conda install jupyter -y
#
# setup a crh user environment
RUN mkdir -p /home/crh
RUN useradd -d /home/crh crh
RUN chown -v -R crh /home/crh
RUN chmod -v -R u+w+X+r /home/crh
RUN ls -dl /home/crh
USER crh
WORKDIR ["/home/crh"]
RUN pwd
RUN ls -ld .
RUN whoami
RUN touch /home/crh/hi
EXPOSE 8888
VOLUME /opt/notebooks
CMD bash -c "cd /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"
