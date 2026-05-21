

normalize_log_cpm <- function(counts_matrix) {
  if (!is.matrix(counts_matrix) && !is.data.frame(counts_matrix)) {
    stop("counts_matrix must be a matrix or data.frame")
  }

  counts_matrix <- as.matrix(counts_matrix)

  lib_size <- colSums(counts_matrix)

  if (any(lib_size == 0)) {
    stop("Some samples have library size equal to zero")
  }

  cpm <- t(t(counts_matrix) / lib_size * 1e6)

  return(log2(cpm + 1))
}