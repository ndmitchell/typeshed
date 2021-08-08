import sys
from _typeshed.wsgi import WSGIEnvironment
from datetime import datetime, timedelta
from typing import Any, Callable, Iterable, Mapping, SupportsInt, Text, Tuple, Type, TypeVar, Union, overload

from .datastructures import (
    Accept,
    Authorization,
    ContentRange,
    ETags,
    Headers,
    HeaderSet,
    IfRange,
    Range,
    RequestCacheControl,
    TypeConversionDict,
    WWWAuthenticate,
)

if sys.version_info >= (3, 0):
    _Str = str
    _ToBytes = Union[bytes, bytearray, memoryview, str]
    _ETagData = Union[bytes, bytearray, memoryview]
else:
    _Str = TypeVar("_Str", str, unicode)
    _ToBytes = Union[bytes, bytearray, buffer, unicode]
    _ETagData = Union[str, unicode, bytearray, buffer, memoryview]

_T = TypeVar("_T")
_U = TypeVar("_U")

HTTP_STATUS_CODES: dict[int, str]

def wsgi_to_bytes(data: bytes | Text) -> bytes: ...
def bytes_to_wsgi(data: bytes) -> str: ...
def quote_header_value(value: Any, extra_chars: str = ..., allow_token: bool = ...) -> str: ...
def unquote_header_value(value: _Str, is_filename: bool = ...) -> _Str: ...
def dump_options_header(header: _Str | None, options: Mapping[_Str, Any]) -> _Str: ...
def dump_header(iterable: Iterable[Any] | dict[_Str, Any], allow_token: bool = ...) -> _Str: ...
def parse_list_header(value: _Str) -> list[_Str]: ...
@overload
def parse_dict_header(value: bytes | Text) -> dict[Text, Text | None]: ...
@overload
def parse_dict_header(value: bytes | Text, cls: Type[_T]) -> _T: ...
@overload
def parse_options_header(value: None, multiple: bool = ...) -> Tuple[str, dict[str, str | None]]: ...
@overload
def parse_options_header(value: _Str) -> Tuple[_Str, dict[_Str, _Str | None]]: ...

# actually returns Tuple[_Str, dict[_Str, _Str | None], ...]
@overload
def parse_options_header(value: _Str, multiple: bool = ...) -> Tuple[Any, ...]: ...
@overload
def parse_accept_header(value: Text | None) -> Accept: ...
@overload
def parse_accept_header(value: _Str | None, cls: Callable[[list[Tuple[str, float]] | None], _T]) -> _T: ...
@overload
def parse_cache_control_header(
    value: None | bytes | Text, on_update: Callable[[RequestCacheControl], Any] | None = ...
) -> RequestCacheControl: ...
@overload
def parse_cache_control_header(
    value: None | bytes | Text, on_update: _T, cls: Callable[[dict[Text, Text | None], _T], _U]
) -> _U: ...
@overload
def parse_cache_control_header(value: None | bytes | Text, *, cls: Callable[[dict[Text, Text | None], None], _U]) -> _U: ...
def parse_set_header(value: Text, on_update: Callable[[HeaderSet], Any] | None = ...) -> HeaderSet: ...
def parse_authorization_header(value: None | bytes | Text) -> Authorization | None: ...
def parse_www_authenticate_header(
    value: None | bytes | Text, on_update: Callable[[WWWAuthenticate], Any] | None = ...
) -> WWWAuthenticate: ...
def parse_if_range_header(value: Text | None) -> IfRange: ...
def parse_range_header(value: Text | None, make_inclusive: bool = ...) -> Range | None: ...
def parse_content_range_header(
    value: Text | None, on_update: Callable[[ContentRange], Any] | None = ...
) -> ContentRange | None: ...
def quote_etag(etag: _Str, weak: bool = ...) -> _Str: ...
def unquote_etag(etag: _Str | None) -> Tuple[_Str | None, _Str | None]: ...
def parse_etags(value: Text | None) -> ETags: ...
def generate_etag(data: _ETagData) -> str: ...
def parse_date(value: str | None) -> datetime | None: ...
def cookie_date(expires: None | float | datetime = ...) -> str: ...
def http_date(timestamp: None | float | datetime = ...) -> str: ...
def parse_age(value: SupportsInt | None = ...) -> timedelta | None: ...
def dump_age(age: None | timedelta | SupportsInt) -> str | None: ...
def is_resource_modified(
    environ: WSGIEnvironment,
    etag: Text | None = ...,
    data: _ETagData | None = ...,
    last_modified: None | Text | datetime = ...,
    ignore_if_range: bool = ...,
) -> bool: ...
def remove_entity_headers(headers: list[Tuple[Text, Text]] | Headers, allowed: Iterable[Text] = ...) -> None: ...
def remove_hop_by_hop_headers(headers: list[Tuple[Text, Text]] | Headers) -> None: ...
def is_entity_header(header: Text) -> bool: ...
def is_hop_by_hop_header(header: Text) -> bool: ...
@overload
def parse_cookie(
    header: None | WSGIEnvironment | Text | bytes, charset: Text = ..., errors: Text = ...
) -> TypeConversionDict[Any, Any]: ...
@overload
def parse_cookie(
    header: None | WSGIEnvironment | Text | bytes,
    charset: Text = ...,
    errors: Text = ...,
    cls: Callable[[Iterable[Tuple[Text, Text]]], _T] | None = ...,
) -> _T: ...
def dump_cookie(
    key: _ToBytes,
    value: _ToBytes = ...,
    max_age: None | float | timedelta = ...,
    expires: None | Text | float | datetime = ...,
    path: None | Tuple[Any, ...] | str | bytes = ...,
    domain: None | str | bytes = ...,
    secure: bool = ...,
    httponly: bool = ...,
    charset: Text = ...,
    sync_expires: bool = ...,
) -> str: ...
def is_byte_range_valid(start: int | None, stop: int | None, length: int | None) -> bool: ...
