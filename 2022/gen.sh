#!/bin/bash

for DAY in {01..25}; do
    cargo new day${DAY}
    cp template.rs day${DAY}/src/main.rs
done