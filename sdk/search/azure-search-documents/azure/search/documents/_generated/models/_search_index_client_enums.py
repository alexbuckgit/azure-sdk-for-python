# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.9.3)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Answers(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Answers."""

    NONE = "none"
    """Do not return answers for the query."""
    EXTRACTIVE = "extractive"
    """Extracts answer candidates from the contents of the documents returned in response to a query
    #: expressed as a question in natural language."""


class AutocompleteMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the mode for Autocomplete. The default is 'oneTerm'. Use 'twoTerms' to get shingles
    and 'oneTermWithContext' to use the current context in producing autocomplete terms.
    """

    ONE_TERM = "oneTerm"
    """Only one term is suggested. If the query has two terms, only the last term is completed. For
    #: example, if the input is 'washington medic', the suggested terms could include 'medicaid',
    #: 'medicare', and 'medicine'."""
    TWO_TERMS = "twoTerms"
    """Matching two-term phrases in the index will be suggested. For example, if the input is 'medic',
    #: the suggested terms could include 'medicare coverage' and 'medical assistant'."""
    ONE_TERM_WITH_CONTEXT = "oneTermWithContext"
    """Completes the last term in a query with two or more terms, where the last two terms are a
    #: phrase that exists in the index. For example, if the input is 'washington medic', the suggested
    #: terms could include 'washington medicaid' and 'washington medical'."""


class Captions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Captions."""

    NONE = "none"
    """Do not return captions for the query."""
    EXTRACTIVE = "extractive"
    """Extracts captions from the matching documents that contain passages relevant to the search
    #: query."""


class IndexActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operation to perform on a document in an indexing batch."""

    UPLOAD = "upload"
    """Inserts the document into the index if it is new and updates it if it exists. All fields are
    #: replaced in the update case."""
    MERGE = "merge"
    """Merges the specified field values with an existing document. If the document does not exist,
    #: the merge will fail. Any field you specify in a merge will replace the existing field in the
    #: document. This also applies to collections of primitive and complex types."""
    MERGE_OR_UPLOAD = "mergeOrUpload"
    """Behaves like merge if a document with the given key already exists in the index. If the
    #: document does not exist, it behaves like upload with a new document."""
    DELETE = "delete"
    """Removes the specified document from the index. Any field you specify in a delete operation
    #: other than the key field will be ignored. If you want to remove an individual field from a
    #: document, use merge instead and set the field explicitly to null."""


class QueryAnswerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This parameter is only valid if the query type is ``semantic``. If set, the query returns
    answers extracted from key passages in the highest ranked documents. The number of answers
    returned can be configured by appending the pipe character ``|`` followed by the
    ``count-<number of answers>`` option after the answers parameter value, such as
    ``extractive|count-3``. Default count is 1. The confidence threshold can be configured by
    appending the pipe character ``|`` followed by the ``threshold-<confidence threshold>`` option
    after the answers parameter value, such as ``extractive|threshold-0.9``. Default threshold is
    0.7.
    """

    NONE = "none"
    """Do not return answers for the query."""
    EXTRACTIVE = "extractive"
    """Extracts answer candidates from the contents of the documents returned in response to a query
    #: expressed as a question in natural language."""


class QueryCaptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This parameter is only valid if the query type is ``semantic``. If set, the query returns
    captions extracted from key passages in the highest ranked documents. When Captions is set to
    ``extractive``\ , highlighting is enabled by default, and can be configured by appending the
    pipe character ``|`` followed by the ``highlight-<true/false>`` option, such as
    ``extractive|highlight-true``. Defaults to ``None``.
    """

    NONE = "none"
    """Do not return captions for the query."""
    EXTRACTIVE = "extractive"
    """Extracts captions from the matching documents that contain passages relevant to the search
    #: query."""


class QueryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the syntax of the search query. The default is 'simple'. Use 'full' if your query
    uses the Lucene query syntax.
    """

    SIMPLE = "simple"
    """Uses the simple query syntax for searches. Search text is interpreted using a simple query
    #: language that allows for symbols such as +, * and "". Queries are evaluated across all
    #: searchable fields by default, unless the searchFields parameter is specified."""
    FULL = "full"
    """Uses the full Lucene query syntax for searches. Search text is interpreted using the Lucene
    #: query language which allows field-specific and weighted searches, as well as other advanced
    #: features."""


class ScoringStatistics(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A value that specifies whether we want to calculate scoring statistics (such as document
    frequency) globally for more consistent scoring, or locally, for lower latency. The default is
    'local'. Use 'global' to aggregate scoring statistics globally before scoring. Using global
    scoring statistics can increase latency of search queries.
    """

    LOCAL = "local"
    """The scoring statistics will be calculated locally for lower latency."""
    GLOBAL = "global"
    """The scoring statistics will be calculated globally for more consistent scoring."""


class SearchMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether any or all of the search terms must be matched in order to count the document
    as a match.
    """

    ANY = "any"
    """Any of the search terms must be matched in order to count the document as a match."""
    ALL = "all"
    """All of the search terms must be matched in order to count the document as a match."""


class SemanticErrorHandling(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allows the user to choose whether a semantic call should fail completely, or to return partial
    results.
    """

    PARTIAL = "partial"
    """If the semantic processing fails, partial results still return. The definition of partial
    #: results depends on what semantic step failed and what was the reason for failure."""
    FAIL = "fail"
    """If there is an exception during the semantic processing step, the query will fail and return
    #: the appropriate HTTP code depending on the error."""


class SemanticPartialResponseReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Reason that a partial response was returned for a semantic ranking request."""

    MAX_WAIT_EXCEEDED = "maxWaitExceeded"
    """If ``semanticMaxWaitInMilliseconds`` was set and the semantic processing duration exceeded that
    #: value. Only the base results were returned."""
    CAPACITY_OVERLOADED = "capacityOverloaded"
    """The request was throttled. Only the base results were returned."""
    TRANSIENT = "transient"
    """At least one step of the semantic process failed."""


class SemanticPartialResponseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of partial response that was returned for a semantic ranking request."""

    BASE_RESULTS = "baseResults"
    """Results without any semantic enrichment or reranking."""
    RERANKED_RESULTS = "rerankedResults"
    """Results have been reranked with the reranker model and will include semantic captions. They
    #: will not include any answers, answers highlights or caption highlights."""


class VectorFilterMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines whether or not filters are applied before or after the vector search is performed."""

    POST_FILTER = "postFilter"
    """The filter will be applied after the candidate set of vector results is returned. Depending on
    #: the filter selectivity, this can result in fewer results than requested by the parameter 'k'."""
    PRE_FILTER = "preFilter"
    """The filter will be applied before the search query."""


class VectorQueryKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of vector query being performed."""

    VECTOR = "vector"
    """Vector query where a raw vector value is provided."""
