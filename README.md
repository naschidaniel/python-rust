# python-rust

A playground to test how well python and rust work together.

## Requirements

* python > 3.9.x
* rust > 1.50.x

## How to try it

1. The Rust function must be built.
2. The `myrustlib.so` can be imported into `python_and_rust.py`.
3. The script can be tested.

```
cd ./pyext-myrustlib/ && cargo build --release
cd ..
cp ./pyext-myrustlib/target/release/libmyrustlib.so ./myrustlib.so
python python_and_rust.py
```

The commands are also integrated for debugging in vscode.

## Further information

* Rust bindings for the python interpreter [https://github.com/dgrunwald/rust-cpython](https://github.com/dgrunwald/rust-cpython).
* This repo was inspired by [https://github.com/rochacbruno/rust-python-example](https://github.com/rochacbruno/rust-python-example).

## LICENSE

[GNU GENERAL PUBLIC LICENSE](./LICENSE.md)