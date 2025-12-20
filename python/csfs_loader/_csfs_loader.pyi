from typing import Optional, Union
from pathlib import Path
from typing_extensions import NotRequired, TypedDict

__version__: str

class ConversionStats(TypedDict):
    success: bool
    input_file: str
    output_file: str
    header_file: NotRequired[str]
    max_line_len: int
    chunk_size: int
    error: NotRequired[str]
    total_lines: NotRequired[int]
    csf_count: NotRequired[int]
    truncated_count: NotRequired[int]

class ParallelConversionStats(ConversionStats):
    num_workers: NotRequired[int]

class HeaderInfo(TypedDict):
    header_lines: int
    file_path: str
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    line4: NotRequired[str]
    line5: NotRequired[str]

def convert_csfs(
    input_path: Union[str, Path],
    output_path: Union[str, Path],
    max_line_len: Optional[int] = 256,
    chunk_size: Optional[int] = 100000
) -> ConversionStats: ...

def convert_csfs_parallel(
    input_path: Union[str, Path],
    output_path: Union[str, Path],
    max_line_len: Optional[int] = 256,
    chunk_size: Optional[int] = 50000,
    num_workers: Optional[int] = None
) -> ParallelConversionStats: ...

def get_parquet_info(input_path: Union[str, Path]) -> dict: ...

def csfs_header(input_path: Union[str, Path]) -> HeaderInfo: ...

class CSFProcessor:
    def __init__(
        self,
        max_line_len: Optional[int] = 256,
        chunk_size: Optional[int] = 30000
    ) -> None: ...

    def set_max_line_len(self, value: int) -> None: ...

    def set_chunk_size(self, value: int) -> None: ...

    def get_config(self) -> dict: ...

    def convert(
        self,
        input_path: Union[str, Path],
        output_path: Union[str, Path]
    ) -> ConversionStats: ...

    def convert_parallel(
        self,
        input_path: Union[str, Path],
        output_path: Union[str, Path],
        num_workers: Optional[int] = None
    ) -> ParallelConversionStats: ...

    def get_metadata(self, input_path: Union[str, Path]) -> dict: ...
