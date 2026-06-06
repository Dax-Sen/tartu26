pak::pak("tdscience/tartu26")
library(flowmapblue)
library(tidyverse)

url_flows <- "https://github.com/tdscience/tartu26/releases/download/v1/flows_seville_time.csv"
flows_seville_time <- read_csv(url_flows)
url_locations <- "https://github.com/tdscience/tartu26/releases/download/v1/locations_seville.csv"
locations_seville <- read_csv(url_locations)
flowmap_seville_interactive <- flowmapblue(
  locations = locations_seville,
  flows = flows_seville_time,
  mapboxAccessToken = Sys.getenv("MAPBOX_TOKEN"),
  darkMode = TRUE,
  animation = FALSE,
  clustering = TRUE
)
# 'Print' the object to render the widget directly:
# flowmap_seville_interactive
