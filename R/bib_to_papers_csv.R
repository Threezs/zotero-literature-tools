#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) stop("Usage: Rscript R/bib_to_papers_csv.R input.bib output.csv")
if (!requireNamespace("bib2df", quietly = TRUE)) {
  stop("Install bib2df first: install.packages('bib2df')")
}
bib <- bib2df::bib2df(args[[1]])
get_col <- function(x, name) if (name %in% names(x)) as.character(x[[name]]) else ""
out <- data.frame(
  paper_id = paste0("P", seq_len(nrow(bib))),
  citation_key = get_col(bib, "KEY"),
  doi = get_col(bib, "DOI"),
  pmid = get_col(bib, "PMID"),
  title = get_col(bib, "TITLE"),
  year = get_col(bib, "YEAR"),
  journal = get_col(bib, "JOURNAL"),
  authors = get_col(bib, "AUTHOR"),
  abstract = get_col(bib, "ABSTRACT"),
  status = "inbox",
  stringsAsFactors = FALSE
)
write.csv(out, args[[2]], row.names = FALSE, na = "")
message("Wrote ", nrow(out), " rows to ", args[[2]])
