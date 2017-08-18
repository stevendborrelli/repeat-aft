.. _concepts:

Concepts
========

A *paper* is a preprint or an article in a scientific publication.

A *variable* is a question about a paper. Most of our variables concern the
reproducibility of the analysis, e.g. "If you used Python to analyze your data,
did you specify which version?".

A *value* relates to exactly one paper and one variable. It is the answer to the
variable's question. Values can be produced automatically by plugins, or
supplied by users.

A *domain* is an area of knowledge or scientific subdiscipline, such as
"studies involving Electronic Health Records", "nuclear physics", or "studies
involving bats". It is the primary unit by which we distinguish which variables
are (ir)relevant to the reproducibility of a given paper. Variables and domains
are in many-to-many correspondence.

A *category* generally represents some element of methodology, such as "text
mining", "randomization", or "data collection"; but it is fundamentally a way of
grouping related variables, and we have more mundane categories such as
"funding" and "bibliography". Every variable belongs to a single category.
