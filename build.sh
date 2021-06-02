#!/bin/bash

cd ./riscverifier
cargo build 
cd ..

cd ./vectre/vectre
cargo build
cd ../..
