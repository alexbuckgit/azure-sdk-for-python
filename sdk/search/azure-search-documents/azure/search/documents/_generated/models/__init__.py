# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.12.3)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AutocompleteItem
from ._models_py3 import AutocompleteOptions
from ._models_py3 import AutocompleteRequest
from ._models_py3 import AutocompleteResult
from ._models_py3 import FacetResult
from ._models_py3 import IndexAction
from ._models_py3 import IndexBatch
from ._models_py3 import IndexDocumentsResult
from ._models_py3 import IndexingResult
from ._models_py3 import QueryAnswerResult
from ._models_py3 import QueryCaptionResult
from ._models_py3 import RequestOptions
from ._models_py3 import SearchDocumentsResult
from ._models_py3 import SearchError
from ._models_py3 import SearchOptions
from ._models_py3 import SearchRequest
from ._models_py3 import SearchResult
from ._models_py3 import SuggestDocumentsResult
from ._models_py3 import SuggestOptions
from ._models_py3 import SuggestRequest
from ._models_py3 import SuggestResult
from ._models_py3 import VectorQuery
from ._models_py3 import VectorizableTextQuery
from ._models_py3 import VectorizedQuery

from ._search_index_client_enums import AutocompleteMode
from ._search_index_client_enums import IndexActionType
from ._search_index_client_enums import QueryAnswerType
from ._search_index_client_enums import QueryCaptionType
from ._search_index_client_enums import QueryType
from ._search_index_client_enums import ScoringStatistics
from ._search_index_client_enums import SearchMode
from ._search_index_client_enums import SemanticErrorMode
from ._search_index_client_enums import SemanticErrorReason
from ._search_index_client_enums import SemanticSearchResultsType
from ._search_index_client_enums import VectorFilterMode
from ._search_index_client_enums import VectorQueryKind
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AutocompleteItem",
    "AutocompleteOptions",
    "AutocompleteRequest",
    "AutocompleteResult",
    "FacetResult",
    "IndexAction",
    "IndexBatch",
    "IndexDocumentsResult",
    "IndexingResult",
    "QueryAnswerResult",
    "QueryCaptionResult",
    "RequestOptions",
    "SearchDocumentsResult",
    "SearchError",
    "SearchOptions",
    "SearchRequest",
    "SearchResult",
    "SuggestDocumentsResult",
    "SuggestOptions",
    "SuggestRequest",
    "SuggestResult",
    "VectorQuery",
    "VectorizableTextQuery",
    "VectorizedQuery",
    "AutocompleteMode",
    "IndexActionType",
    "QueryAnswerType",
    "QueryCaptionType",
    "QueryType",
    "ScoringStatistics",
    "SearchMode",
    "SemanticErrorMode",
    "SemanticErrorReason",
    "SemanticSearchResultsType",
    "VectorFilterMode",
    "VectorQueryKind",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
