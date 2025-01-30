#!/bin/bash

#solana-keygen new --outfile coinbase.json --no-passphrase
#solana-keygen new --outfile main.json --no-passphrase

COINBASE_PUBKEY=$(solana-keygen pubkey coinbase.json)
MAIN_PUBKEY=$(solana-keygen pubkey main.json)

echo "Coinbase pubkey: $COINBASE_PUBKEY"
echo "Main pubkey: $MAIN_PUBKEY"

for i in {1..100}
do
  random_amount=$(awk -v min=0 -v max=1 'BEGIN{srand(); print min+rand()*(max-min)}')
  solana -ud transfer -k coinbase.json $MAIN_PUBKEY $random_amount --allow-unfunded-recipient
  sleep $(awk -v min=0 -v max=1 'BEGIN{srand(); print min+rand()*(max-min)}')
  solana -ud transfer -k main.json $COINBASE_PUBKEY $random_amount --allow-unfunded-recipient
  sleep $(awk -v min=2 -v max=4 'BEGIN{srand(); print min+rand()*(max-min)}')
done