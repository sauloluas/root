#!/usr/bin/env bash

if (($# < 2)); then
  echo 'Número de argumentos inválido.' >&2
  exit 1
fi

sed -n "1p;/$1/p" "$2"
