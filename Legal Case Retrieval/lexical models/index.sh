python -m pyserini.index.lucene \
  --collection JsonCollection \
  --input /search/odin/TianGongQP/qian/COLIEE2023/lht_process/BM25/corpus \
  --index /search/odin/TianGongQP/qian/COLIEE2023/lht_process/BM25/index \
  --generator DefaultLuceneDocumentGenerator \
  --threads 128 \
  --storePositions --storeDocvectors --storeRaw \