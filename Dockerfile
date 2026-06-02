FROM ghcr.io/itsleeds/tds:latest

# Install Python dependencies in the system environment for direct Quarto execution
RUN python3 -m pip install --no-cache-dir --break-system-packages \
    duckdb \
    pandas \
    pyarrow \
    jupyter-cache \
    ipykernel \
    plotly || \
    python3 -m pip install --no-cache-dir \
    duckdb \
    pandas \
    pyarrow \
    jupyter-cache \
    ipykernel \
    plotly

# Install R package dependencies
RUN Rscript -e "if (!requireNamespace('pak', quietly = TRUE)) install.packages('pak', repos = 'https://cloud.r-project.org')" \
  && Rscript -e "pak::pak('tdscience/tartu26')"
