# Master script for Canada-Ukraine Project

master <- c("ndjson", "dplyr", "stringr", 
            "labelled", "tidyverse", #clean_and_combine_data
            "haven", "lubridate",  #append_age_differences
            #none for variable_labels
            "xtable", "gridExtra", "fastDummies", "devtools", "TOSTER", #balance_tables
            "kableExtra", "showtext", "sysfonts", "ggtext", #descriptive_statistics.R
            "glue", "lfe", "lmtest", "sandwich", "modelsummary", #contrasts.R
            "cowplot", #plots.R
            "marginaleffects", #comparison_plots.R
            "boot", "caret", "rms", "htmlTable", #cross_validation.R
            "pandoc", #presentable_table.R
            "texreg", #regression_tables.R
            "flextable", "gt", "janitor", "kableExtra")

library(ndjson)
library(dplyr)
library(stringr)
library(lubridate)
library(tidyr)
library(jsonlite)
library(xml2)
library(rvest)

library(master)

# variable_labels.R generates a dataframe of variable names, variable descriptions, 
# and variable groupings. This dataframe is used in subsequent files 
# to group and relabel outcomes.
source("scripts/initial_cleaning.Rmd")

source("scripts/canada_mentions.Rmd")

# Maybe update this tomorrow in case she asks for it
source("scripts/ukraine_mentions.Rmd")

# You should try to incorporate every other word embedding file into this
source("scripts/word_embeddings.Rmd")

source("scripts/word_embeddings_extended.Rmd")

source("scripts/us_word_embeddings.Rmd")

source("scripts/us_dtm_word_movers.Rmd")

source("scripts/lemmatizaton.Rmd")
