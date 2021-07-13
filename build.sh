#!/bin/bash

cd ./riscverifier
cargo build 
cd ..

cd ./vectre/vectre
cargo build
cd ../..

cd uclid
sbt compile "set fork := true"
sbt universal:packageBin
cd target/universal/ && unzip -o uclid-0.9.5.zip
cd ../../../