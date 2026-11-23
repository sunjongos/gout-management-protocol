# Gout Clinical Ontology Reference (llmwiki_gout_ontology.md)

| Node ID | Cluster | Title | Key Symbolic Variables | Linked Clinical Nodes |
| :--- | :--- | :--- | :--- | :--- |
| `[[WIKI-GOUT-01]]` | Root Cause | Uricase Deficiency & Renal Excretion Defect | `uricase_null`, `renal_excretion_ratio_66`, `urate_transporter` | `[[WIKI-GOUT-02]]`, `[[WIKI-GOUT-07]]` |
| `[[WIKI-GOUT-02]]` | Aggravating Factor | Alcohol, Lactate Competition & Beer Yeast Purine | `lactate_inhibition`, `urat1_competition`, `beer_hop_purine` | `[[WIKI-GOUT-01]]`, `[[WIKI-GOUT-05]]` |
| `[[WIKI-GOUT-03]]` | Aggravating Factor | Fructose Hepatic ATP Depletion & Rapid Urate Surge | `fructose_fructokinase`, `atp_depletion`, `amp_deaminase` | `[[WIKI-GOUT-04]]`, `[[WIKI-GOUT-05]]` |
| `[[WIKI-GOUT-04]]` | Lifestyle & Weight | Obesity Cell Load vs Plant Purine Safety | `adipocyte_turnover`, `caloric_restriction`, `plant_purine_safe` | `[[WIKI-GOUT-03]]`, `[[WIKI-GOUT-07]]` |
| `[[WIKI-GOUT-05]]` | Attack Trigger | Rapid Fluctuation Attack Trigger (Surge & Drop) | `delta_sua_rate`, `msu_surface_destabilization`, `nlrp3_inflammasome` | `[[WIKI-GOUT-02]]`, `[[WIKI-GOUT-06]]` |
| `[[WIKI-GOUT-06]]` | Acute Phase | Acute Anti-inflammatory Protocol & E-Stop | `nsaids_colchicine_steroid`, `elevation_ice`, `xoi_initiation_contraindication` | `[[WIKI-GOUT-05]]`, `[[WIKI-GOUT-07]]` |
| `[[WIKI-GOUT-07]]` | Chronic Phase | Urate Lowering Therapy (ULT) & Target Standards | `target_sua_60_or_50`, `xoi_allopurinol_febuxostat`, `prophylaxis_colchicine` | `[[WIKI-GOUT-01]]`, `[[WIKI-GOUT-04]]` |

---

### [[WIKI-GOUT-01]]: Uricase Deficiency & Renal Excretion Defect
- **Axioms**: Unlike other mammals, humans lack functional uricase enzyme. Elimination relies entirely on kidney (67%) and GI tract (33%). 80-90% of gout patients are under-excretors due to genetic polymorphism in renal transporters (URAT1, GLUT9, ABCG2).
- **Rule**: Dietary restriction alone lowers sUA by merely 1-2 mg/dL. Pharmacologic urate lowering is mandatory for sustained remission.

### [[WIKI-GOUT-02]]: Alcohol-Lactate Competition & Beer Toxicity
- **Mechanism**: Ethanol metabolism produces lactic acid (lactate), which competitively blocks renal uric acid excretion at URAT1.
- **Beer**: Contains both ethanol and high concentrations of purine nucleotides (guanosine from brewer's yeast). Worst beverage for hyperuricemia.

### [[WIKI-GOUT-03]]: Fructose Hepatic ATP Depletion
- **Mechanism**: Fructose bypasses phosphofructokinase control in hepatocytes. Rapid phosphorylation by fructokinase depletes intracellular ATP, yielding high levels of AMP which feeds directly into the purine degradation pathway, surging uric acid within minutes.

### [[WIKI-GOUT-04]]: Obesity & Plant Purine Myth
- **Weight Loss Priority**: Higher fat mass means higher cell turnover and higher basal uric acid production. Caloric deficit and gradual fat loss lower uric acid far more effectively than strict purine restriction.
- **Plant Purines**: Purines in vegetables (beans, lentils, mushrooms, spinach) are not associated with incident gout or recurrent flares. Do not restrict.

### [[WIKI-GOUT-05]]: Rapid Fluctuation Attack Trigger
- **Mechanism**: Sudden shifts in serum uric acid—both rapid spikes (binge drinking) AND rapid drops (crash starvation, severe fasting, sudden large XOI dose)—destabilize monosodium urate (MSU) crystals, shedding microcrystals that trigger NLRP3 inflammasome and IL-1beta release.

### [[WIKI-GOUT-06]]: Acute Flare Anti-Inflammatory Protocol
- **Action**: Immediate high-dose NSAID or low-dose colchicine (1.2mg load + 0.6mg 1hr later). Corticosteroid if renal/GI compromised.
- **Immune E-Stop**: Do NOT start allopurinol/febuxostat during an acute flare unless patient is already taking it stably.

### [[WIKI-GOUT-07]]: Chronic Urate Lowering Therapy (ULT)
- **Target**: Serum urate < 6.0 mg/dL (< 360 umol/L) for all; < 5.0 mg/dL (< 300 umol/L) for tophaceous gout.
- **Titration**: Start low (Febuxostat 20-40mg or Allopurinol 100mg) and titrate monthly.
- **Flare Prophylaxis**: Co-prescribe colchicine 0.6mg daily for first 3-6 months.
