# Zotero Literature Tools

这个仓库保存 DOI/PMID、BibTeX、Zotero 导出和文献索引整理的轻量工具。

## 方法论文元数据字段

录入 Nature Methods 或其他方法论文时，除 DOI/PMID 外，建议补充：

- functional_category：preprocessing、trajectory、state_density、transcriptomics、spatial_context、integration_benchmark、rna_modification、foundation_models 或 cross_species；
- execution_mode：baseline-function、runtime-required、integration-required 或 manifest-only；
- official_repo、release/tag、checkpoint URL、许可证和 SHA-256；
- minimal_input、experimental_unit、baseline_to_compare 和 validation_status；
- 对 SCMMIB/scMultiBench 记录 integration task、modality pairing 和 split；
- 对 NaRMBench 记录 RNA002/RNA004 chemistry、ground-truth sites、retraining 状态和 site-level calibration。

这些字段可以直接和 [bioinformatics-literature-workbench](https://github.com/Threezs/bioinformatics-literature-workbench) 的 data/method_function_map.csv 对齐，并链接到 [nature-methods-bioinformatics-catalog](https://github.com/Threezs/nature-methods-bioinformatics-catalog) 的 catalog.csv。
