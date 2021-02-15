use cpython::{py_fn, py_module_initializer, PyResult, Python};

fn rs_hello_world(name: &str) -> String {
    format!("Hello {}! This message comes from Rust.", name)
}

fn rs_hello_world_py(_: Python, name: &str) -> PyResult<String> {
    let greeting = rs_hello_world(name);
    Ok(greeting)
}

py_module_initializer!(myrustlib, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(
        py,
        "rs_hello_world",
        py_fn!(py, rs_hello_world_py(name: &str)),
    )?;
    Ok(())
});
