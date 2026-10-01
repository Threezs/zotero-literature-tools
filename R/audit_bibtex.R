#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) stop("Usage: Rscript R/audit_bibtex.R references.bib")
path <- args[[1]]
if (!file.exists(path)) stop("File not found: ", path)
txt <- paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")

keys <- sub("^@[^\\{]+\\{([^,]+),.*$", "\\1", regmatches(txt, gregexpr("@[^\\{]+\\{[^,]+,", txt))[[1]])
keys <- trimws(keys)
if (anyDuplicated(keys)) warning("Duplicate citation keys found")

doi_hits <- unlist(regmatches(txt, gregexpr("(?i)doi\\s*=\\s*[\\{\"]([^\\}\"]+)", txt, perl = TRUE)))
doi_hits <- tolower(gsub(".*[\\{\"]|[\\}\"].*", "", doi_hits))
doi_hits <- gsub("^https?://doi.org/", "", doi_hits)
doi_hits <- gsub("^doi:", "", doi_hits)
doi_hits <- trimws(doi_hits)
if (anyDuplicated(doi_hits)) warning("Duplicate DOI values found")

entries <- length(keys)
message("Audited ", entries, " BibTeX entries")
