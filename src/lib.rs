use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use pyo3::types::PyPathBuf;
use std::path::Path;

// 导入原始函数
use super::*;

#[pyfunction]
#[pyo3(signature = (csfs_path, output_path, max_line_len=256, chunk_size=30000))]
fn py_convert_csf_text_to_parquet(
    csfs_path: &PyPathBuf,
    output_path: &PyPathBuf,
    max_line_len: usize,
    chunk_size: usize,
) -> PyResult<()> {
    let rust_csfs_path = Path::new(csfs_path.as_os_str());
    let rust_output_path = Path::new(output_path.as_os_str());

    convert_csf_text_to_parquet(rust_csfs_path, rust_output_path, max_line_len, chunk_size)
        .map_err(|e| PyValueError::new_err(format!("Conversion failed: {}", e)))
}

#[pyfunction]
fn py_read_csf_from_parquet(
    parquet_path: &PyPathBuf,
    limit: Option<usize>,
) -> PyResult<Vec<(String, String, String)>> {
    let rust_path = Path::new(parquet_path.as_os_str());

    read_csf_from_parquet(rust_path, limit)
        .map_err(|e| PyValueError::new_err(format!("Read failed: {}", e)))
}

#[pyfunction]
fn py_get_parquet_info(
    parquet_path: &PyPathBuf,
) -> PyResult<()> {
    let rust_path = Path::new(parquet_path.as_os_str());

    get_parquet_info(rust_path)
        .map_err(|e| PyValueError::new_err(format!("Info retrieval failed: {}", e)))
}

#[pymodule]
fn arrow_v(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(py_convert_csf_text_to_parquet, m)?)?;
    m.add_function(wrap_pyfunction!(py_read_csf_from_parquet, m)?)?;
    m.add_function(wrap_pyfunction!(py_get_parquet_info, m)?)?;

    // 添加版本信息
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;

    Ok(())
}