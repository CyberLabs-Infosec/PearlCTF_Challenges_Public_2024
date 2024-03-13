FROM --platform=linux/amd64 menoone/nimrod

RUN apt -yq update && \
    apt -yq install python3 && \
    apt -yq install python3-pip

RUN pip install z3-solver
COPY sol.py /tmp/sol.py

CMD /bin/sh; sleep infinity
