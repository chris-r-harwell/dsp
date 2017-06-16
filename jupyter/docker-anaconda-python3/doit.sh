#!/bin/bash
#
docker build -t supercrh/anaconda3-juptyer-for-pandas1 .
docker run -it -p 8888:8888 -v /home/crh/git/dsp/jupyter/notebooks:/opt/notebooks supercrh/anaconda3-juptyer-for-pandas1

