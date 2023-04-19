python -m pyserini.search.lucene \
  --index /search/odin/TianGongQP/qian/COLIEE2023/lht_process/BM25/index \
  --topics //search/odin/TianGongQP/qian/COLIEE2023/lht_process/BM25/query.tsv \
  --output /search/odin/TianGongQP/qian/COLIEE2023/lht_process/BM25/output_bm25_all.tsv \
  --bm25 \
  --k1 3 \
  --b 1 \
  --hits 4451 \
  --threads 10 \
  --batch-size 16 \